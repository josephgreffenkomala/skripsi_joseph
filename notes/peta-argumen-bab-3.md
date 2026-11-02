# Peta Argumen Bab 3 — Metode dan Rancangan Penelitian

**Acuan:** [Dokumen Induk Penelitian](dokumen-induk-penelitian.md), terutama bagian 5–9.

**Tujuan bab:** menjelaskan bagaimana eksperimen akan menjawab rumusan masalah, mulai dari persiapan data hingga analisis kualitas dan waktu inferensi.

## Alur besar Bab 3

```text
Tetapkan rancangan perbandingan dan variabel
        ↓
Susun tahapan penelitian dan indikator capaiannya
        ↓
Siapkan model, data, dan prompt
        ↓
Implementasikan routing → latih router dan LoRA
        ↓
Pilih konfigurasi dengan data validasi → evaluasi akhir pada data uji
        ↓
Analisis perubahan kualitas dan waktu inferensi
```

## Urutan argumen per subbab

### 3.1 Deskripsi Umum dan Rancangan Eksperimen

1. **Jenis penelitian:** eksperimen komputasional komparatif pada Qwen3-0.6B untuk peringkasan XL-Sum bahasa Indonesia.
2. **Hubungan dengan rumusan masalah:** pengaruh routing dinilai melalui kualitas ringkasan dan waktu inferensi; perbandingan strategi serta kontrol tanpa LoRA menjawab pertanyaan tentang trade-off dan perubahan terkait LoRA.
3. **Kelompok eksperimen:** sajikan tabel model penuh + LoRA, pelompatan statis + LoRA, routing adaptif + LoRA, dan routing adaptif tanpa LoRA. Jelaskan fungsi masing-masing sebagai pembanding atau kontrol.
4. **Variabel:** strategi eksekusi lapisan dan penggunaan LoRA sebagai perlakuan; kualitas dan waktu sebagai keluaran. Samakan model dasar, data uji, prompt, pengaturan generasi, perangkat, serta presisi numerik.

### 3.2 Tahapan Penelitian

1. **Urutan kerja:** penyusunan protokol → persiapan data dan model → implementasi dan pemeriksaan → pelatihan → pemilihan konfigurasi dengan validasi → evaluasi akhir → analisis.
2. **Bagan alir:** tampilkan urutan tersebut dan bedakan kegiatan yang sudah dilakukan dengan yang direncanakan berdasarkan status yang tercatat.
3. **Indikator capaian:** kaitkan setiap tahap dengan keluaran yang dapat diperiksa, seperti jumlah data setelah penyaringan, implementasi yang lolos pemeriksaan, router dan adapter terlatih, konfigurasi terpilih, serta skor dan waktu setiap metode.

### 3.3 Model, Data, dan Persiapan Masukan

1. **Model dan pembagian data:** gunakan Qwen3-0.6B dengan 28 lapisan serta subset dari split resmi XL-Sum Indonesia: 1.000 train, 200 validation, dan 500 test setelah penyaringan. Data uji hanya untuk evaluasi akhir. Pilot 50 artikel dari train digunakan untuk estimasi kebutuhan komputasi.
2. **Alur pengolahan:** pembersihan tepi teks dan penghapusan pasangan kosong → deduplikasi → penyaringan panjang → sampling tanpa pengembalian. Deduplikasi antar-split memprioritaskan test, validation, lalu train; sampling menggunakan seed 42. Catat jumlah dan identitas data yang tersaring atau dipilih.
3. **Prompt dan panjang:** gunakan instruksi dari dokumen induk dengan format chat non-thinking. Prompt lengkap maksimal 3.840 token dan target maksimal 256 token, dalam konteks gabungan 4.096 token. Artikel dan target yang melampaui batas dikeluarkan, tanpa pemotongan.

### 3.4 Perancangan Routing dan Pelatihan

