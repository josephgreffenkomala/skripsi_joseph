# Handoff: lanjutkan diagnosis sequence-level routing

Lanjutkan pekerjaan pada repo `/home/joseph/skripsi/skripsi_joseph`. Jawab dalam bahasa Indonesia, singkat dan langsung. Baca `AGENTS.md`, `routing_diagnostics/README.md`, dan skill lokal `modal` serta `python-code-quality` sebelum memakai platform/mengubah Python. Jangan membuat subagent tanpa instruksi eksplisit. User sudah mengizinkan menjalankan diagnosis di Modal melalui pesan **“run it”**; tidak perlu meminta izin ulang untuk melanjutkan job yang sama.

## Tujuan dan konteks

Topik skripsi: sequence-level routing Qwen3-0.6B untuk peringkasan XL-Sum Indonesia. Sebanyak 28 lapisan dibagi menjadi 7 kelompok; G1/G7 selalu aktif, lima bit router memilih G2–G6 sekali per artikel. Pelatihan router memakai target pencarian greedy berdasarkan teacher-forced NLL + penalti kelompok aktif, kemudian LoRA.

User menunjukkan ringkasan yang buruk dan khawatir ide routing tidak masuk akal. Kami membuat folder **`routing_diagnostics/`** untuk memisahkan tiga pertanyaan:

1. Kualitas model penuh sebelum vs sesudah LoRA pada **20 artikel validasi**.
2. Keragaman target/prediksi router dan perbandingan terhadap prediksi mayoritas konstan.
3. Semua **32 route pada 8 artikel validasi**, NLL dan generasi/ROUGE, termasuk oracle per artikel vs route tetap serta perbandingan pada kedalaman sama.

Gunakan train/validation untuk diagnosis. Distribusi test lama hanya audit deskriptif; jangan memilih konfigurasi berdasarkan test atau mengklaim oracle sebagai router yang bisa dipakai saat inferensi. Jangan mengubah proposal atau pipeline eksperimen lama dalam lanjutan ini kecuali diperlukan dan diinstruksikan user.

## PENTING: job probe masih berjalan

**Jangan langsung menjalankan job baru. Periksa run aktif terlebih dahulu.**

- Command aktif: `modal run -m routing_diagnostics.modal_app --stage probe`
- Modal app: `ap-LCcuJPqRSpLG9yNwss2g0O`
- Dashboard: https://modal.com/apps/josephgreffenkomala/main/ap-LCcuJPqRSpLG9yNwss2g0O
- Exec session ID dari chat sebelumnya: **61353**. Jika sesi tool masih tersedia, poll memakai `write_stdin`; jika tidak, periksa `modal app list` / `modal app logs` (gunakan `--help` untuk opsi). Jangan menganggap session ID lintas chat pasti tersedia.
- Nama Modal app: `qwen3-routing-diagnostics`.
- Volume: **`experiment-proposal-data`**; mount `/vol`.
- Output probe aktif: **`/vol/routing_diagnostics/20261102T213919Z_a2416dd5_probe`**.
- Terakhir terlihat **56/256 route selesai**: artikel kedua `160601_majalah_paedofil_inggris`, route `[1,0,1,1,1]`. Ini snapshot progres, bukan status live.
- Job belum dinyatakan selesai. Periksa state dan hasil aktual sebelum melaporkan sukses. Jika ternyata berhenti, baca failure artifact/log sebelum memutuskan rerun. Lanjutkan hanya tahap yang belum selesai, tidak mengulang baseline.

## Baseline dan audit SUDAH selesai, probe lama terhenti

Run gabungan sebelumnya: `/vol/routing_diagnostics/20261102T213256Z_a54af16c_all`. Baseline dan audit selesai; tahap probe berhenti pada mismatch token FP16. Jangan menganggap keseluruhan run ini sukses.

Artefak lengkap baseline/audit sudah diunduh dan dirapikan di:

