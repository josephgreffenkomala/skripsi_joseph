# Eksplorasi Topik Computer Vision x XAI

Tanggal: 2026-06-08
Target: proposal dan skripsi

## Ringkasan

Arah paling kuat untuk topik Computer Vision x Explainable AI (XAI) adalah membuat produk atau prototipe evaluasi yang tidak hanya menampilkan peta panas, tetapi juga mengukur apakah model visi komputer benar-benar memakai area atau konsep visual yang relevan dengan domain. Dengan kerangka Skripsi Inovasi Produk, produk yang dibuat dapat berupa dashboard atau pipeline evaluasi model yang menerima model dan citra, menghasilkan prediksi, penjelasan visual, skor keselarasan penjelasan, dan laporan potensi shortcut learning.

Setelah dibandingkan dengan Amara et al. (2024), rekomendasi utama perlu diperbaiki: topik penyakit tanaman masih layak, tetapi tidak boleh diformulasikan sebagai "penerapan ACE pada PlantVillage" karena itu sudah dikerjakan. Arah yang lebih kuat adalah membuat toolkit audit XAI untuk menguji shortcut learning dan stabilitas penjelasan model pada citra penyakit tanaman, terutama melalui uji gangguan latar belakang, cahaya, bayangan, mask daun, dan validasi konsep secara interaktif.

## Temuan

### Opsi 1: XAI untuk Deteksi Penyakit Tanaman

Calon judul:
Pengembangan Toolkit Audit Explainable AI untuk Evaluasi Shortcut Learning pada Model Klasifikasi Penyakit Tanaman Berbasis Citra

Alternatif judul:
Evaluasi Keselarasan Penjelasan Model Visi Komputer terhadap Gejala Visual Penyakit Tanaman Menggunakan Explainable AI

Ide produk:
Prototipe evaluasi XAI untuk model klasifikasi penyakit tanaman. Sistem melatih atau memuat model CNN/ViT ringan, menghasilkan Grad-CAM, Grad-CAM++, Score-CAM, atau ACE, lalu membuat laporan apakah penjelasan model selaras dengan gejala penyakit atau justru dipengaruhi latar belakang, pencahayaan, bayangan, dan artefak dataset.

Kebaruan yang masih masuk akal:
- Fokus pada toolkit audit dan evaluasi shortcut learning, bukan sekadar menerapkan XAI.
- Menyediakan pengujian kuantitatif melalui background swap, brightness/shadow perturbation, leaf-only mask, dan background-only control.
- Membandingkan beberapa metode XAI dengan protokol evaluasi yang sama.
- Menyediakan human-in-the-loop untuk memberi label konsep sebagai gejala, struktur daun, latar belakang, bayangan, atau artefak.
- Menghasilkan laporan audit yang dapat dipakai untuk memperbaiki dataset atau model.

Kelayakan:
- Dataset dasar mudah: PlantVillage tersedia di TensorFlow Datasets dengan 54.303 gambar dan 38 kategori.
- Dapat dibatasi ke 3-5 penyakit pada satu tanaman, misalnya tomat atau kentang, agar skripsi S1 tetap tajam.
- Tidak membutuhkan ahli medis; validasi konsep visual dapat dilakukan dari literatur agronomi, inspeksi dataset, dan evaluasi manual terbatas.
- Produk dapat dibuat sebagai aplikasi web sederhana, notebook pipeline, atau toolkit Python.

Risiko:
- Jika hanya memakai PlantVillage + InceptionV3 + ACE, topik terlalu dekat dengan Amara et al. (2024).
- PlantVillage memiliki latar yang relatif bersih sehingga perlu uji perturbasi atau citra lapangan agar isu shortcut lebih terlihat.
- Segmentasi gejala otomatis bisa menjadi rumit; solusi aman adalah memakai proxy seperti mask daun, rasio fokus latar belakang, dan evaluasi manual terbatas.

### Opsi 2: XAI untuk Screening TBC dari Chest X-Ray

Calon judul:
Evaluasi Keselarasan Penjelasan Model Visi Komputer dengan Area Paru pada Deteksi Tuberkulosis Berbasis Chest X-Ray

Ide produk:
Pipeline evaluasi model CXR yang melakukan klasifikasi normal/TB, menghasilkan peta panas XAI, lalu menghitung apakah peta panas berada di area paru, bukan marker, border, teks, atau artefak luar paru. Produk dapat berupa notebook reproducible atau dashboard sederhana dengan laporan prediksi, peta panas, mask paru, dan skor keselarasan.

