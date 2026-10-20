# Peta Argumen Bab 1

*Disusun dari dokumen induk penelitian sebagai alur awal penulisan, bukan naskah final.*

## Alur argumen

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

## Isi pokok tiap langkah

1. **Konteks:** model kausal menghasilkan ringkasan secara autoregresif, sehingga komputasi lapisan berulang selama generasi.
2. **Tantangan:** melewati lapisan mungkin mengurangi komputasi, tetapi dampaknya terhadap kualitas tidak boleh diasumsikan; overhead router juga dapat memengaruhi waktu.
3. **Fokus:** satu route dipilih untuk setiap artikel (*sequence-level routing*) dan dipertahankan selama pemrosesan prompt serta generasi.
4. **Kebutuhan evaluasi:** ukur kualitas ringkasan dan waktu aktual, termasuk overhead router, bukan hanya jumlah lapisan aktif.
5. **Ruang penelitian:** Qwen3-0.6B, XL-Sum bahasa Indonesia, dan perbandingan strategi penuh, statis, serta adaptif; routing adaptif juga dikaji dengan dan tanpa LoRA.
6. **Arah Bab 1:** tutup latar belakang dengan dua rumusan masalah dari dokumen induk, lalu turunkan tujuan, batasan penelitian, dan manfaatnya. Jangan menyatakan sejak awal bahwa routing atau LoRA pasti lebih unggul.
