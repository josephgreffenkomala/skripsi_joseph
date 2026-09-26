"""Muat Qwen3-0.6B lalu jawab satu pertanyaan, seluruhnya di komputer lokal."""

import argparse
import time
from pathlib import Path
from typing import Protocol

MODEL_ID = "Qwen/Qwen3-0.6B"
CACHE_DIR = Path(__file__).resolve().parent / ".cache" / "huggingface"


class TokenBatch(Protocol):
    """Nilai tensor minimal yang dikirim oleh Transformers ke streamer."""

    def numel(self) -> int:
        """Kembalikan jumlah token dalam tensor."""


class ProgressBar(Protocol):
    """Operasi progress bar yang dibutuhkan streamer."""

    def update(self, n: int = 1) -> object:
        """Majukan progress bar sebanyak ``n`` unit."""

    def refresh(self) -> object:
        """Gambar ulang progress bar."""


class TokenProgressStreamer:
    """Perbarui progress bar setiap kali model menghasilkan token baru."""

    def __init__(self, progress_bar: ProgressBar) -> None:
        """Simpan progress bar dan siapkan pengabaian token prompt pertama."""
        self.progress_bar = progress_bar
        self._next_tokens_are_prompt = True

    def put(self, value: TokenBatch) -> None:
        """Terima token dari ``generate`` dan hitung hanya token jawaban."""
        if self._next_tokens_are_prompt:
            self._next_tokens_are_prompt = False
            return
        self.progress_bar.update(value.numel())

    def end(self) -> None:
        """Pastikan pembaruan terakhir terlihat ketika generasi berhenti."""
        self.progress_bar.refresh()


def main() -> None:
    """Baca pertanyaan, muat model, lalu cetak token jawaban sebagai teks."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--prompt", default="Jelaskan apa itu model bahasa dalam dua kalimat sederhana."
    )
    parser.add_argument("--max-new-tokens", type=int, default=128)
    parser.add_argument(
        "--offline", action="store_true", help="Hanya gunakan file yang sudah diunduh."
    )
    args = parser.parse_args()
    if not args.prompt.strip():
        parser.error("Pertanyaan tidak boleh kosong.")
    if not 1 <= args.max_new_tokens <= 1024:
        parser.error("--max-new-tokens harus antara 1 dan 1024.")

    print(f"Model: {MODEL_ID} | Perangkat: CPU", flush=True)

    # Import setelah parsing supaya --help bisa dibuka sebelum instalasi library.
    import_started = time.perf_counter()
    print("[1/4] Mengimpor PyTorch dan Transformers...", flush=True)
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer, set_seed
    from tqdm.auto import tqdm

    print(
        f"      Selesai ({time.perf_counter() - import_started:.1f} detik).", flush=True
    )

    torch.set_num_threads(4)
    set_seed(42)

    tokenizer_started = time.perf_counter()
    print("[2/4] Memuat tokenizer...", flush=True)
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_ID, cache_dir=CACHE_DIR, local_files_only=args.offline
    )
    print(
        f"      Selesai ({time.perf_counter() - tokenizer_started:.1f} detik).",
        flush=True,
    )

    model_started = time.perf_counter()
    print("[3/4] Memuat bobot model ke RAM...", flush=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        cache_dir=CACHE_DIR,
        local_files_only=args.offline,
        torch_dtype=torch.float32,
        low_cpu_mem_usage=True,
    ).to("cpu")
    model.eval()
    print(
        f"      Selesai ({time.perf_counter() - model_started:.1f} detik).", flush=True
    )

    # 1. Susun pesan pengguna ke format percakapan yang dikenali Qwen.
    messages = [{"role": "user", "content": args.prompt}]
    text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True, enable_thinking=False
    )

    # 2. Ubah teks menjadi angka (ID token) dalam tensor PyTorch.
    inputs = tokenizer(text, return_tensors="pt")
    input_length = inputs.input_ids.shape[1]
    if input_length > 2048:
        parser.error(
            "Pertanyaan terlalu panjang. Batasi hingga 2048 token untuk latihan."
        )
    print(f"[4/4] Membuat jawaban dari input {input_length} token...", flush=True)

    # 3. Prediksi token lanjutan tanpa menghitung gradien untuk pelatihan.
    with tqdm(
        total=args.max_new_tokens,
        desc="Token jawaban",
        unit="token",
        dynamic_ncols=True,
    ) as progress_bar:
        streamer = TokenProgressStreamer(progress_bar)
        with torch.inference_mode():
            generated = model.generate(
                **inputs,
                max_new_tokens=args.max_new_tokens,
                do_sample=True,
                temperature=0.7,
                top_p=0.8,
                top_k=20,
                pad_token_id=tokenizer.eos_token_id,
                streamer=streamer,
            )

    # 4. Buang token pertanyaan; ubah hanya token jawaban kembali menjadi teks.
    answer_ids = generated[0, input_length:]
    answer = tokenizer.decode(answer_ids, skip_special_tokens=True)
    print(f"\nPertanyaan: {args.prompt}\n\nJawaban:\n{answer.strip()}")
    print(f"\nToken jawaban: {len(answer_ids)}")
    if len(answer_ids) == args.max_new_tokens:
        print(
            "Batas token tercapai; jawaban mungkin terpotong. Naikkan --max-new-tokens."
        )


if __name__ == "__main__":
    main()