Kebaruan:
- Membawa isu shortcut learning ke kasus kesehatan yang penting.
- Evaluasi XAI dibuat kuantitatif dengan lung-region alignment, bukan hanya visual subjektif.
- Dapat membandingkan beberapa model CNN, misalnya ResNet, DenseNet, dan EfficientNet.

Kelayakan:
- Dataset publik tersedia: Montgomery County dan Shenzhen TB CXR dari NLM/NIH; TBX11K juga dapat dipertimbangkan.
- Produk minimal dapat memakai segmentasi paru sederhana atau anotasi ROI terbatas.

Risiko:
- Klaim medis harus sangat hati-hati; produk tidak boleh diposisikan sebagai alat diagnosis klinis.
- Validasi keselarasan radiologis idealnya membutuhkan dokter/radiolog. Tanpa itu, klaim harus dibatasi pada keselarasan ke area paru dan deteksi artefak luar paru.

### Opsi 3: XAI untuk Deteksi Kerusakan Jalan

Calon judul:
Prototipe Explainable Road Damage Detection untuk Mengidentifikasi Shortcut Visual pada Citra Jalan

Ide produk:
Aplikasi deteksi pothole/crack berbasis YOLO atau segmentasi ringan yang menampilkan bounding box dan peta penjelasan. Sistem mengevaluasi apakah penjelasan model tumpang tindih dengan area kerusakan, atau salah fokus ke bayangan, marka jalan, genangan, kendaraan, dan tekstur aspal.

Kebaruan:
- Menggeser deteksi kerusakan jalan dari sekadar mAP menuju auditability dan analisis false positive.
- Relevan untuk smart city dan pemeliharaan infrastruktur.
- Dapat dibuat sebagai demo web dengan upload gambar atau video pendek.

Kelayakan:
- RDD2022 memiliki 47.420 citra dari enam negara.
- Dataset baru berbasis UAV juga tersedia, tetapi perlu pemeriksaan lisensi dan kualitas anotasi.

Risiko:
- XAI untuk object detection lebih rumit daripada klasifikasi.
- Perlu desain metrik yang jelas, misalnya IoU peta penjelasan dengan bounding box/mask, kategori false positive, dan robustness terhadap kondisi cahaya.

### Opsi Tambahan: XAI untuk Deteksi Kualitas Makanan atau Buah

Calon judul:
Explainable AI untuk Klasifikasi Kualitas Buah Berbasis Citra dengan Evaluasi Fokus Visual Model

Alasan menarik:
Data lebih mudah dikumpulkan sendiri dengan kamera ponsel. Produk dapat mendeteksi kualitas buah, cacat permukaan, atau kematangan, lalu XAI memeriksa apakah model fokus pada cacat/warna buah atau latar belakang.

Risiko:
Kebaruan akademik lebih lemah jika hanya memakai dataset umum dan Grad-CAM. Perlu diferensiasi melalui data lokal atau evaluasi shortcut yang rapi.

## Arah yang Direkomendasikan

Rekomendasi saya setelah membaca Amara et al. (2024): tetap ambil domain penyakit tanaman, tetapi ubah fokus dari "menerapkan XAI berbasis konsep" menjadi "membangun toolkit audit XAI untuk menguji shortcut learning dan stabilitas penjelasan model".

Formulasi produk:
Produk yang dikembangkan adalah toolkit evaluasi XAI untuk model klasifikasi penyakit tanaman berbasis citra daun. Toolkit menghasilkan prediksi penyakit, peta penjelasan, hasil uji perturbasi, skor stabilitas penjelasan, rasio fokus ke daun/latar belakang, dan laporan potensi shortcut learning. Produk ini membantu mengevaluasi apakah model visi komputer menggunakan gejala visual yang relevan, bukan pola insidental dari dataset.

Batasan ruang lingkup:
- Fokus pada klasifikasi citra, bukan diagnosis agronomi penuh.
- Dataset utama PlantVillage, ditambah uji perturbasi atau citra lapangan sederhana jika memungkinkan.
- Model baseline: ResNet, EfficientNet, MobileNet, atau ViT kecil.
- Metode XAI: Grad-CAM/Grad-CAM++, Score-CAM, dan opsional ACE.
- Evaluasi: rasio fokus peta penjelasan pada daun/latar belakang, deletion/insertion score, stabilitas penjelasan terhadap perubahan cahaya/latar, dan evaluasi manual terbatas.

