# Sequence-Level Routing Resources

## Knowledge

- [FiRST: Finetuning Router-Selective Transformers for Input-Adaptive Latency Reduction](https://aclanthology.org/2025.findings-emnlp.1197/)
  Contoh utama router per-layer yang membuat keputusan pada tingkat sequence dan menjaga kompatibilitas dengan KV cache. Gunakan untuk memahami arsitektur dan pelatihan router.
- [Prompt-based Depth Pruning of Large Language Models (PuDDing)](https://proceedings.mlr.press/v267/wee25a.html)
  Contoh prompt router yang memilih satu pola penghapusan layer dari sekumpulan kandidat. Gunakan untuk rancangan skripsi yang lebih sederhana daripada gate per-layer.
- [Dynamic Layer Selection in Decoder-only Transformers](https://arxiv.org/abs/2410.20022)
  Studi mengenai potensi per-sequence adaptation dan perbandingannya dengan early exit. Gunakan untuk memahami mengapa oracle study perlu dilakukan sebelum melatih router.

## Wisdom (Communities)

- Dosen pembimbing dan laboratorium komputasi kampus.
  Gunakan untuk menguji kelayakan scope, akses GPU, serta standar kontribusi tugas akhir.

## Gaps

- Belum dipilih implementasi open-source yang akan dijadikan titik awal eksperimen.
- Belum ditentukan komunitas teknis yang ingin diikuti pengguna untuk mendapatkan umpan balik implementasi.