1. **Arsitektur inferensi:** sertakan diagram tujuh kelompok × empat lapisan; G1 dan G7 selalu aktif. Rata-rata representasi token artikel setelah G1 menjadi fitur router, dengan instruksi, token khusus, dan padding dikecualikan. Router menghasilkan lima keputusan biner bagi G2–G6; route tetap selama sisa prefill dan seluruh decoding. Ringkasan acuan tidak tersedia saat inferensi.
2. **Pembentukan target:** jelaskan pencarian penghapusan satu kelompok secara bertahap dengan objective `J(m) = NLL(m) + λ C(m)`, dengan `C(m)` proporsi kelompok tengah aktif. Target berupa lima bit route akhir; pencarian lokal tidak menjamin optimum seluruh 32 route.
3. **Pelatihan dua tahap:** bekukan model utama dan latih router untuk memprediksi target, lalu bekukan router dan latih LoRA pada attention serta FFN. Rujuk konfigurasi yang sudah ditetapkan dalam dokumen induk; jelaskan kebutuhan konsistensi fitur router ketika LoRA memperbarui G1.
4. **Pemilihan konfigurasi:** gunakan data validasi untuk memilih λ dan route statis. LoRA dilatih terpisah pada ketiga pendekatan utama; kontrol adaptif menggunakan router tanpa LoRA. Tetapkan seluruh pilihan sebelum evaluasi akhir.

### 3.5 Protokol Evaluasi

1. **Pemeriksaan implementasi:** pastikan route penuh setara dengan model penuh, kelompok yang dilewati tidak dieksekusi, route tetap selama generasi, dan KV cache konsisten.
2. **Generasi yang sebanding:** gunakan greedy decoding, mode non-thinking, batch size 1, dan batas keluaran 256 token. Generasi berhenti pada token akhir respons atau batas keluaran; token akhir termasuk dalam batas.
3. **Kualitas:** hitung F1 ROUGE-1, ROUGE-2, ROUGE-L, dan BERTScore per artikel, kemudian rata-ratakan dengan bobot sama dan laporkan terpisah. Penilaian manual berada di luar lingkup.
4. **Waktu:** ukur waktu total, termasuk representasi artikel dan router; catat prefill dan decoding terpisah. Gunakan warm-up dan pengulangan pada kondisi sama. Catat panjang keluaran, lapisan aktif, serta frekuensi route sebagai informasi pendukung.

### 3.6 Rencana Analisis dan Keluaran yang Diharapkan

1. **Perbandingan kualitas:** bandingkan adaptif + LoRA dengan setiap pembanding menggunakan selisih rata-rata F1 berpasangan dan interval kepercayaan 95% melalui paired bootstrap 10.000 ulangan, seed 42. Interval menggambarkan variasi antarartikel.
2. **Perbandingan efisiensi:** baca waktu total bersama waktu prefill, decoding, dan panjang keluaran. Gunakan jumlah lapisan aktif serta distribusi route untuk menjelaskan pola pemakaian komputasi.
3. **Jawaban penelitian:** sajikan profil kualitas–waktu keempat kelompok untuk menilai trade-off dan perubahan ketika LoRA digunakan. Keluaran yang diharapkan adalah bukti empiris dan batas penerapan; arah keunggulan tidak ditentukan sebelumnya.

## Hal yang Masih Perlu Ditetapkan

- Arsitektur dan aturan keputusan router; konsistensi fiturnya setelah adaptasi G1; konfigurasi dan objective LoRA.
- Kriteria pemilihan λ serta agregasi skor pemilihan route statis; implementasi ROUGE dan konfigurasi BERTScore.
- Perangkat, presisi, versi model dan perangkat lunak, jumlah warm-up/pengulangan, serta statistik ringkasan waktu.

Gunakan status keputusan pada dokumen induk. Konfigurasi implementasi yang belum disahkan dan hasil run yang belum dipastikan statusnya tidak dijadikan keputusan atau hasil final penelitian.