## Sumber

- Selvaraju et al. (2017), "Grad-CAM: Visual Explanations From Deep Networks via Gradient-Based Localization", ICCV. Peran: dasar metode penjelasan visual. URL: https://openaccess.thecvf.com/content_iccv_2017/html/Selvaraju_Grad-CAM_Visual_Explanations_ICCV_2017_paper.html
- Kim et al. (2018), "Interpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation Vectors (TCAV)". Peran: dasar XAI berbasis konsep. URL: https://arxiv.org/abs/1711.11279
- Koh et al. (2020), "Concept Bottleneck Models", ICML/PMLR. Peran: dasar model yang memprediksi konsep sebelum label. URL: https://proceedings.mlr.press/v119/koh20a/koh20a.pdf
- Chen et al. (2019), "This Looks Like That: Deep Learning for Interpretable Image Recognition", NeurIPS. Peran: dasar interpretabilitas berbasis prototipe. URL: https://papers.neurips.cc/paper_files/paper/2019/file/adf7ee2dcf142b0e11888e72b43fcb75-Paper.pdf
- TensorFlow Datasets, "plant_village". Peran: dataset tanaman; 54.303 gambar dan 38 kategori. URL: https://www.tensorflow.org/datasets/catalog/plant_village
- FAO, Plant Production and Protection. Peran: latar belakang dampak hama/penyakit tanaman; sampai 40 persen produksi tanaman hilang karena hama dan penyakit. URL: https://www.fao.org/plant-production-protection/about/en
- Jaeger et al. (2014), "Two public chest X-ray datasets for computer-aided screening of pulmonary diseases". Peran: dataset CXR TB Montgomery dan Shenzhen. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC4256233/
- Kementerian Kesehatan RI (2025), komitmen eliminasi TBC. Peran: latar belakang Indonesia sebagai negara beban TBC tinggi. URL: https://www.kemkes.go.id/id/menkes-dan-mendagri-tegaskan-komitmen-percepatan-eliminasi-tuberkulosis-tbc-dengan-dukungan-pemerintah-daerah
- Arya et al. (2022), "RDD2022: A multi-national image dataset for automatic Road Damage Detection". Peran: dataset kerusakan jalan; 47.420 citra dari enam negara. URL: https://arxiv.org/abs/2209.08538
- BPS, "Panjang Jalan Menurut Jenis Permukaan". Peran: latar belakang infrastruktur jalan Indonesia. URL: https://www.bps.go.id/indicator/17/51/1
- Amara, Konig-Ries, dan Samuel (2024), "Explainability of Deep Learning-Based Plant Disease Classifiers Through Automated Concept Identification". Peran: pembanding utama yang sudah menerapkan ACE pada InceptionV3 dan PlantVillage. URL: https://arxiv.org/pdf/2412.07408

## Bahan untuk Penulisan

Target: proposal

Saran struktur bab:
- Bab 1: latar belakang kebutuhan model visi komputer yang tidak hanya akurat tetapi juga dapat diaudit; rumusan masalah tentang cara mengevaluasi keselarasan penjelasan model dengan gejala visual dan cara mendeteksi shortcut learning.
- Bab 2: penelitian terkait dalam empat kelompok: deteksi penyakit tanaman, XAI visual attribution, XAI berbasis konsep, dan shortcut learning/dataset bias.
- Bab 3: metode penelitian berisi akuisisi dataset, preprocessing, pelatihan model baseline, penerapan XAI, rancangan metrik audit, uji perturbasi, dan rancangan prototipe laporan.
- Bab 4: jadwal penelitian: studi literatur, persiapan dataset, baseline model, implementasi XAI, evaluasi, dan penulisan.

Klaim kunci:
- Model visi komputer dengan akurasi tinggi tetap dapat bergantung pada shortcut visual.
- XAI perlu dievaluasi secara kuantitatif/konseptual agar tidak berhenti sebagai visualisasi subjektif.
- Penyakit tanaman cocok sebagai domain karena gejala visual dapat dijadikan konsep evaluasi, tetapi penerapan ACE pada PlantVillage sudah pernah dilakukan sehingga perlu fokus kebaruan pada toolkit audit dan uji robustness.

