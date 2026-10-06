# TODO

Pembaruan: 6 Oktober 2026. Fokus pekerjaan adalah penyelesaian penelitian dan
penulisan skripsi. Tidak ada tahap pilot terpisah; pemeriksaan kebenaran kode,
baseline, dan evaluasi kualitas–efisiensi menjadi bagian eksperimen utama.

## Progres yang sudah ada

- [x] Mengunci arah topik: sequence-level routing / input-adaptive layer skipping pada decoder-only SLM.
- [x] Menetapkan mekanisme umum: router ringan membaca representasi prompt/sequence dan memilih layer atau kelompok layer yang tetap digunakan selama decoding.
- [x] Menyiapkan script inference Qwen3-0.6B, mode offline, dan progress token; keberhasilan inference dasar tercatat di `experiment/README.md`.
- [x] Mengumpulkan rujukan awal dan bahan belajar tentang sequence-level routing; sintesis literatur dan posisi kontribusi belum selesai.

## 1. Tetapkan cakupan penelitian

- [x] Tetapkan Qwen3-0.6B (`Qwen/Qwen3-0.6B`) dan XL-Sum subset Indonesia (`csebuetnlp/xlsum`, konfigurasi `indonesian`) untuk peringkasan berita bahasa Indonesia; disetujui pada 6 Oktober 2026.
- [x] Sepakati dua pertanyaan penelitian tentang kualitas–waktu inferensi dan perbandingan routing adaptif dengan static/random skipping dengan mempertimbangkan kualitas dan biaya inferensi.
- [x] Sepakati pemilihan satu pola kelompok layer per prompt, pelatihan awal hanya router dengan Qwen dibekukan, serta pembanding full model, static skipping, dan random routing.
- [ ] Tetapkan rincian batasan penelitian dan judul final.
- [ ] Sintesiskan penelitian terkait, terutama FiRST dan PuDDing, lalu rumuskan posisi penelitian yang dapat dipertanggungjawabkan.
- [ ] Tetapkan target, fungsi loss, mekanisme pembelajaran keputusan biner, dorongan penghematan, dan ambang router; grouping, representasi setelah kelompok pertama, dan MLP lima output sigmoid telah disepakati.
- [ ] Tetapkan perangkat komputasi serta batas waktu dan biaya eksperimen; LoRA hanya dipertimbangkan melalui keputusan berikutnya jika diperlukan.
- [ ] Tetapkan metrik kualitas dan efisiensi, protokol pengukuran, serta kriteria untuk menilai trade-off; jangan mengasumsikan speedup atau kualitas akan membaik.

## 2. Tulis proposal sambil membangun implementasi

Status draf 6 Oktober 2026: `latex/proposal/` sudah memuat draf Bab 1,
kajian awal Bab 2, rancangan umum dan dua diagram Bab 3, serta intisari dan
abstract. Referensi awal sudah ditambahkan. Checklist di bawah tetap terbuka
untuk pelengkapan dan finalisasi; judul, metadata, rincian metode, dan jadwal
belum selesai.

- [ ] Isi Bab 1: latar belakang, rumusan masalah, batasan, tujuan, dan manfaat.
- [ ] Isi Bab 2: sintesis penelitian terkait dan posisi penelitian.
- [ ] Isi Bab 3: rancangan metode, diagram arsitektur, bagan alir, dan desain evaluasi.
- [ ] Isi Bab 4: jadwal penyelesaian yang sesuai sumber daya tersedia.
- [ ] Lengkapi metadata, intisari/abstract, dan referensi; periksa sitasi dan kompilasi sesuai pedoman UGM.

## 3. Implementasi dan eksperimen utama

- [ ] Siapkan dataset beserta split train/validation/test, preprocessing, dan konfigurasi yang dapat direproduksi.
- [ ] Implementasikan full model, static layer skipping, random routing, dan router terlatih sesuai rancangan pembanding yang disepakati.
- [ ] Implementasikan eksekusi layer kondisional dan konsistensi route selama decoding, termasuk penanganan KV cache.
- [ ] Periksa bahwa konfigurasi semua layer aktif sesuai dengan full model dan layer yang dilewati benar-benar tidak dieksekusi.
- [ ] Bentuk target route dan latih router menggunakan data train; gunakan validation untuk pemilihan konfigurasi dan test hanya untuk evaluasi akhir.
- [ ] Tetapkan protokol biaya pembanding dan bandingkan kualitas–efisiensi metode skipping tanpa budget layer tetap, dengan full model sebagai acuan kualitas dan biaya penuh.
- [ ] Ukur kualitas keluaran dan latency aktual termasuk overhead router; kendalikan perangkat, panjang input/output, batch size, warm-up, dan pengulangan pengukuran.
- [ ] Analisis pola route, kemungkinan routing collapse, dan trade-off kualitas–efisiensi; simpan konfigurasi serta hasil mentah.

