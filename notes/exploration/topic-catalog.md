---
cssclasses:
  - full-width
---
# Katalog Kandidat Aktif Skripsi / Proposal

Tanggal: 2026-08-31

Updated: 2026-09-03

Status: EKSPLORASI — belum ada topik yang dipilih secara final

## Kandidat Aktif

| No. canonical | Kandidat | Fokus | Status |
| --- | --- | --- | --- |
| 01 | IndoAgentBench | Benchmark pasangan issue Indonesia–Inggris untuk mengukur kesenjangan bahasa pada coding agent tingkat repositori | Kandidat utama |
| 02 | Foundation-vs-Supervised Shortcut Attribution | Studi empiris shortcut learning pada foundation model dan supervised model menggunakan attribution sebagai alat diagnosis | Kandidat kuat untuk skripsi ilmiah akademik |
| 14 | Ketahanan Kuantisasi Lintas-SLM untuk NLP Bahasa Indonesia | Evaluasi degradasi relatif dan transisi kesalahan SLM multibahasa umum versus SLM berorientasi Asia Tenggara pada beberapa tingkat GGUF di CPU | Kandidat utama bersyarat; model dan novelty final menunggu pilot serta systematic mapping |
| 15 | Structured Pruning dan Kualitas XAI Model Klasifikasi Citra | Audit berpasangan explanation drift, faithfulness, dan localization pada model yang dipangkas dengan target MACs terkontrol | Kandidat layak bersyarat; novelty umum pruning--XAI telah memiliki pembanding dekat |

## Berkas Detail

- [`topic-01-indoagentbench.md`](topic-01-indoagentbench.md)
- [`topic-02-foundation-shortcut-attribution.md`](topic-02-foundation-shortcut-attribution.md)
- [`topic-14-slm-quantization-indonesian-nlp.md`](topic-14-slm-quantization-indonesian-nlp.md)
- [`topic-15-pruning-xai-image-classification.md`](topic-15-pruning-xai-image-classification.md)

## Ringkasan Pemilihan

**IndoAgentBench** paling matang untuk diturunkan menjadi proposal karena memiliki desain evaluasi berpasangan, audit ekuivalensi bilingual, dan analisis kegagalan yang jelas. **Foundation-vs-Supervised Shortcut Attribution** menawarkan kontribusi eksperimen yang kuat untuk menguji ketergantungan shortcut lintas paradigma pretraining. **Ketahanan Kuantisasi Lintas-SLM untuk NLP Bahasa Indonesia** adalah kandidat paling realistis terhadap constraint hardware: scope intinya maksimal tiga model, tiga representasi bobot, dan dua kondisi tugas. Novelty generik lintas-SLM telah gugur oleh SLMQuant dan pembanding lain; posisi yang masih layak adalah degradasi relatif serta transisi kesalahan pada model multibahasa umum versus model berorientasi Asia Tenggara dalam satu pipeline GGUF/CPU. **Structured Pruning dan Kualitas XAI** sesuai dengan minat Computer Vision--XAI dan memiliki rancangan eksperimen yang jelas, tetapi hanya layak bila novelty difokuskan pada evaluasi berpasangan prediction-preserving serta pemisahan drift, faithfulness, dan localization; pertanyaan umum pengaruh pruning terhadap explainability sudah diteliti. Seluruh kandidat aktif diposisikan sebagai skripsi ilmiah akademik dengan luaran utama berupa temuan empiris dan analisis ilmiah.

Kandidat lain telah dipindahkan ke [`archive/`](archive/README.md). Arsip dipertahankan sebagai riwayat keputusan agar ide dan hasil eksplorasi lama tidak hilang atau dieksplorasi ulang tanpa alasan.
