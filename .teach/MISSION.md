# Mission: Memahami dan Merancang Sequence-Level Routing untuk Skripsi

## Why

Memahami sequence-level routing sampai mampu menentukan rancangan eksperimen yang benar-benar dapat diimplementasikan dan dipertanggungjawabkan kepada dosen pembimbing sebagai topik tugas akhir.

## Success looks like

- Dapat menjelaskan alur prompt, router, pemilihan route, dan decoding dengan bahasa sendiri.
- Dapat membedakan backbone, router, grouped layers, candidate routes, dan label route.
- Dapat merancang pilot yang menguji apakah routing adaptif lebih berguna daripada static skipping.
- Dapat membaca serta mengubah implementasi decoder-only SLM untuk eksperimen routing.

## Constraints

- Eksperimen lokal saat ini menggunakan CPU dan RAM sekitar 9 GB; eksperimen utama membutuhkan akses GPU eksternal.
- Scope harus tetap realistis untuk skripsi satu mahasiswa.
- Backbone, dataset, dan domain tugas final belum dikunci.

## Out of scope

- Melatih language model dari awal.
- Token-level routing dan pembuatan inference engine baru pada tahap awal.
- Reinforcement learning atau MCTS sebelum baseline sederhana terbukti layak.