Rumusan masalah yang mungkin:
- Bagaimana merancang toolkit audit XAI untuk model klasifikasi penyakit tanaman berbasis citra?
- Bagaimana mengukur stabilitas dan keselarasan penjelasan model terhadap area daun atau gejala visual penyakit?
- Apakah uji perturbasi latar belakang, cahaya, dan bayangan dapat mengidentifikasi indikasi shortcut learning pada model?

Metrik evaluasi yang mungkin:
- Accuracy, precision, recall, dan F1-score untuk klasifikasi.
- Rasio fokus peta penjelasan pada area daun dibandingkan latar belakang.
- Deletion/insertion score untuk menguji faithfulness penjelasan.
- Skor stabilitas penjelasan terhadap perubahan latar belakang, brightness, blur, crop, dan bayangan.
- Analisis kualitatif untuk false positive dan false negative.

Gambar/tabel yang dibutuhkan:
- Diagram pipeline toolkit audit XAI.
- Bagan alir metodologi penelitian.
- Contoh output dashboard: citra input, prediksi, peta penjelasan, hasil uji perturbasi, dan skor audit.
- Tabel perbandingan metode XAI.
- Tabel skenario pengujian dan metrik.

Pertanyaan terbuka:
- Apakah produk akhirnya akan berupa aplikasi web/dashboard, notebook pipeline, atau library/toolkit Python?
- Apakah kamu ingin memakai PlantVillage saja dengan perturbasi terkontrol, atau menambah citra lokal/field images?
- Apakah fokus utama ingin pada Grad-CAM/Score-CAM yang lebih mudah, atau tetap memasukkan ACE sebagai pembanding?

## Perbandingan dengan Amara et al. 2024

Paper pembanding:
Amara, Konig-Ries, dan Samuel (2024), "Explainability of Deep Learning-Based Plant Disease Classifiers Through Automated Concept Identification", arXiv:2412.07408.

Yang sudah dikerjakan paper tersebut:
- Menerapkan Automated Concept-based Explanation (ACE) untuk klasifikasi penyakit tanaman.
- Menggunakan InceptionV3 dan dataset PlantVillage.
- Menggunakan ACE untuk mengidentifikasi konsep visual secara otomatis dari data citra.
- Membahas konsep yang relevan seperti bercak, area terinfeksi, bagian daun, dan pola venasi.
- Membahas korelasi yang tidak diinginkan seperti bias latar belakang, bayangan, dan pencahayaan.
- Menghubungkan konsep yang paling menonjol dengan kelas yang memiliki recall/F1 rendah, lalu menyarankan peningkatan keragaman data dan latar belakang.

Dampak terhadap klaim kebaruan:
- Tidak baru: "menggunakan ACE untuk menjelaskan model klasifikasi penyakit tanaman".
- Tidak cukup baru: "mendeteksi bias latar belakang atau bayangan pada PlantVillage menggunakan ACE".
- Lemah: "menggunakan Grad-CAM/ACE untuk menunjukkan model fokus pada area penyakit", kecuali ada metrik baru, dataset baru, interaksi produk, atau rancangan evaluasi baru.

Pergeseran kebaruan yang masih defensible:
- Membangun alat audit XAI interaktif yang memungkinkan pengguna memeriksa, memvalidasi, dan memberi label cluster konsep, lalu menghasilkan laporan audit.
- Membandingkan beberapa metode penjelasan, misalnya Grad-CAM++, Score-CAM, ACE, dan TCAV, memakai protokol keselarasan dan faithfulness yang sama.
- Bergerak melampaui evaluasi PlantVillage saja dengan menambahkan citra lapangan, citra lokal dari kamera ponsel, atau gangguan latar belakang/pencahayaan terkontrol.
- Membuat benchmark shortcut learning kuantitatif: background swap, brightness/shadow perturbation, leaf-only mask, background-only control, serta pelaporan stabilitas prediksi dan penjelasan.
- Menambahkan validasi konsep berbasis human-in-the-loop: pengguna memberi label konsep sebagai gejala, struktur daun, latar belakang, bayangan, atau artefak tidak relevan.
- Mengubah hasil menjadi toolkit evaluasi untuk model visi komputer pertanian, bukan hanya replikasi eksperimen paper.

Kesimpulan jujur:
Topik awal masih layak, tetapi kebaruannya lebih lemah daripada perkiraan awal jika hanya memakai PlantVillage + InceptionV3 + ACE. Agar layak sebagai skripsi, topik perlu diformulasikan sebagai prototipe/toolkit audit XAI dengan evaluasi robustness dan shortcut learning yang kuantitatif, atau memakai setup data yang lebih realistis/lokal. Tanpa pergeseran itu, topik berisiko menjadi reproduksi Amara et al. (2024).

