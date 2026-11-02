# Peta Argumen Bab 2 — Penelitian Terkait

**Acuan:** [Dokumen Induk Penelitian](dokumen-induk-penelitian.md), terutama bagian 3–7.

**Tujuan bab:** menjelaskan pendekatan yang sudah dikaji, batas relevansinya, dan posisi penelitian ini. FiRST dan PuDDing menjadi pembahasan utama.

## Alur besar Bab 2

```text
Pengurangan kedalaman dan komputasi adaptif pada Transformer
        ↓
Routing berbasis masukan sebagai pendekatan yang paling dekat
        ↓
Konteks penerapan: peringkasan berita Indonesia
        ↓
Dasar evaluasi kualitas ringkasan dan efisiensi inferensi
        ↓
Sintesis penelitian terdahulu → posisi penelitian ini
```

## Urutan argumen per subbab

### 2.1 Pengurangan Kedalaman dan Komputasi Adaptif

1. **Dasar pengurangan kedalaman:** gunakan LayerDrop (Fan et al., 2020) untuk menjelaskan bahwa pelatihan dengan penghilangan lapisan memungkinkan penggunaan Transformer pada kedalaman berbeda.
2. **Perbedaan unit keputusan:** DeeBERT (Xin et al., 2020) memberi konteks penghentian pada lapisan tertentu (*early exit*) di BERT; CALM (Schuster et al., 2022) membahas komputasi adaptif pada tingkat token. Hubungkan dengan pilihan penelitian ini untuk menetapkan satu route per artikel.
3. **Konteks generasi autoregresif:** singgung LayerSkip (Elhoushi et al., 2024) sebagai pendekatan early exit dengan pelatihan khusus dan *self-speculative decoding*. Gunakan FFN-SkipLLM (Jaiswal et al., 2024) untuk mengenalkan isu skipping dan pengelolaan cache selama generasi.

### 2.2 Routing Berbasis Masukan dan Adaptasi Model

1. **FiRST (Jain et al., 2025):** bahas routing adaptif pada tahap pemrosesan masukan (*prefill*) dan pelatihan dua tahap: router dilatih saat model utama dibekukan, lalu LoRA dilatih saat router dibekukan. Ini menjadi landasan pola pelatihan penelitian.
2. **PuDDing (Wee et al., 2025):** bahas router yang memilih himpunan lapisan untuk dilewati berdasarkan prompt dari opsi yang dibentuk berbasis data. Jelaskan konteks pengujiannya pada penalaran akal sehat.
3. **Hubungkan ke rancangan penelitian:** penelitian ini mengkaji satu keputusan route per artikel melalui lima keputusan biner kelompok lapisan tengah, dengan jalur tetap selama sisa prefill dan generasi. Bedakan mekanisme ini dari pemilihan himpunan kandidat pada PuDDing.

### 2.3 Peringkasan Berita Bahasa Indonesia

1. **Tugas dan data:** gunakan XL-Sum (Hasan et al., 2021) untuk menjelaskan peringkasan abstraktif serta ketersediaan pasangan artikel berita dan ringkasan acuan bahasa Indonesia.
2. **Model dalam lingkup kajian:** perkenalkan Qwen3-0.6B secara singkat berdasarkan kartu model: model bahasa kausal sekitar 0,6 miliar parameter dengan 28 lapisan.
3. **Hubungan dengan penelitian terkait:** jelaskan bahwa mekanisme routing berbasis masukan akan dikaji dalam konteks tugas dan model tersebut. Bukti pada tugas penalaran yang dibahas sebelumnya belum menjadi bukti efektivitas pada konteks ini.

### 2.4 Evaluasi Kualitas Ringkasan dan Efisiensi Inferensi

1. **Dasar metrik:** ROUGE (Lin, 2004) mengukur kesamaan kata dan urutan; BERTScore (Zhang et al., 2020) mengukur kemiripan representasi kontekstual. Keduanya mendasari penggunaan beberapa metrik yang dilaporkan terpisah.
2. **Batas metrik:** gunakan Forde et al. (2024) untuk menjelaskan keterbatasan metrik otomatis pada peringkasan multibahasa, termasuk Indonesia. Skor kesamaan terhadap acuan tidak membuktikan faktualitas atau kualitas menyeluruh.
3. **Dasar penilaian efisiensi:** hubungkan kajian routing dengan kebutuhan mengukur waktu inferensi aktual, termasuk biaya router. Jumlah lapisan aktif menjadi informasi pendukung untuk membaca perubahan kualitas dan waktu.

### 2.5 Sintesis dan Posisi Penelitian

1. **Capaian yang menjadi landasan:** penelitian terdahulu telah mengkaji pengurangan kedalaman, komputasi adaptif, dan routing berbasis masukan; FiRST memberi preseden pelatihan router dan LoRA dua tahap.
2. **Ruang kajian yang dituju:** penelitian ini memusatkan penerapan pada sequence-level routing kelompok lapisan Qwen3-0.6B untuk peringkasan XL-Sum Indonesia. Nyatakan posisi berdasarkan perbedaan mekanisme, model, dan tugas yang telah dibahas, tanpa mengklaim sebagai penerapan pertama.
3. **Kontribusi yang akan diuji:** perbandingan model penuh + LoRA, pelompatan statis + LoRA, dan routing adaptif + LoRA, disertai kontrol adaptif tanpa LoRA; kualitas ringkasan dan waktu aktual menjadi dasar analisis.

Tutup dengan pengantar ke Bab 3 untuk detail rancangan, pelatihan, dan evaluasi.

## Batas penulisan

- Susun pembahasan penelitian utama sebagai **pendekatan → capaian → batas relevansi → hubungan dengan penelitian ini**.
- Gunakan capaian yang tercatat dalam dokumen induk; angka hasil penelitian terdahulu belum dirangkum di sana. Detail implementasi ditempatkan di Bab 3.
