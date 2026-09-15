# TODO

Sumber naskah final proposal berada di `latex/proposal/`. Keputusan isi mengalir dari catatan eksplorasi ke `notes/exploration/topic-14-slm-quantization-indonesian-nlp.md`, lalu ke proposal LaTeX.

## Proposal

- [ ] Lengkapi identitas pada `latex/proposal/main.tex`: nama, NIM, pembimbing, dan dua penguji. Jenjang, gelar, tahun, program studi, dan departemen telah diisi.
- [x] Ganti `latex/proposal/figures/logougm.pdf` dengan logo resmi UGM.
- [x] Tulis intisari Bahasa Indonesia dan abstract Bahasa Inggris.
- [x] Lengkapi sitasi dasar SLM, kuantisasi, dan evaluasi efisiensi pada Bab 1.
- [x] Tambahkan diagram arsitektur sistem dan bagan alir metodologi pada Bab 3.
- [x] Konfirmasi jadwal penelitian enam bulan pada Bab 4.
- [x] Pastikan seluruh sitasi tersedia di `latex/proposal/references.bib`.

## Keputusan Eksperimen

- [x] Eksperimen inti berhenti pada Q4_K_M; tipe IQ4 tidak disertakan.
- [x] Importance matrix tidak digunakan karena tipe IQ4 dikeluarkan dari eksperimen inti.
- [x] Tetapkan kriteria kelulusan pilot model, baseline presisi tinggi yang stabil, dan metode pengukuran peak RAM.
- [x] Kunci revisi checkpoint model, commit `llama.cpp`, prompt, parser, parameter decoding, dan jumlah pengulangan sistem sebelum evaluasi test set.
- [x] Masukkan explainability sebagai **analisis sekunder terarah** menggunakan token/word occlusion untuk membuat heatmap sensitivitas token sebelum dan sesudah kuantisasi.
  - Pilot wajib dilakukan pada Qwen3-0.6B dengan 5 sampel SmSA, baseline dan satu varian 4-bit. Catat keberhasilan eksekusi, waktu, RAM, serta kestabilan atribusi.
  - Jika pilot stabil, lanjutkan pada subset kecil yang seimbang (rekomendasi awal: 30 sampel), bukan seluruh test set.
  - Laporkan perubahan token penting, korelasi peringkat, dan contoh heatmap; tafsirkan sebagai sensitivitas terhadap penghilangan token, bukan alasan kognitif atau penjelasan kausal model.
  - Integrated Gradients tidak termasuk scope penelitian.
  - Material awal: [`notes/exploration/explainability-kuantisasi-sentimen.md`](notes/exploration/explainability-kuantisasi-sentimen.md), [Integrated Gradients](https://proceedings.mlr.press/v70/sundararajan17a.html), dan [input marginalization](https://aclanthology.org/2020.emnlp-main.255/).

## Skripsi

- [ ] Sesuaikan scaffold lama di `latex/skripsi/chapters/` menjadi struktur skripsi ilmiah akademik sebelum penulisan laporan akhir.