## Penilaian Ide Setelah Paper Pembanding

Ide awal tidak menjadi jelek. Yang berubah adalah posisi kebaruannya. Setelah ada Amara et al. (2024), topik "XAI untuk penyakit tanaman" tidak bisa lagi dijual sebagai kebaruan umum karena paper tersebut sudah menunjukkan bahwa ACE dapat menemukan konsep penyakit dan bias latar belakang pada PlantVillage. Jadi, ide awal masih bagus sebagai domain dan masalah, tetapi perlu dinaikkan levelnya dari "menjelaskan model" menjadi "mengaudit model".

Bagian yang masih kuat:
- Domain penyakit tanaman tetap relevan dan mudah dipahami.
- Masalah shortcut learning tetap nyata dan penting.
- XAI tetap cocok karena gejala penyakit tanaman bersifat visual.
- Produk audit XAI cocok untuk Skripsi Inovasi Produk karena dapat dirancang, diimplementasikan, dan diuji.

Bagian yang melemah:
- Klaim "menggunakan ACE untuk penyakit tanaman" sudah tidak baru.
- Klaim "menemukan bias background/shadow pada PlantVillage" sudah tidak cukup kuat.
- Jika hanya eksperimen klasifikasi + XAI visual, topik menjadi terlalu tipis.

Rekomendasi akhir:
Jangan membuang domain penyakit tanaman, tetapi ubah judul dan kontribusi menjadi pengembangan alat audit. Kata kunci yang lebih kuat: audit XAI, shortcut learning, robustness, explanation stability, perturbation testing, dan laporan evaluasi model.

## Ide Lain dan Kemungkinan Jenis TA

### 1. Toolkit Audit XAI untuk Penyakit Tanaman

Judul:
Pengembangan Toolkit Audit Explainable AI untuk Evaluasi Shortcut Learning pada Model Klasifikasi Penyakit Tanaman Berbasis Citra

Inti:
Membangun alat yang menguji model dengan peta penjelasan, background swap, perubahan cahaya, leaf-only mask, background-only control, dan skor stabilitas penjelasan.

Kemungkinan jenis TA:
- Paling cocok: Skripsi Inovasi Produk.
- Bisa juga: Skripsi Ilmiah Akademik, jika fokusnya eksperimen metrik dan analisis tanpa produk interaktif.
- Bisa menjadi Publikasi Ilmiah jika evaluasinya rapi, dataset/benchmark jelas, dan hasilnya cukup kuat.

Catatan:
Ini rekomendasi utama karena masih dekat dengan minat CV x XAI, tetapi sudah menjauh dari replikasi Amara et al. (2024).

### 2. Benchmark Shortcut Learning pada Dataset Penyakit Tanaman

Judul:
Rancang Bangun Benchmark Shortcut Learning untuk Evaluasi Robustness Model Klasifikasi Penyakit Tanaman

Inti:
Membuat benchmark terkontrol: citra asli, latar belakang diganti, cahaya diubah, bayangan ditambah, daun dimask, latar saja diuji. Fokusnya bukan dashboard, tetapi protokol pengujian dan analisis kuantitatif.

Kemungkinan jenis TA:
- Paling cocok: Skripsi Ilmiah Akademik.
- Bisa juga: Skripsi Inovasi Produk jika benchmark dikemas sebagai perangkat lunak/toolkit yang bisa digunakan ulang.
- Bisa menjadi Publikasi Ilmiah jika benchmark dan hasil eksperimennya cukup kuat.

Catatan:
Ini lebih "research-heavy" daripada produk. Bagus jika kamu suka eksperimen dan metrik.

### 3. Human-in-the-loop XAI untuk Validasi Konsep Penyakit Tanaman

Judul:
Pengembangan Sistem Human-in-the-loop untuk Validasi Konsep Visual pada Explainable AI Penyakit Tanaman

Inti:
Sistem menampilkan cluster konsep/peta penjelasan, lalu pengguna memberi label: gejala penyakit, struktur daun, latar belakang, bayangan, atau artefak. Hasil label dipakai untuk laporan kualitas model.

