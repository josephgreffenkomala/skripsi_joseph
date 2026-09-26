# Belajar memuat Qwen3-0.6B dari nol

Folder ini untuk belajar menjalankan model bahasa lokal: beri pertanyaan, muat model,
lalu lihat jawabannya. Ini eksplorasi teknis, belum menetapkan topik atau model skripsi.

## 1. Model apa yang dipakai?

**`Qwen/Qwen3-0.6B`**, model percakapan resmi Qwen dengan ukuran nominal sekitar
600 juta parameter. Berdasarkan pengecekan katalog resmi pada 25 September 2026,
ini pilihan terbaru yang ditemukan untuk percakapan umum dengan ukuran tepat 0.6B.
Varian 0.6B untuk suara, embedding, reranking, atau moderasi memiliki tugas berbeda.
Qwen3.5 punya varian kecil 0.8B; itu tidak memenuhi permintaan ukuran 0.6B.

Sumber: [model card Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B),
[katalog resmi Qwen](https://huggingface.co/Qwen/models?search=0.6B),
[Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B).

Versi library di `requirements.txt` sengaja ditetapkan agar contoh stabil;
versi library berbeda dari versi model. Model diambil dari revisi `main` yang tersedia
ketika dijalankan online, sehingga revisi bobot belum dikunci untuk penelitian.

## 2. Istilah paling dasar

Bayangkan kamu ingin menjalankan mesin penjawab pertanyaan di laptop:

| Istilah | Arti sederhana |
| --- | --- |
| Python | Bahasa untuk menulis instruksi kepada komputer. |
| Script | File berisi instruksi Python, di sini `load_qwen.py`. |
| Library | Kumpulan alat siap pakai supaya kita tidak menulis semuanya sendiri. |
| Model | Jaringan perhitungan yang sudah dilatih untuk memprediksi kelanjutan teks. |
| Parameter/bobot | Angka-angka di dalam model yang dipelajari saat pelatihan. |
| 0.6B | Sekitar 0,6 miliar parameter; bukan ukuran file 0,6 GB. |
| Load/memuat | Membaca bobot dari penyimpanan ke memori agar bisa dihitung. |
| Prompt | Teks pertanyaan atau instruksi yang kita berikan. |
| Token | Potongan teks; bisa bagian kata, tanda baca, atau unsur lain. |
| Tokenizer | Alat untuk mengubah teks menjadi ID token dan sebaliknya. |
| Tensor | Wadah angka yang digunakan library untuk perhitungan model. |
| Inference | Memakai model terlatih untuk menghasilkan jawaban. |
| Training | Proses mengubah bobot model melalui pembelajaran dari data. |
| Cache | Tempat menyimpan unduhan supaya bisa dipakai lagi. |
| Virtual environment | Lingkungan library khusus proyek agar instalasinya terpisah. |

Kita melakukan **inference**. Mengajukan pertanyaan di script ini tidak melatih
ulang model dan tidak membuatnya mengingat percakapan berikutnya.

## 3. Struktur folder

```text
experiment/
├── README.md           ← panduan yang sedang kamu baca
├── load_qwen.py        ← program untuk memuat model dan menjawab satu pertanyaan
├── requirements.txt    ← daftar library dan versi yang digunakan
├── .gitignore          ← aturan agar file besar/lokal tidak masuk Git
├── .venv/              ← Python dan library lokal; muncul setelah instalasi
└── .cache/
    └── huggingface/    ← tokenizer, konfigurasi, dan bobot; muncul saat dijalankan
```

File/folder berawalan titik biasanya tersembunyi. Lihat dengan `ls -a`.
`.venv` dan `.cache` diabaikan Git. Bobot model tidak ditulis langsung ke kode Python.
Path cache dihitung dari lokasi script sehingga tetap sama meski script dipanggil
dari direktori lain.

Tiga library utama:

- **PyTorch (`torch`)** menjalankan perhitungan angka.
- **Transformers** menyediakan loader model, tokenizer, dan proses menghasilkan teks.
- **Accelerate** membantu loader memuat bobot dengan penggunaan memori yang lebih hemat.

## 4. Menjalankan contoh

Perintah berikut ditujukan untuk terminal Bash di Linux ini. Ketik perintahnya
tanpa menambahkan tanda `$`. `uv` sudah tersedia di lingkungan ini.

### Jika lingkungan sudah disiapkan

```bash
cd /home/joseph/skripsi/skripsi_joseph/experiment
source .venv/bin/activate
python load_qwen.py
```

`cd` memindahkan lokasi kerja terminal. `source` mengaktifkan lingkungan Python
khusus folder ini. `python load_qwen.py` menjalankan instruksi di file tersebut.

### Jika menyiapkan ulang dari awal

```bash
cd /home/joseph/skripsi/skripsi_joseph/experiment
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install torch==2.6.0 --index-url https://download.pytorch.org/whl/cpu
uv pip install -r requirements.txt
python load_qwen.py
```

Python 3.12 dipakai untuk kecocokan dengan versi library contoh. Instalasi pertama
memilih PyTorch CPU supaya tidak mengunduh paket CUDA yang besar. Script memang
menggunakan CPU meskipun dijalankan di komputer yang memiliki GPU.

Pemakaian pertama perlu internet untuk mengunduh model; bobot yang terunduh sekitar 1,5 GB
di disk, ditambah tokenizer, library, dan cache instalasi. Sediakan beberapa GB
ruang kosong. Script memakai float32 pada CPU: bobot di RAM membutuhkan kira-kira
3 GB, ditambah memori untuk perhitungan dan proses pemuatan. Itu perkiraan, bukan batas maksimum.
Jika RAM hampir penuh, tutup aplikasi berat terlebih dahulu. CPU bisa memerlukan
waktu cukup lama untuk menyelesaikan jawaban. Script menampilkan empat tahap beserta
waktu pemuatan dan progress bar jumlah token jawaban. Angka pada progress bar adalah
token yang benar-benar sudah dihasilkan, bukan perkiraan waktu. Progress bar dapat
selesai sebelum batas maksimum jika model lebih dahulu menghasilkan penanda akhir jawaban.

Ganti pertanyaan:

```bash
python load_qwen.py --prompt "Apa bedanya RAM dan penyimpanan? Jawab singkat."
```

Berikan ruang lebih panjang untuk jawaban:

```bash
python load_qwen.py --prompt "Jelaskan token dengan contoh sederhana." --max-new-tokens 256
```

Sesudah unduhan lengkap, coba tanpa mengambil file dari internet:

```bash
python load_qwen.py --offline --prompt "Berapa hasil 2 + 2?"
```

`--offline` memakai cache yang sudah ada. Setiap menjalankan script, model tetap
dibaca lagi ke RAM. Cache menghemat unduhan, bukan mempertahankan model di RAM.
Keluar dari lingkungan Python dengan `deactivate`.

## 5. Apa yang terjadi dari awal sampai muncul jawaban?

```text
Pertanyaanmu
    ↓
Chat template: susun pesan ke format percakapan Qwen
    ↓
Tokenizer: ubah teks menjadi deretan angka
    ↓
Model: hitung peluang token berikutnya
    ↓
Generate: pilih token, lalu ulangi hingga selesai atau mencapai batas
    ↓
Decode: ubah token jawaban menjadi teks yang bisa dibaca
```

Model tidak mengambil jawaban dari Google. Script ini melakukan perhitungan lokal
menggunakan bobot model. Jawaban dapat salah, terutama pada model kecil.

## 6. Membaca kode secara bertahap

Mulai dari `main()`, yaitu fungsi yang mengatur urutan kerja program.

1. **`argparse`** membaca opsi terminal seperti `--prompt`. Tanpa opsi, program
   memakai pertanyaan contoh. Input kosong dan batas token di luar 1–1024 ditolak.
2. **`MODEL_ID`** menunjuk repositori model di Hugging Face, tempat distribusi model.
3. **`AutoTokenizer.from_pretrained(...)`** mengambil aturan pemecahan teks.
4. **`AutoModelForCausalLM.from_pretrained(...)`** memuat model yang sudah dilatih.
   `CausalLM` di sini berarti model memprediksi token berikutnya dari token sebelumnya.
5. **`model.eval()`** mengatur perilaku model untuk evaluasi/inference.
6. **`messages`** berisi satu pesan dengan peran `user`. Ini format data percakapan.
7. **`apply_chat_template(...)`** menambahkan penanda percakapan yang dikenali model.
   `enable_thinking=False` dipilih untuk latihan jawaban langsung. Kita belum
   menambahkan mode thinking agar contoh awal tetap sederhana.
8. **`return_tensors="pt"`** meminta keluaran tokenizer berupa tensor PyTorch.
9. **`torch.inference_mode()`** menonaktifkan pencatatan gradien yang dipakai saat training.
10. **`model.generate(...)`** menghasilkan token baru. `max_new_tokens` membatasi
    jumlah token tambahan, bukan jumlah kata atau panjang input.
11. **`generated[0, input_length:]`** mengambil hasil pertama, lalu membuang bagian
    input. Tanpa langkah ini, pertanyaan ikut tercetak sebagai jawaban.
12. **`tokenizer.decode(...)`** mengubah token baru kembali menjadi teks.

Pengaturan sampling memilih dari beberapa kemungkinan token: `temperature`
mengatur ketajaman distribusi peluang, sedangkan `top_p` dan `top_k` membatasi
kandidat. Untuk awal, biarkan nilainya tetap. Seed 42 membantu mengulang percobaan,
tetapi bukan jaminan hasil identik di semua perangkat dan versi library.

`if __name__ == "__main__":` memastikan `main()` dijalankan ketika file ini
dipanggil sebagai program. Import library berat diletakkan setelah pembacaan opsi
agar `python load_qwen.py --help` tetap bisa dipakai sebelum library terpasang.

## 7. Latihan kecil agar benar-benar paham

Lakukan satu per satu; jangan mengubah semuanya sekaligus.

1. Jalankan pertanyaan bawaan. Temukan baris nama model, perangkat, dan jumlah token.
2. Ubah hanya `--prompt`. Perhatikan bahwa script-nya sama, tetapi input berbeda.
3. Minta penjelasan panjang dengan batas 16 token, kemudian 128 token. Perhatikan
   kemungkinan jawaban terpotong. Batas token yang lebih besar bukan jaminan jawaban lebih benar.
4. Jalankan dengan `--offline` sesudah unduhan selesai. Ini menunjukkan peran cache.
5. Jelaskan dengan bahasamu sendiri alur: teks → token → model → token → teks.

Cek pemahaman:

- Mengapa 0.6B bukan 0,6 GB? Karena B menghitung parameter, sedangkan GB menghitung byte.
- Apakah prompt baru mengubah bobot? Tidak; script hanya melakukan inference.
- Mengapa perlu tokenizer? Perhitungan model memakai ID token, bukan huruf mentah.
- Mengapa pertanyaan dipotong dari `generated`? Hasil generate juga memuat input awal.
- Apakah program ini chatbot dengan ingatan? Belum; satu eksekusi hanya satu pertanyaan.

## 8. Jika terjadi kendala

| Gejala | Langkah pertama |
| --- | --- |
| `ModuleNotFoundError` | Aktifkan `.venv` dan jalankan instalasi requirements. |
| `KeyError: 'qwen3'` | Pastikan memakai Transformers dari requirements, bukan instalasi global lama. |
| Unduhan gagal | Periksa internet lalu jalankan ulang; unduhan menggunakan cache. |
| Mode offline gagal | Jalankan online terlebih dahulu sampai semua file berhasil dimuat. |
| Program berhenti dengan `Killed` | Periksa RAM; tutup aplikasi berat dan coba prompt pendek. |
| Jawaban lama muncul | Lihat tahap dan progress bar; bobot dibaca dari disk, lalu CPU menghasilkan token secara bertahap. |
| Jawaban terpotong | Naikkan `--max-new-tokens`, misalnya ke 256. |
| Jawaban keliru | Coba instruksi lebih sederhana dan periksa faktanya; keberhasilan program tidak berarti jawabannya benar. |

Untuk mempelajari API lebih lanjut: [panduan chat template Transformers](https://huggingface.co/docs/transformers/chat_templating)
dan [dokumentasi inference_mode PyTorch](https://docs.pytorch.org/docs/stable/generated/torch.autograd.grad_mode.inference_mode.html).

## 9. Hasil pengecekan awal

Pada 25 September 2026 di lingkungan ini (CPU, Python 3.12):

- Instalasi library berhasil, Ruff lint dan format lulus.
- Model berhasil diunduh dan dimuat. Revisi cache: `c1899de289a04d12100db370d81485cdf75e47ca`.
- Prompt `Berapa hasil 2 + 2? Jawab singkat dalam bahasa Indonesia.` menghasilkan
  `Hasil dari 2 + 2 adalah 4.` (13 token keluaran).
- Pengujian `--offline` dengan prompt `Sebutkan satu warna.` berhasil dari cache,
  menghasilkan `Jawaban: Kuning` (7 token keluaran).

Ini pemeriksaan bahwa alur program berjalan, bukan evaluasi kualitas model untuk skripsi.
