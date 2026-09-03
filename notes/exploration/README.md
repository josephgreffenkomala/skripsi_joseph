# Memori Canonical Eksplorasi Skripsi

Updated: 2026-09-03

Folder ini memisahkan kandidat aktif dari kandidat yang telah diarsipkan. Informasi baru tentang shortlist harus memperbarui `topic-catalog.md` atau salah satu file detail aktif. Riwayat kandidat yang dikeluarkan dari shortlist disimpan di `archive/` agar keputusan lama tetap dapat ditelusuri.

## Canonical files

- [`topic-catalog.md`](topic-catalog.md): indeks utama dan status kandidat aktif.
- [`topic-01-indoagentbench.md`](topic-01-indoagentbench.md): benchmark coding agent dengan pasangan instruksi Indonesia–Inggris.
- [`topic-02-foundation-shortcut-attribution.md`](topic-02-foundation-shortcut-attribution.md): studi shortcut learning foundation model versus supervised model.
- [`topic-14-slm-quantization-indonesian-nlp.md`](topic-14-slm-quantization-indonesian-nlp.md): evaluasi ketahanan kuantisasi lintas-SLM untuk Bahasa Indonesia, mencakup degradasi relatif, transisi kesalahan, dan efisiensi CPU.
- [`topic-15-pruning-xai-image-classification.md`](topic-15-pruning-xai-image-classification.md): benchmark structured pruning untuk klasifikasi citra dengan audit explanation drift, faithfulness, localization, dan efisiensi deployment.
- [`archive/`](archive/README.md): kandidat di luar shortlist dan snapshot katalog lama.

Shortlist aktif saat ini terdiri atas Topik 01, Topik 02, Topik 14, dan Topik 15. Topik 14 adalah kandidat nomor 10 dalam ringkasan percakapan, tetapi nomor canonical-nya tetap dipertahankan agar riwayat berkas tidak terputus.

## Selera dan preferensi pengguna yang perlu diingat

Bagian ini adalah memori kerja lintas sesi, bukan klaim akademik.

- Minat utama berada di AI engineering, software engineering, coding agent, Computer Vision, dan Explainable AI (XAI). Arah terbaru yang paling menarik adalah coding agent dan masalah yang muncul dari kerja agent secara iteratif.
- Lebih menyukai penelitian computational yang dapat diuji dengan benchmark, eksperimen terkontrol, log, test suite, atau metrik kuantitatif. Human study sebaiknya dihindari jika tidak wajib; jika diperlukan, gunakan skala kecil dan jelaskan kebutuhan etiknya.
- Menyukai produk/prototipe yang nyata untuk format Skripsi Inovasi Produk: benchmark harness, toolkit, website audit, pipeline reproducible, atau middleware yang dapat dipakai ulang.
- Tetap mengutamakan kejujuran akademik. Jangan menjual wrapper library, dashboard generik, atau klaim “pertama” sebagai novelty jika literatur sudah memiliki solusi serupa.
- Suka scope yang sempit, terukur, dapat selesai sekitar satu semester, memakai data/infrastruktur yang tersedia, dan memiliki fallback plan.
- Untuk eksperimen coding agent, konfigurasi ideal adalah satu agent, environment dan tools yang sama, task yang sama, serta model/LLM family yang dibatasi. Satu LLM family dapat diterima jika pertanyaan riset memang mengenai kebijakan agent, bukan perbandingan model.
- Judul sebaiknya tidak mengunci teknik terlalu dini. Gunakan framing seperti “studi empiris” atau “evaluasi” bila teknik terbaik baru akan ditemukan lewat eksperimen.
- Catatan dan draft harus berbahasa Indonesia. Istilah teknis boleh tetap dalam bahasa Inggris pada penyebutan pertama; judul English hanya disediakan sebagai pasangan judul formal.
- Pengguna menghargai penjelasan sederhana, tetapi tidak ingin scope dibuat dangkal. Setiap ide harus memuat masalah, produk, novelty, metrik, risiko, dan fallback.
- Jangan menyarankan multi-modal atau multi-framework tanpa batasan format yang sangat jelas. Integrasi luas biasanya menjadi scope creep.

## Aturan kerja eksplorasi

1. Mulai dari masalah dan bentuk evaluasi, bukan dari nama model atau library.
2. Verifikasi novelty sebelum menyebut topik “baru”. Catat pembanding yang menggugurkan klaim lama.
3. Pisahkan novelty algoritmik, novelty produk, dan novelty protokol evaluasi.
4. Untuk setiap kandidat, tuliskan batasan, metrik, kebutuhan data/infrastruktur, risiko, dan fallback.
5. Bedakan ide yang disukai dari ide yang sudah dipilih. Status “tersimpan” bukan berarti “diterima”.
6. Jika ide dikeluarkan dari shortlist, pindahkan berkas detailnya ke `archive/` dan simpan alasan atau statusnya agar tidak dieksplorasi ulang tanpa pertimbangan baru.
7. Bila topik dipilih, tandai `✅ TERPILIH` di katalog sebelum mulai menulis LaTeX.

## Keputusan yang sudah mengikat

- IndoAgentBench bukan klaim pertama tentang pengaruh bahasa natural pada coding agent. Ren et al. sudah menjadi pembanding untuk efek bahasa Cina. Posisi yang aman adalah ekstensi terkontrol ke Bahasa Indonesia, kondisi translate-then-act, audit ekuivalensi bilingual, failure taxonomy, dan transformasi task anti-kontaminasi.
- Catatan keputusan yang hanya berlaku untuk kandidat di luar shortlist berada di [`archive/`](archive/README.md).

## Prosedur pembaruan

- Tambahkan kandidat baru sebagai baris baru di `topic-catalog.md`; buat file detail hanya jika kandidat melewati scan awal.
- Perbarui file detail yang ada jika eksplorasi adalah kelanjutan topik yang sama. Jangan membuat `topic-XX-v2`, file tanggalan, atau snapshot duplikat.
- Setelah pencarian literatur, masukkan sumber dan konsekuensi novelty langsung ke file detail dan katalog.
- Sebelum menghapus catatan, pastikan masalah, judul, novelty, pembanding, metrik, keputusan, risiko, dan pertanyaan terbuka sudah terserap ke canonical files.