Kemungkinan jenis TA:
- Paling cocok: Skripsi Inovasi Produk.
- Bisa juga: Proyek Kolaboratif jika melibatkan mahasiswa pertanian/agronomi atau pengguna domain.
- Bisa menjadi Skripsi Ilmiah Akademik jika fokusnya evaluasi kualitas label dan agreement antar penilai.

Catatan:
Menarik karena mengisi celah praktis dari paper Amara et al. (2024), yaitu kebutuhan alat interaktif untuk mengeksplorasi dan memvalidasi konsep.

### 4. XAI untuk Deteksi TBC Chest X-Ray Berbasis Keselarasan Area Paru

Judul:
Evaluasi Keselarasan Penjelasan Model Visi Komputer dengan Area Paru pada Deteksi Tuberkulosis Berbasis Chest X-Ray

Inti:
Model mendeteksi normal/TB, lalu XAI diuji apakah fokusnya berada pada area paru atau malah marker, border, teks, dan artefak luar paru.

Kemungkinan jenis TA:
- Paling cocok: Skripsi Ilmiah Akademik.
- Bisa juga: Skripsi Inovasi Produk jika dibuat sebagai alat audit CXR dengan visualisasi dan laporan.
- Kurang cocok untuk Proyek Industri kecuali ada mitra kesehatan yang jelas.

Catatan:
Akademiknya kuat, tetapi risikonya lebih tinggi karena klaim medis dan validasi radiologis. Tanpa ahli, batasi klaim pada area paru, bukan diagnosis klinis.

### 5. XAI untuk Deteksi Kerusakan Jalan dan Analisis False Positive

Judul:
Prototipe Explainable Road Damage Detection untuk Mengidentifikasi Shortcut Visual pada Citra Jalan

Inti:
Sistem mendeteksi retakan/lubang jalan, lalu menganalisis apakah model salah fokus ke bayangan, marka jalan, genangan, kendaraan, atau tekstur aspal.

Kemungkinan jenis TA:
- Paling cocok: Skripsi Inovasi Produk.
- Bisa juga: Proyek Industri jika ada mitra pemerintah/kontraktor/institusi yang membutuhkan inspeksi jalan.
- Bisa menjadi Skripsi Ilmiah Akademik jika fokus pada evaluasi model dan metrik XAI untuk object detection.

Catatan:
Lebih produk dan lebih lokal-praktis, tetapi XAI untuk object detection lebih rumit daripada klasifikasi.

### 6. Deteksi Penyakit Tanaman dengan Dataset Lokal dan Audit XAI

Judul:
Pengembangan Dataset Citra Lapangan dan Audit XAI untuk Klasifikasi Penyakit Tanaman Lokal

Inti:
Mengumpulkan dataset kecil dari kamera ponsel untuk tanaman tertentu, lalu membandingkan model yang dilatih/diuji pada PlantVillage dan citra lapangan. XAI dipakai untuk melihat pergeseran fokus model.

Kemungkinan jenis TA:
- Paling cocok: Skripsi Ilmiah Akademik jika kontribusi utamanya dataset dan analisis generalisasi.
- Bisa juga: Skripsi Inovasi Produk jika dataset dipakai dalam aplikasi/tool audit.
- Bisa menjadi Proyek Kolaboratif jika melibatkan pihak pertanian atau mahasiswa bidang pertanian.

Catatan:
Ini lebih kuat dari PlantVillage murni, tetapi membutuhkan usaha pengumpulan data dan kontrol kualitas anotasi.

### 7. Generator Laporan Audit XAI untuk Model Visi Komputer

Judul:
Pengembangan Generator Laporan Audit Explainable AI untuk Model Klasifikasi Citra

Inti:
Membuat perangkat lunak umum yang menerima model dan dataset, lalu menghasilkan laporan otomatis: performa klasifikasi, peta penjelasan, deletion/insertion score, stabilitas terhadap perturbasi, dan ringkasan potensi shortcut.

Kemungkinan jenis TA:
- Paling cocok: Skripsi Inovasi Produk.
- Bisa juga: Proyek Industri jika diarahkan untuk kebutuhan audit model di perusahaan/instansi.
- Bisa menjadi Skripsi Ilmiah Akademik jika fokusnya evaluasi metode audit pada beberapa dataset.

Catatan:
Lebih general dan fleksibel, tetapi perlu hati-hati agar tidak terlalu luas. Sebaiknya tetap dibatasi pada satu domain uji, misalnya penyakit tanaman.