`/home/joseph/skripsi/skripsi_joseph/routing_diagnostics/outputs/20261102T213256Z_a54af16c_all/`

File penting: `baseline_summary.json`, `baseline_report.md`, `baseline_examples.json`, `router_cached_summary.json`, `router_feature_drift.json`, `implementation_checks.json`, `saved_audit.json`, dan `manifest.json`.

### Hasil baseline pada 20 validation

| Metrik | Model penuh asli | Model penuh + LoRA |
| --- | ---: | ---: |
| NLL | 2.888589 | 1.839996 |
| ROUGE-1 F1 | 0.180640 | 0.212781 |
| ROUGE-2 F1 | 0.053843 | 0.047611 |
| ROUGE-L F1 | 0.123229 | 0.179227 |
| Rata-rata token keluaran | 201.70 | 54.05 |

Interpretasi: LoRA memperpendek ringkasan dan menaikkan ROUGE-1/L, tetapi ROUGE-2 sedikit turun. Jangan menyimpulkan peningkatan kualitas menyeluruh/faktualitas. Contoh masih dapat melewatkan informasi penting atau salah fakta; artikel asli dan keluaran tersedia untuk dibaca.

### Audit router

- Lambda terpilih **0.0**.
- Target train 500: `11011`: 379, `11111`: 114, `10111`: 5, `10011`: 2.
- Prediksi train: `11011`: 499, `11111`: 1. Akurasi route 0.760 vs mayoritas konstan 0.758.
- Target validation 100: `11011`: 72, `11111`: 26, `10011`: 2.
- Prediksi validation: **semua 100 `11011`**. Akurasi route **0.72**, sama dengan mayoritas konstan; bit accuracy 0.944 menutupi kegagalan memilih route berbeda.
- Pada 20 artikel, sebelum/sesudah adapter **adaptive-LoRA**, keputusan router tetap seluruhnya `11011`; proporsi keputusan berubah 0, perubahan absolut rata-rata probabilitas sekitar 0.009418. Feature drift tidak menjelaskan pola konstan pada sampel ini.
- Audit test lama (150) menghasilkan `11011` pada 149 artikel, `11111` pada 1 artikel.

### Temuan implementasi penting

**Bug prefill routing adaptif terkonfirmasi pada model sebenarnya dan Qwen kecil lokal.** `RouteController` mengganti modul setelah G1 lewat hook, tetapi loop Qwen sudah membuat salinan `self.layers[:]`. Akibatnya kelompok yang dipilih untuk dilewati tetap berjalan pada prefill pertama, baru dilewati saat decoding. Mekanisme ini perlu diperbaiki sebelum hasil lama dianggap implementasi rancangan yang setia. Belum membuktikan sebagai penyebab tunggal ringkasan buruk.

Route tetap dipasang sebelum forward, sehingga baseline dan probe tetap sah untuk diagnosis tersebut. Semua-lapisan-aktif, cache/tanpa-cache untuk route cek utama, serta loop manual lama vs native generation lulus setelah greedy dikunci.

## Perubahan kode selama eksekusi

Implementasi diagnosis hanya mengubah folder `routing_diagnostics/`; pipeline `experiment_proposal/` belum diperbaiki. Saat handoff awal belum ada commit. Setelah itu user meminta seluruh perubahan dikomit dan dipush ke GitHub; periksa `git log` dan `git status` untuk status terbaru.