## 4. Selesaikan skripsi

- [ ] Susun naskah dengan struktur skripsi ilmiah akademik enam bab sesuai `AGENTS.md`.
- [ ] Tulis implementasi, hasil, pembahasan, keterbatasan, kesimpulan, dan saran berdasarkan temuan eksperimen.
- [ ] Lengkapi tabel/gambar, daftar pustaka, serta lampiran kode dan konfigurasi.
- [ ] Periksa konsistensi naskah, format UGM, kompilasi, dan revisi bersama dosen pembimbing.

## Model dan dataset yang sudah dikunci

- **Backbone utama:** Qwen3-0.6B (`Qwen/Qwen3-0.6B`).
- **Dataset dan tugas utama:** XL-Sum (`csebuetnlp/xlsum`), konfigurasi `indonesian`, untuk peringkasan berita bahasa Indonesia.
- Kedua pilihan disetujui pada 6 Oktober 2026. Kualitas ringkasan dan penghematan komputasi setelah skipping tetap harus diukur.

## Rancangan dan pertanyaan penelitian yang disepakati

Disepakati pada 6 Oktober 2026:

- Satu router MLP dengan satu hidden layer dan lima output sigmoid menghasilkan keputusan biner untuk lima kelompok tengah. Sebanyak 28 layer dibagi menjadi tujuh kelompok berisi empat layer; kelompok pertama dan terakhir selalu aktif. Keputusan dibuat sekali per prompt dan dipertahankan pada sisa prefill serta seluruh decoding. Budget tetap 24/20 layer dan dua router terpisah dihapus.
- Rancangan awal melatih router saja dengan bobot Qwen dibekukan. LoRA belum termasuk rancangan awal.
- Pembanding adalah full model, static layer skipping, dan random routing. Protokol penyetaraan biaya antarmetode skipping masih perlu ditetapkan setelah penghapusan budget tetap, sedangkan full model menjadi acuan kualitas dan biaya penuh.

Pertanyaan penelitian:

1. Bagaimana pengaruh sequence-level routing terhadap kualitas ringkasan dan waktu inferensi Qwen3-0.6B pada XL-Sum Indonesia?
2. Apakah router terlatih memberikan trade-off kualitas–efisiensi yang lebih baik daripada static dan random skipping dengan mempertimbangkan kualitas dan biaya inferensi?

## Rincian yang masih berupa usulan

- **Usulan decoding:** mode non-thinking; konfigurasi generasi, batas panjang, preprocessing, dan jumlah sampel belum dikunci.
- **Pelatihan router setelah revisi:** target dan fungsi loss keputusan biner, mekanisme pembelajarannya, dorongan penghematan, ambang, ukuran hidden layer, aktivasi hidden layer, dan hiperparameter belum ditetapkan. Label offline dan penalti biaya merupakan opsi; tidak ada kewajiban enumerasi 32 pola. Representasi tetap rata-rata hidden state token artikel setelah kelompok pertama.
- **Usulan metrik:** ROUGE untuk kualitas ringkasan, dilengkapi pemeriksaan faktualitas pada sampel; latency end-to-end, waktu per token decoding, dan jumlah layer aktif untuk efisiensi. Jumlah layer aktif tidak boleh dilaporkan sebagai pengukuran FLOPs atau bukti speedup.

Sumber: [Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B),
[XL-Sum](https://huggingface.co/datasets/csebuetnlp/xlsum), dan
[PuDDing](https://proceedings.mlr.press/v267/wee25a.html).

## Ide terdahulu yang diparkir

- Ide menghubungkan setiap layer ke layer akhir dan berhenti ketika confidence tinggi disimpan sebagai ide eksplorasi early exit. Hubungan dan mekanismenya belum dirancang; ide ini bukan scope sequence-level routing yang sudah dikunci.
- Arah lama perbandingan pruning untuk sentimen Indonesia tidak lagi diperlakukan sebagai topik final.
- Qwen3-1.7B, IndoSum, dan SmSA merupakan alternatif terdahulu yang tidak dipilih sebagai model/dataset utama.
