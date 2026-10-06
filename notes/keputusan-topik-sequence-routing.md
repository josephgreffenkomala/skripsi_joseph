# Keputusan Topik: Sequence-Level Routing pada Decoder-only SLM

**Status:** arah topik dikunci pada 25 September 2026.

## Arah penelitian yang dikunci

Penelitian akan membahas **sequence-level routing** atau **input-adaptive layer skipping** pada decoder-only small language model (SLM). Sebuah router ringan membaca representasi prompt atau sequence, kemudian menentukan layer atau kelompok layer yang perlu dijalankan. Jalur yang dipilih digunakan secara konsisten selama decoding sehingga setiap input dapat memperoleh jumlah komputasi yang berbeda tanpa menerapkan keputusan routing pada setiap token.

Sistem yang diteliti bukan sekadar konfigurasi library. Penelitian memerlukan intervensi pada alur forward model berupa:

1. penambahan router ringan, misalnya MLP;
2. pembentukan kandidat layer atau kelompok layer yang dapat dilewati;
3. mekanisme keputusan `execute`/`skip`;
4. pelatihan router menggunakan target jalur hasil pencarian offline atau objective gabungan kualitas dan biaya komputasi;
5. modifikasi inference agar hanya layer terpilih yang dijalankan; dan
6. evaluasi apakah pengurangan komputasi benar-benar menghasilkan percepatan wall-clock tanpa penurunan kualitas yang berlebihan.

Backbone pretrained dapat tetap dibekukan. Komponen yang dilatih dapat dibatasi pada router, atau router bersama adapter seperti LoRA jika diperlukan untuk memulihkan kualitas setelah layer skipping.

## Posisi penelitian sementara

Kontribusi tidak akan hanya berupa pemasangan MLP router karena gagasan dasar tersebut telah muncul pada penelitian seperti FiRST, PuDDing, dan Dr.LLM. Posisi penelitian perlu diperjelas melalui satu atau beberapa aspek berikut:

- penerapan pada decoder-only SLM dan lingkungan komputasi terbatas;
- grouped-layer routing untuk menekan overhead router;
- evaluasi pada tugas atau domain yang belum banyak dikaji, dengan peringkasan bahasa Indonesia sebagai kandidat;
- perbandingan adil terhadap full model, static skipping, dan random routing pada budget komputasi yang sama;
- pengukuran FLOPs, jumlah layer aktif, penggunaan memori, dan wall-clock latency; serta
- analisis apakah keputusan router benar-benar berbeda antarinput dan tidak mengalami routing collapse.

## Rancangan awal yang masih berupa kandidat

Rancangan paling terkendali adalah mempertahankan layer awal dan akhir, kemudian membagi middle layers menjadi beberapa kelompok. Router memilih pola kelompok aktif berdasarkan representasi prompt. Ruang pilihan dapat dibatasi menjadi beberapa kandidat route agar pelatihan dan evaluasi lebih stabil daripada menggunakan satu binary gate untuk setiap layer.

Rancangan ini **belum mengunci** backbone, dataset, bahasa/domain tugas, jumlah kelompok layer, arsitektur router, metode supervision, penggunaan LoRA, metrik, perangkat keras, atau klaim kontribusi final.

## Pertanyaan penelitian kandidat

1. Apakah sequence-level routing dapat mengurangi komputasi dan wall-clock latency decoder-only SLM dengan penurunan kualitas yang masih dapat diterima?
2. Apakah router terlatih menghasilkan trade-off kualitas–efisiensi yang lebih baik daripada static dan random layer skipping pada budget komputasi yang sama?
3. Seberapa adaptif dan stabil pola layer yang dipilih router terhadap variasi karakteristik input?

## Paragraf singkat untuk dosen pembimbing

Saya berencana mengambil topik efisiensi inferensi decoder-only small language model menggunakan **sequence-level routing**. Pada pendekatan ini, saya akan menambahkan router ringan yang membaca representasi prompt untuk menentukan kelompok layer yang perlu dijalankan selama decoding, sehingga input yang berbeda dapat menggunakan jumlah komputasi yang berbeda. Penelitian akan membandingkan metode tersebut dengan full model dan static layer skipping pada budget komputasi yang sama, kemudian mengevaluasi trade-off kualitas keluaran, FLOPs, penggunaan memori, dan wall-clock latency. Model, dataset, serta domain tugas final masih akan saya tentukan setelah kajian literatur dan eksperimen awal.

## Langkah berikutnya

- Menentukan domain tugas dan dataset.
- Memilih kandidat decoder-only SLM.
- Mereproduksi baseline full model dan static layer skipping.
- Menentukan strategi grouping layer dan pembentukan target route.
- Menyusun eksperimen awal untuk menguji kelayakan latency dan kualitas.
