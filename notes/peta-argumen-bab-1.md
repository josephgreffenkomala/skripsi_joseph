# Peta Argumen Bab 1

*Disusun dari dokumen induk penelitian sebagai alur awal penulisan, bukan naskah final.*

## Alur besar Bab 1

```text
Peringkasan autoregresif menjalankan komputasi Transformer berulang
        ↓
Pelompatan lapisan berpotensi mengurangi komputasi,
tetapi dapat memengaruhi kualitas ringkasan
        ↓
Routing adaptif memilih jalur lapisan berdasarkan artikel;
router sendiri menambah overhead
        ↓
Jumlah lapisan yang dilewati belum cukup untuk menyimpulkan percepatan:
kualitas dan waktu inferensi aktual perlu diukur bersama
        ↓
Penelitian menguji sequence-level routing pada Qwen3-0.6B
untuk peringkasan berita Indonesia dengan XL-Sum
        ↓
Hasil routing adaptif dibandingkan dengan model penuh dan
pelompatan statis; kontrol tanpa LoRA mengukur perubahan terkait LoRA
        ↓
Rumusan masalah, tujuan, batasan, dan manfaat penelitian
```

## Urutan argumen per subbab

### 1.1 Latar Belakang

Susun dari konteks umum menuju fokus penelitian:

1. Jelaskan bahwa model bahasa kausal membentuk ringkasan secara autoregresif dan menjalankan komputasi lapisan berulang selama generasi.
2. Kenalkan *layer skipping* sebagai cara potensial untuk mengurangi komputasi, dengan dua pola: statis (lapisan yang dilewati tetap) dan adaptif (jalur menyesuaikan artikel).
3. Paparkan trade-off: melewati lapisan dapat memengaruhi kualitas ringkasan, sedangkan router adaptif menambah overhead.
4. Tarik implikasi bahwa jumlah lapisan yang dilewati tidak cukup untuk menyatakan inferensi lebih cepat; kualitas dan waktu aktual perlu diukur bersama.
5. Perkenalkan fokus penelitian: *sequence-level routing*, yaitu satu route dipilih per artikel dan dipertahankan selama sisa pemrosesan prompt serta generasi.
6. Batasi konteks studi pada Qwen3-0.6B dan peringkasan berita bahasa Indonesia menggunakan XL-Sum.
7. Tutup dengan rancangan perbandingan: model penuh, *static skipping*, dan routing adaptif dengan LoRA, serta kontrol routing adaptif tanpa LoRA. Arahkan ke pertanyaan tentang pengaruh pada kualitas dan waktu serta trade-off antarmetode, tanpa mendahului hasil.

### 1.2 Rumusan Masalah

Nyatakan sebagai dua pertanyaan yang langsung mengikuti latar belakang:

1. Bagaimana pengaruh *sequence-level routing* terhadap kualitas ringkasan dan waktu inferensi Qwen3-0.6B pada XL-Sum Indonesia?
2. Apakah routing adaptif dengan LoRA memberi trade-off kualitas–efisiensi yang lebih baik daripada *static skipping* dan model penuh dengan LoRA, serta bagaimana hasil routing adaptif berubah tanpa LoRA?

### 1.3 Batasan Masalah

Jelaskan lingkup agar pembaca tahu apa yang dicakup dan apa yang tidak dinilai:

- Model dan tugas: Qwen3-0.6B untuk peringkasan berita bahasa Indonesia pada XL-Sum.
- Routing: keputusan satu kali per artikel pada lima kelompok lapisan tengah; kelompok pertama dan terakhir selalu aktif, dan route dipertahankan selama pemrosesan prompt serta generasi.
- Pembanding: model penuh + LoRA, *static skipping* + LoRA, routing adaptif + LoRA, serta routing adaptif tanpa LoRA.
- Evaluasi: ROUGE-1, ROUGE-2, ROUGE-L, dan BERTScore untuk kualitas; waktu inferensi aktual total sebagai ukuran efisiensi utama, dengan waktu *prefill* dan *decoding* dicatat terpisah.
- Batas interpretasi: penelitian tidak mengasumsikan metode tertentu unggul dan tidak melakukan penilaian manual atau pengukuran faktualitas secara manual.

### 1.4 Tujuan Penelitian

Pasangkan tujuan dengan rumusan masalah dalam urutan yang sama:

1. Menganalisis pengaruh *sequence-level routing* terhadap kualitas ringkasan dan waktu inferensi Qwen3-0.6B pada XL-Sum Indonesia.
2. Membandingkan trade-off kualitas–efisiensi routing adaptif + LoRA dengan *static skipping* + LoRA dan model penuh + LoRA, serta mengukur perubahan hasil routing adaptif melalui kontrol tanpa LoRA.

### 1.5 Manfaat Penelitian

Turunkan manfaat dari keluaran yang memang diukur, bukan dari hasil yang belum diketahui:

- **Manfaat akademis:** menyediakan hasil empiris tentang hubungan strategi pelompatan lapisan, kualitas ringkasan, dan waktu inferensi pada tugas serta model yang diteliti.
- **Manfaat metodologis:** memberi rancangan perbandingan yang mencakup metode penuh, statis, adaptif, dan kontrol tanpa LoRA, sambil menghitung overhead router dalam waktu inferensi.
- **Manfaat praktis:** menjadi bahan pertimbangan saat menilai apakah routing adaptif layak digunakan untuk efisiensi inferensi pada konteks eksperimen ini.

Manfaat tersebut berupa kontribusi dan bahan pertimbangan; jangan menuliskannya sebagai bukti bahwa routing pasti lebih cepat atau lebih baik.
