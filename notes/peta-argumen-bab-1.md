# Peta Argumen Bab 1

*Disusun dari dokumen induk penelitian sebagai alur awal penulisan, bukan naskah final.*

## Alur besar Bab 1

```text
Peringkasan berita bahasa Indonesia dengan model bahasa kausal
        ↓
Generasi autoregresif menjalankan komputasi lapisan berulang,
sehingga efisiensi inferensi menjadi fokus kajian
        ↓
Pelompatan lapisan sebagai pendekatan pengurangan komputasi:
pola statis dan routing adaptif
        ↓
Sequence-level routing memilih satu jalur lapisan per artikel
dan mempertahankannya selama generasi
        ↓
Fokus penelitian: Qwen3-0.6B dan XL-Sum bahasa Indonesia
        ↓
Rumusan masalah → batasan masalah → tujuan → manfaat penelitian
```

## Urutan argumen per subbab

### 1.1 Latar Belakang

Susun dari konteks umum menuju fokus penelitian:

1. **Konteks tugas:** awali dengan peringkasan berita bahasa Indonesia menggunakan model bahasa kausal.
2. **Masalah komputasi:** jelaskan bahwa ringkasan dibentuk secara autoregresif, sehingga komputasi lapisan berulang selama generasi. Hubungkan dengan kebutuhan efisiensi inferensi.
3. **Pendekatan yang relevan:** kenalkan *layer skipping* sebagai cara potensial mengurangi komputasi. Bedakan pola statis yang tetap untuk semua artikel dan routing adaptif yang menyesuaikan artikel.
4. **Fokus pendekatan:** perkenalkan *sequence-level routing*, yaitu pemilihan satu route per artikel yang dipertahankan selama sisa pemrosesan prompt dan generasi.
5. **Posisi penelitian:** gunakan FiRST dan PuDDing yang dirangkum dalam dokumen induk sebagai landasan pendekatan, lalu arahkan pada konteks yang dikaji: Qwen3-0.6B dan XL-Sum bahasa Indonesia.
6. **Penutup latar belakang:** nyatakan perlunya mengkaji penerapan routing tersebut pada konteks penelitian ini, lalu hubungkan dengan rumusan masalah.

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
