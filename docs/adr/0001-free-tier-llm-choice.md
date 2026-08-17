# ADR-0001: Pilihan Model LLM Free Tier (Gemini 2.0 Flash + Llama-3.3-70B)

Status: stored — ADR ini mengikat **jika** topik IndoAgentBench dipilih. Selama topik masih disimpan/belum di-accept, ADR ini berstatus pending dan tidak mengikat.

Konteks menentukan bahwa eksperimen IndoAgentBench membutuhkan 2 model LLM dari keluarga berbeda untuk mengukur apakah instruction language gap berbeda antar model. Rencana awal (catatan `indonesian-prompt-coding-agent-topic-2026-06-08.md`) adalah Claude 3.5 Sonnet (Anthropic) + DeepSeek-Coder (DeepSeek) via API berbayar, dengan estimasi biaya $120-340.

Verifikasi hardware penulis menunjukkan: AMD Ryzen 3 5300U, 9GB RAM, tidak ada GPU, 8.5GB disk kosong. Tidak memungkinkan menjalankan model coding agent lokal (bahkan model 7B membutuhkan VRAM di atas kapasitas). Verifikasi anggaran penulis: $0 (tidak ada dana untuk API berbayar).

Karena itu kita memilih 2 model via API free tier: Gemini 2.0 Flash (Google AI Studio free tier) dan Llama-3.3-70B (Groq free tier). Kedua model mewakili keluarga berbeda (Google vs Meta), memenuhi kebutuhan RQ2, dan tidak menunda eksekusi 6 bulan. Konsekuensi: jumlah pengulangan direduksi dari 3 menjadi 1 per kondisi untuk menghormati rate limit free tier; ini dicatat sebagai keterbatasan di Bab 6.

Pertimbangan yang ditolak:
- Claude 3.5 + DeepSeek-Coder berbayar: ditolak karena anggaran $0.
- Model lokal via Ollama/vLLM: ditolak karena tidak ada GPU.
- Cari dana/beasiswa: ditolak untuk sekarang karena menunda eksekusi 1-2 bulan; bisa dipertimbangkan lagi jika eksperimen pilot free tier menunjukkan hasil menjanjikan dan butuh konfirmasi dengan model berbeda.