1. Manifest sumber menyimpan `model_revision: null`. Kode sekarang hanya memulihkan revisi bila ada **tepat satu snapshot lengkap** di cache model. Revisi terpulihkan: **`c1899de289a04d12100db370d81485cdf75e47ca`**. Manifest diagnosis mempertahankan manifest sumber asli dan mencatat provenance pemulihan; keterbatasan historis harus diakui. Tidak diam-diam memakai `main`.
2. Transformers 4.51.3 sempat mengganti default `GenerationConfig` dengan default sampling Qwen. `generate_tokens()` kini memakai **`use_model_defaults=False`**, sehingga benar-benar greedy. Run baseline yang disebut di atas sudah memakai perbaikan ini. Run gagal sebelumnya `20261102T213132Z_c4ec9e3f_all` tidak dipakai untuk baseline kualitas.
3. Probe FP16 menemukan mismatch cached/uncached pada beberapa route dengan skipping besar. `check_cache_precision()` kini menyimpan mismatch dan menguji ulang pada FP32. Jika FP32 cocok, lanjut dengan label **`reduced_precision_mismatch_disappears_at_fp32`**; jika tetap berbeda, berhenti dengan failure artifact. Beberapa kasus pada artikel pertama sudah terkonfirmasi cocok pada FP32. Semua skor/generasi tetap FP16.
4. Saat kembali dari FP32, **buffer asli dipulihkan**, termasuk RoPE yang awalnya FP32. Jangan mengganti pemulihan ini dengan `.half()` saja karena bisa mengubah model untuk route berikutnya.
5. Tes tambahan mencakup model dengan default sampling, pemulihan revisi, threshold logits persis seperti kode sumber, serta pemulihan dtype/buffer pada retest cache.

Verifikasi terakhir: **11 tes lulus**, Ruff check dan format lulus. Tes memakai `experiment/.venv/bin/python`; Python global tersedia sebagai `python3`, bukan `python`. Dependensi model lokal tidak selengkap image Modal, jadi import ROUGE dibuat lazy.

## Langkah selanjutnya

1. Monitor job probe yang masih aktif. Beri update singkat bermakna selama pekerjaan berlangsung; jangan menarasikan snapshot yang sama terus-menerus.
2. Setelah selesai, unduh output probe:

   ```bash
   modal volume get experiment-proposal-data /routing_diagnostics/20261102T213919Z_a2416dd5_probe ./routing_diagnostics/outputs
   ```

   CLI menambahkan nama folder remote di bawah destination. Jangan memberi destination bernama run yang sama jika folder itu sudah ada, karena bisa menghasilkan direktori bersarang. `--force` hanya jika menimpa artefak diagnosis milik kita yang memang parsial.

3. Periksa `summary.json`, `route_probe_summary.json`, `route_probe.json`, `route_probe_report.md`, dan `probe_implementation_checks.json`.
4. Pastikan benar-benar **8 artikel × 32 route**, metrik finite, status cache, dan regret greedy. Bandingkan NLL-oracle dengan ROUGE-oracle; laporkan gain route adaptif potensial terutama pada kedalaman sama. Route tetap dan oracle dipilih/dinilai pada sampel sama, sehingga gain optimistis dan bukan hasil generalisasi router. Probe memakai backbone **tanpa LoRA**, bukan batas performa route setelah diadaptasi.
5. Gabungkan ringkasan hasil baseline/audit dan probe dalam satu laporan lokal yang mudah dibaca (misalnya `routing_diagnostics/outputs/diagnosis_complete/summary.md`), dengan provenance kedua run. Jangan mencampurkan artefak probe lama yang parsial sebagai hasil final.
6. Beri user hasil singkat dan tautan laporan. Arah interpretasi yang sudah didukung: belum perlu membatalkan topik; ada bug implementasi, router hampir konstan, dan baseline kualitas masih perlu perhatian. Tunggu hasil probe untuk menilai potensi adaptivitas; jangan mengarang kesimpulannya.

Perubahan user yang sudah ada sebelum pekerjaan: `.obsidian/workspace.json`, `TODO.md`, `experiment_proposal/evaluation/report.md`, serta beberapa folder Obsidian/Untitled. User kemudian secara eksplisit meminta **seluruh perubahan** dikomit dan dipush, termasuk perubahan tersebut. Jangan menimpanya. `routing_diagnostics/outputs/` tetap diabaikan Git, tetapi file lokal dapat ditautkan kepada user dan hasil remote tersedia di volume Modal.
