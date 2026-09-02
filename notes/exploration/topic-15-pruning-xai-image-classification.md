---
cssclasses:
  - full-width
---
# Detail Topik 15: Evaluasi Dampak Structured Pruning terhadap Performa dan Penjelasan XAI Model Klasifikasi Citra

Date: 2026-09-02

Updated: 2026-09-03

Catalog Reference: [`topic-catalog.md`](topic-catalog.md)

## Status Singkat

**Kandidat layak bersyarat dan menarik untuk jalur Computer Vision--XAI; belum dipilih secara final.** Ide awal mengenai penggunaan beberapa model Computer Vision, pemangkasan model, pengujian klasifikasi, dan XAI telah dipersempit menjadi evaluasi faktorial terkontrol atas hubungan antara **ukuran arsitektur**, **tingkat structured pruning**, dan **kualitas penjelasan** pada satu tugas klasifikasi citra.

Task inti yang direkomendasikan adalah klasifikasi citra, bukan deteksi objek. YOLO tidak dimasukkan ke eksperimen inti karena YOLO terutama merupakan keluarga model deteksi objek; mencampurkan YOLO dengan ResNet untuk klasifikasi akan mencampurkan task, bentuk keluaran, metrik performa, dan metode penjelasan. Jika deteksi objek lebih diminati, keseluruhan rancangan harus dipindahkan menjadi studi khusus deteksi dan bukan sekadar menambahkan YOLO sebagai model ketiga.

Model utama yang direncanakan adalah ResNet-18 dan ResNet-50, yaitu dua ukuran dalam satu keluarga arsitektur. Keduanya akan mengalami structured channel pruning pada beberapa target pengurangan operasi komputasi. Penelitian akan membedakan tiga konsep yang sering tercampur: **pergeseran penjelasan terhadap model padat** (*explanation drift*), **kesetiaan penjelasan terhadap model yang sedang dijelaskan** (*faithfulness*), dan **kesesuaian spasial penjelasan dengan objek beranotasi** (*localization/plausibility*).

Kebaruan yang ditargetkan bersifat **empiris dan metodologis**, bukan metode pruning atau metode XAI baru. Pertanyaan umum "apakah pruning memengaruhi explainability" telah diteliti; karena itu, kandidat ini hanya layak jika kontribusinya dipertahankan pada evaluasi berpasangan dan multidimensi yang lebih spesifik.

## 1. Opsi Judul

### Judul utama

- **Bahasa Indonesia**: *Studi Empiris Dampak Structured Pruning terhadap Performa Prediktif dan Kualitas Penjelasan Model Klasifikasi Citra*
- **Bahasa Inggris**: *An Empirical Study of the Effects of Structured Pruning on Predictive Performance and Explanation Quality in Image Classifiers*

### Alternatif yang menonjolkan gap

- **Bahasa Indonesia**: *Evaluasi Pergeseran, Faithfulness, dan Lokalisasi Penjelasan XAI pada Model Klasifikasi Citra Terpangkas*
- **Bahasa Inggris**: *Evaluating Explanation Drift, Faithfulness, and Localization in Pruned Image Classification Models*

### Alternatif yang menonjolkan desain eksperimen

- **Bahasa Indonesia**: *Analisis Faktorial Performa dan Kualitas Penjelasan pada Model Klasifikasi Citra dengan Structured Pruning*
- **Bahasa Inggris**: *A Factorial Analysis of Performance and Explanation Quality in Structured-Pruned Image Classifiers*

Judul sebaiknya tidak menyebut Grad-CAM, ResNet, atau nama dataset sebelum pilot membuktikan seluruh komponen dapat dijalankan secara stabil.

## 2. Penjelasan Sederhana

Pruning mengecilkan jaringan saraf dengan menghapus bobot, kanal, atau struktur yang dianggap kurang penting. Model hasil pruning dapat memiliki akurasi yang hampir sama dengan model padat, tetapi kesamaan akurasi tidak menjamin bahwa model masih menggunakan bagian citra yang sama untuk mengambil keputusan.

Sebagai contoh, model padat dan model terpangkas dapat sama-sama memprediksi ras kucing dengan benar. Namun, model padat mungkin berfokus pada wajah dan bentuk telinga, sedangkan model terpangkas beralih ke latar belakang atau tekstur yang kebetulan berkorelasi dengan kelas. Jika hanya akurasi yang diperiksa, perubahan tersebut tidak terlihat. Heatmap XAI dapat membantu mengauditnya, tetapi heatmap juga tidak boleh langsung dianggap benar.

Penelitian ini akan menguji model padat dan model terpangkas menggunakan citra yang sama. Pada sampel yang label prediksinya tetap sama, penelitian akan mengukur apakah penjelasannya bergeser. Selanjutnya, penelitian akan memeriksa apakah penjelasan tersebut tetap setia pada perilaku masing-masing model melalui uji perturbasi, serta apakah area pentingnya masih berada pada objek berdasarkan mask anotasi. Dengan demikian, penelitian tidak menyamakan "heatmap mirip" dengan "penjelasan berkualitas".

Penelitian dilaksanakan sebagai **eksperimen komputasional terkontrol**. Skrip eksperimen digunakan untuk menerapkan pruning, mengevaluasi model, menghasilkan attribution map, menghitung metrik XAI, dan mengukur biaya inferensi secara konsisten. Luaran utamanya adalah temuan empiris mengenai perubahan performa serta kualitas penjelasan dan analisis ilmiah atas hubungan antarvariabel tersebut.

## 3. Fokus dan Pertanyaan Penelitian

### Fokus utama

Hubungan utama yang akan diuji adalah:

> ukuran model × metode pruning × tingkat pengurangan MACs → performa prediktif + efisiensi inferensi + explanation drift + faithfulness + localization

Eksperimen akan menggunakan evaluasi berpasangan pada input yang sama. Analisis explanation drift utama hanya dilakukan pada subset sampel yang diprediksi benar oleh model padat dan model terpangkas dengan kelas yang sama. Pembatasan ini mencegah perubahan heatmap akibat perubahan kelas target disalahartikan sebagai perubahan cara model bernalar.

### Pertanyaan penelitian sementara

1. Bagaimana tingkat structured pruning memengaruhi akurasi, kalibrasi, latensi, penggunaan memori, ukuran model, dan jumlah operasi ResNet-18 serta ResNet-50?
2. Pada sampel dengan prediksi yang tetap sama, apakah peningkatan tingkat pruning menyebabkan explanation drift terhadap model padat?
3. Apakah penjelasan model terpangkas tetap faithful terhadap modelnya sendiri dan tetap terlokalisasi pada objek, meskipun akurasi agregat masih dipertahankan?
4. Apakah dampak pruning terhadap kualitas penjelasan berbeda menurut ukuran model atau kriteria pruning?
5. Konfigurasi mana yang memberikan trade-off Pareto terbaik antara akurasi, pengurangan MACs, latensi CPU, faithfulness, dan localization?

Pertanyaan "apakah XAI berpengaruh pada hasil pruning" perlu dibedakan dari fokus di atas. Dalam scope inti, XAI digunakan untuk **mengaudit dampak pruning**, bukan sebagai masukan untuk menentukan unit yang dipangkas. Jika XAI dipakai sebagai kriteria pruning, penelitian berubah menjadi pengembangan atau perbandingan *explainability-aware pruning* dan berhadapan langsung dengan *Pruning by Explaining*, X-Pruner, serta C-SWAP.

## 4. Analisis Kebaruan

### 4.1 Kondisi Penelitian Sebelumnya

- *What Do Compressed Deep Neural Networks Forget?* menunjukkan bahwa akurasi agregat dapat menyembunyikan dampak kompresi yang tidak proporsional pada kelas dan contoh tertentu.
- *Lost in Pruning* menunjukkan bahwa kesamaan test accuracy belum cukup untuk menjamin performa pada metrik yang lebih sulit, termasuk data di luar distribusi dan ketahanan terhadap noise.
- Merkle et al. melalui *Less is More: The Influence of Pruning on the Explainability of CNNs* telah menguji pengaruh beberapa rasio pruning terhadap perceived explainability melalui eksperimen berbasis manusia. Oleh karena itu, kandidat ini bukan penelitian pertama mengenai pruning dan explainability pada klasifikasi citra.
- Studi 2025 *A Study on the Faithfulness of Feature Attribution Explanations in Pruned Vision-Based Multi-Task Learning* telah mengukur faithfulness Grad-CAM menggunakan IROF pada model multi-task yang mengalami structured dan unstructured pruning. Pertanyaan umum mengenai faithfulness setelah pruning juga bukan ruang kosong.
- *Pruning by Explaining*, X-Pruner, dan C-SWAP menggunakan informasi explainability untuk menentukan struktur yang dipangkas. Penggunaan XAI sebagai dasar pruning bukan novelty baru.
- Quantus telah menyediakan kumpulan metrik evaluasi XAI untuk faithfulness, robustness, localization, complexity, randomization, dan sifat aksiomatik. Mengintegrasikan library tersebut tanpa pertanyaan eksperimen yang spesifik bukan kontribusi yang cukup.
- DepGraph/Torch-Pruning telah menyediakan mekanisme structured pruning yang menangani ketergantungan antarlapis. Implementasi channel pruning generik juga bukan kontribusi baru.

### 4.2 Gap yang Ditargetkan

Gap yang masih masuk akal dan perlu diverifikasi lebih sistematis adalah keterbatasan studi terdahulu dalam menggabungkan seluruh elemen berikut pada klasifikasi citra dalam satu protokol terkontrol:

1. perbandingan model padat dan terpangkas secara berpasangan pada input yang sama;
2. analisis explanation drift yang dikondisikan pada **prediction agreement**, sehingga perubahan kelas target tidak mencemari perbandingan heatmap;
3. pemisahan antara similarity/drift, faithfulness terhadap model, dan localization terhadap mask objek;
4. perbandingan dua ukuran dalam satu keluarga arsitektur dan dua kriteria structured pruning pada target pengurangan MACs yang disamakan;
5. pengaitan kualitas penjelasan dengan akurasi, kalibrasi, ukuran model, MACs, latensi CPU, dan memori aktual; serta
6. pelaporan kurva dan titik patah ketika akurasi masih tampak stabil tetapi salah satu dimensi kualitas penjelasan mulai menurun.

Elemen-elemen tersebut membentuk **hipotesis gap**, bukan dasar untuk klaim "pertama". Pencarian awal telah menemukan pembanding yang sangat dekat, sehingga literature review final wajib memeriksa apakah studi klasifikasi lain sudah memakai kombinasi prediction agreement, explanation similarity, faithfulness, dan ground-truth localization secara bersamaan.

### 4.3 Kebaruan yang Aman

Rumusan kontribusi sementara yang defensible adalah:

> Penelitian ini menawarkan protokol evaluasi berpasangan untuk mengukur apakah structured pruning mengubah bukti visual yang digunakan model klasifikasi ketika prediksinya tetap sama, dengan membedakan explanation drift, faithfulness, dan localization serta menghubungkannya dengan trade-off efisiensi inferensi.

Kontribusi ilmiah yang ditargetkan dibagi menjadi dua lapisan utama:

| Lapisan kontribusi | Bentuk kontribusi |
|---|---|
| Empiris | Bukti instance-level tentang kapan akurasi/prediksi tetap stabil tetapi penjelasan mulai bergeser atau kehilangan localization |
| Metodologis | Evaluasi berpasangan dan agreement-conditioned yang memisahkan drift, faithfulness, dan plausibility/localization |

Skrip, konfigurasi, attribution map, dan hasil mentah disertakan sebagai artefak pendukung reprodusibilitas, bukan sebagai sumber kebaruan tersendiri.

### 4.4 Mengapa Tiga Dimensi XAI Harus Dipisahkan

| Dimensi | Pertanyaan yang dijawab | Contoh metrik | Kesalahan interpretasi yang dihindari |
|---|---|---|---|
| Explanation drift | Apakah peta atribusi model terpangkas berbeda dari baseline pada prediksi yang sama? | Spearman rank correlation, top-k overlap, SSIM sebagai metrik tambahan | Peta yang berbeda langsung disebut lebih buruk |
| Faithfulness | Apakah fitur yang diberi skor penting benar-benar memengaruhi output model yang dijelaskan? | IROF, deletion AUC, faithfulness correlation | Peta yang terlihat masuk akal dianggap setia pada model |
| Localization/plausibility | Apakah energi atribusi berada pada objek yang beranotasi? | Relevance Mass Accuracy, Energy-Based Pointing Game, mask overlap | Fokus pada objek dianggap bukti kausal lengkap |

Mask objek adalah proksi plausibility, bukan ground truth proses internal model. Pada klasifikasi fine-grained, bagian kecil seperti telinga atau wajah dapat lebih penting daripada seluruh tubuh; karena itu, IoU biner tidak boleh menjadi satu-satunya metrik localization.

### 4.5 Batas Klaim

Penelitian tidak akan mengklaim:

- algoritma pruning atau metode XAI baru;
- penelitian pertama yang menghubungkan pruning dan explainability;
- heatmap sebagai bukti langsung proses kausal internal model;
- penjelasan yang mirip dengan model padat pasti lebih baik;
- localization pada mask objek selalu identik dengan faithfulness;
- pengurangan parameter atau sparsity nominal pasti menghasilkan percepatan aktual;
- hasil berlaku untuk semua arsitektur, dataset, metode pruning, metode XAI, dan perangkat keras.

## 5. Posisi Penelitian dan Batasan

### Masalah penelitian

Evaluasi model terpangkas yang hanya menggunakan akurasi dan ukuran model dapat melewatkan perubahan perilaku pada contoh tertentu serta perubahan bukti visual yang digunakan model. Di sisi lain, pemeriksaan heatmap secara manual bersifat subjektif, sulit direproduksi, dan tidak membedakan kemiripan penjelasan dari faithfulness.

### Pendekatan penelitian

Penelitian menggunakan eksperimen berpasangan dan faktorial dengan prosedur berikut:

- memvariasikan ukuran arsitektur, kriteria pruning, dan target pengurangan MACs;
- membandingkan model padat dan model terpangkas pada input serta kelas target yang sama;
- mengelompokkan sampel berdasarkan perubahan kebenaran dan kesamaan prediksi;
- mengukur performa prediktif, explanation drift, faithfulness, localization, serta efisiensi inferensi;
- mengendalikan sumber bobot awal, split data, preprocessing, fine-tuning, target layer XAI, dan perangkat pengujian; serta
- menganalisis efek utama, efek interaksi, interval kepercayaan, effect size, dan Pareto frontier.

Skrip berbasis CLI hanya berfungsi sebagai instrumen untuk menjalankan prosedur tersebut secara konsisten serta menyimpan konfigurasi dan hasil per sampel.

### Batasan penelitian

1. Task inti hanya klasifikasi citra single-label.
2. Dataset utama direkomendasikan Oxford-IIIT Pet karena menyediakan 37 kelas, sekitar 200 citra per kelas, bounding box kepala, dan trimap foreground--background.
3. Arsitektur inti dibatasi pada ResNet-18 dan ResNet-50 dengan bobot awal dari sumber dan tahap pretraining yang sama.
4. Pruning inti berupa structured channel pruning. Unstructured pruning tidak menjadi eksperimen utama karena sparsity bobot tidak otomatis menghasilkan percepatan pada CPU umum.
5. Kriteria pruning dibatasi pada magnitude berbasis norm dan satu kriteria berbasis sensitivitas, misalnya Taylor importance.
6. Target pruning ditentukan berdasarkan pengurangan MACs, bukan hanya persentase parameter nol.
7. Metode XAI dibatasi pada Grad-CAM dan satu pembanding yang kompatibel, misalnya Integrated Gradients.
8. Evaluasi utama dilakukan pada satu test split tetap dengan preprocessing dan target kelas yang konsisten.
9. Penelitian tidak mengembangkan metode pruning baru, XAI baru, dashboard generik, mobile application, atau human study.
10. YOLO, object detection, segmentation sebagai task prediksi, quantization, knowledge distillation, dan neural architecture search tidak termasuk scope inti.

## 6. Landasan Teknik dan Ilmiah

- **Structured channel pruning**: penghapusan kanal atau kelompok parameter beserta struktur yang bergantung padanya sehingga bentuk tensor benar-benar mengecil dan berpotensi mempercepat inferensi pada hardware umum.
- **Magnitude importance**: skor kepentingan berdasarkan besar norm parameter. Metode ini sederhana dan menjadi baseline yang mudah direproduksi.
- **Taylor importance**: pendekatan sensitivitas orde pertama yang memperkirakan perubahan objektif akibat penghapusan parameter atau kelompok parameter.
- **MACs**: jumlah operasi multiply--accumulate sebagai proksi biaya komputasi. MACs harus dilaporkan bersama latensi aktual karena keduanya tidak selalu berbanding lurus.
- **Grad-CAM**: metode attribution berbasis gradien dan activation map pada convolutional layer untuk menghasilkan peta lokasi yang relevan terhadap kelas target.
- **Integrated Gradients**: metode attribution yang mengintegrasikan gradien sepanjang jalur dari baseline input menuju input aktual.
- **Explanation drift**: perubahan peta atribusi model hasil pruning terhadap model padat pada input dan kelas target yang sama. Istilah ini merupakan definisi operasional penelitian, bukan klaim bahwa setiap perubahan merupakan kerusakan.
- **Faithfulness**: tingkat kesesuaian penjelasan dengan perilaku prediktif model yang dijelaskan, biasanya diuji dengan mengubah fitur menurut urutan kepentingannya dan mengamati perubahan output.
- **Localization/plausibility**: tingkat kesesuaian spasial atribusi dengan region of interest yang dianotasi manusia. Dimensi ini berbeda dari faithfulness.
- **Prediction agreement**: proporsi dan himpunan contoh yang memperoleh prediksi kelas sama dari model padat dan model terpangkas.

## 7. Rencana Pengujian dan Parameter Ukur

### 7.1 Desain Minimum yang Direkomendasikan

| Faktor | Level yang direncanakan |
|---|---|
| Ukuran model | ResNet-18, ResNet-50 |
| Kriteria structured pruning | Magnitude/norm, Taylor importance |
| Target pengurangan MACs | 25%, 50%, 70% dari baseline, ditambah model padat 0% |
| Dataset/task | Oxford-IIIT Pet, klasifikasi 37 ras |
| Metode XAI | Grad-CAM, Integrated Gradients |
| Lingkungan inferensi | Satu CPU dan konfigurasi runtime yang tetap |

Karena baseline tidak bergantung pada kriteria pruning, desain menghasilkan dua model padat dan 2 × 2 × 3 = 12 model terpangkas, atau **14 varian model**. Setiap varian akan dievaluasi dengan dua metode XAI. Fine-tuning pascapruning menggunakan budget epoch, optimizer, scheduler, augmentasi, dan kriteria penghentian yang sama pada setiap sel eksperimen.

Jika biaya komputasi terlalu tinggi, desain minimum fallback adalah ResNet-18 dengan dua kriteria pruning dan tiga target pengurangan MACs. Pengurangan jumlah arsitektur lebih baik daripada mengurangi validitas metrik XAI atau menambah dataset kecil tanpa replikasi yang memadai.

### 7.2 Protokol Pasangan Sampel

Untuk setiap pasangan model padat--terpangkas dan setiap metode XAI, test set dibagi menjadi:

1. **stable-correct**: keduanya benar dan memprediksi kelas yang sama;
2. **stable-wrong**: keduanya salah tetapi memprediksi kelas yang sama;
3. **correct-to-wrong**: model padat benar dan model terpangkas salah;
4. **wrong-to-correct**: model padat salah dan model terpangkas benar;
5. **changed-wrong**: prediksi berubah dan keduanya salah.

Explanation drift utama dihitung pada kelompok stable-correct. Kelompok lain dianalisis terpisah sebagai failure taxonomy. Attribution map harus dihitung terhadap kelas target yang sama ketika dua model dibandingkan; kelas prediksi masing-masing dapat disajikan sebagai analisis tambahan.

### 7.3 Metrik

- **Performa prediktif**: top-1 accuracy, macro-F1, negative log-likelihood, expected calibration error, dan akurasi per kelas.
- **Perubahan prediksi**: prediction agreement, transition matrix kategori pasangan, serta jumlah Pruning Identified Exemplars bila definisinya diadaptasi secara tepat.
- **Explanation drift**: Spearman correlation pada ranking piksel/superpixel, top-k attribution overlap, dan SSIM hanya sebagai metrik pelengkap karena peta atribusi bukan citra biasa.
- **Faithfulness**: IROF atau deletion AUC serta satu metrik faithfulness tambahan dari Quantus. Konfigurasi perturbasi harus tetap dan dilaporkan karena deletion metric dapat menghasilkan input di luar distribusi.
- **Localization**: proporsi energi atribusi di dalam trimap objek, Energy-Based Pointing Game, dan analisis terpisah pada bounding box kepala bila relevan untuk klasifikasi ras.
- **Robustness penjelasan**: perubahan atribusi terhadap perturbasi kecil yang mempertahankan prediksi, sebagai eksperimen tambahan jika waktu cukup.
- **Efisiensi**: jumlah parameter, MACs, ukuran checkpoint, waktu muat, latensi batch-1, throughput, dan peak RAM pada CPU.
- **Trade-off**: Pareto frontier performa--latensi--faithfulness--localization.
- **Reproducibility**: seed, split dataset, versi library, checkpoint hash, konfigurasi pruning, jumlah fine-tuning epoch, preprocessing, target layer XAI, baseline Integrated Gradients, dan hardware.

### 7.4 Analisis Statistik

1. Gunakan unit analisis per citra dan per seed, bukan hanya satu nilai agregat per model.
2. Jalankan minimal tiga seed untuk training/fine-tuning jika waktu memungkinkan; jika tidak, batasi klaim dan gunakan bootstrap per sampel untuk ketidakpastian evaluasi.
3. Hitung interval kepercayaan bootstrap berpasangan untuk selisih metrik model padat--terpangkas.
4. Analisis pengaruh arsitektur, kriteria pruning, dan target MACs beserta interaksinya menggunakan model statistik yang sesuai distribusi metrik.
5. Koreksi perbandingan jamak bila melakukan banyak uji pasangan.
6. Laporkan effect size, bukan hanya nilai p.
7. Tentukan *accuracy-preserving region* sebelum melihat hasil, misalnya degradasi akurasi absolut tidak lebih dari ambang yang disepakati. Kemudian uji apakah metrik XAI sudah berubah di dalam region tersebut.

### 7.5 Validasi Penting

- Lakukan sanity check metode XAI pada model yang parameternya diacak untuk memastikan peta bereaksi terhadap perubahan model.
- Pastikan Grad-CAM pada model padat dan terpangkas memakai convolutional stage yang semantik dan resolusi relatifnya sebanding.
- Audit apakah operasi pruning benar-benar mengubah bentuk tensor, jumlah MACs, ukuran berkas, dan latensi; jangan hanya mempercayai sparsity nominal.
- Gunakan mask setelah transformasi geometris yang identik dengan citra agar metrik localization tidak salah alignment.
- Simpan attribution map mentah sebelum thresholding agar hasil dapat dihitung ulang.

## 8. Pemetaan ke Bab Proposal dan Skripsi Ilmiah Akademik

- **Proposal Bab 1**: kebutuhan model vision yang efisien, keterbatasan evaluasi berbasis akurasi, kesenjangan bukti mengenai perubahan penjelasan setelah pruning, rumusan masalah, tujuan, batasan, serta manfaat ilmiah dan praktis penelitian.
- **Proposal Bab 2**: structured pruning, magnitude/Taylor importance, dampak kompresi di luar akurasi, Grad-CAM dan Integrated Gradients, evaluasi XAI, prediction agreement, penelitian pruning--explainability, dan gap penelitian.
- **Proposal Bab 3**: deskripsi data dan mask, desain faktorial, prosedur training--pruning--fine-tuning, protokol pasangan sampel, metrik, kontrol eksperimen, serta rancangan analisis statistik.
- **Proposal Bab 4**: jadwal verifikasi literatur, studi pendahuluan dataset/model, penyiapan instrumen eksperimen, eksperimen pruning, evaluasi XAI, analisis, dan penulisan.
- **Skripsi Bab 1**: latar belakang, perumusan masalah, batasan penelitian, tujuan, dan manfaat penelitian.
- **Skripsi Bab 2**: tinjauan pustaka tentang structured pruning, kompresi model, XAI, evaluasi kualitas penjelasan, dan penelitian pruning--explainability.
- **Skripsi Bab 3**: metodologi yang mencakup data, faktor dan variabel eksperimen, rancangan pruning dan fine-tuning, protokol pasangan sampel, metrik, kontrol, dan analisis statistik.
- **Skripsi Bab 4**: implementasi lingkungan dan instrumen eksperimen, model lineage, pruning, fine-tuning, integrasi XAI/Quantus, penyimpanan hasil per sampel, dan profiling CPU.
- **Skripsi Bab 5**: hasil faktorial, explanation drift pada stable-correct, faithfulness, localization, Pareto frontier, failure taxonomy, pembahasan terhadap penelitian terdahulu, dan keterbatasan.
- **Skripsi Bab 6**: simpulan yang menjawab perumusan masalah dan tujuan penelitian serta saran penelitian lanjutan.

## 9. Risiko dan Kelayakan Akademik

- **Risiko kebaruan**: sudah ada studi langsung mengenai pruning dan explainability. Mitigasinya adalah tidak memakai klaim umum, menonjolkan evaluasi agreement-conditioned, memisahkan tiga dimensi XAI, dan melakukan literature review sistematis sebelum topik diterima.
- **Risiko interpretasi XAI**: similarity, faithfulness, dan localization dapat memberikan kesimpulan yang berbeda. Mitigasinya adalah melaporkan ketiganya tanpa membuat satu skor gabungan yang arbitrer.
- **Risiko metric gaming/OOD**: deletion dan insertion metric sensitif terhadap cara perturbasi. Mitigasinya adalah memakai lebih dari satu metrik, mengunci perturbation baseline, dan menyatakan keterbatasan OOD.
- **Risiko komputasi training**: 14 varian dengan beberapa seed memerlukan GPU untuk fine-tuning yang praktis. Mitigasinya adalah melakukan pilot ResNet-18, memakai transfer learning, dan mengaktifkan desain fallback satu arsitektur.
- **Risiko latensi**: penurunan MACs belum tentu menghasilkan percepatan karena operator, memory access, dan runtime. Mitigasinya adalah mengukur latensi dan memori aktual pada perangkat target.
- **Risiko perbandingan layer XAI**: structured pruning mengubah jumlah kanal dan dapat memengaruhi layer target. Mitigasinya adalah membandingkan stage semantik yang sama dan mendokumentasikan resolusi feature map.
- **Risiko dataset**: mask seluruh tubuh tidak selalu menjadi ground truth fitur untuk membedakan ras. Mitigasinya adalah memakai localization sebagai plausibility, menambahkan ROI kepala, dan tidak menyamakannya dengan faithfulness.
- **Risiko scope**: penambahan YOLO, quantization, distillation, banyak dataset, dan dashboard akan membuat eksperimen tidak terkendali. Scope inti harus dikunci sebelum implementasi.

### Fallback plan

1. Jika ResNet-50 terlalu mahal, gunakan ResNet-18 saja dan pertahankan dua kriteria pruning serta tiga dimensi XAI.
2. Jika Integrated Gradients terlalu lambat untuk seluruh test set, jalankan pada subset berstratifikasi yang ditentukan sebelum analisis dan gunakan Grad-CAM untuk cakupan penuh.
3. Jika Taylor importance tidak stabil, gunakan magnitude sebagai eksperimen inti dan Taylor sebagai pilot yang kegagalannya didokumentasikan; jangan mengganti metode setelah melihat hasil final tanpa protokol baru.
4. Jika latency profiling bervariasi tinggi, tingkatkan warm-up dan pengulangan, kunci thread serta power mode, lalu laporkan median dan interval kuantil.
5. Jika klasifikasi 37 kelas tidak stabil, gunakan task species dua kelas hanya untuk debug; task final sebaiknya tetap fine-grained agar ROI kepala dan perubahan bukti visual bermakna.

## 10. Catatan Sumber dan Literatur

### 10.1 Pembanding Utama

| # | Sumber | Tahun | URL | Relevansi | Konsekuensi bagi novelty |
|---|---|---:|---|---|---|
| 1 | Hooker et al., *What Do Compressed Deep Neural Networks Forget?* | 2020/2021 | https://research.google/pubs/what-do-compressed-deep-neural-networks-forget/ | Dampak kompresi dapat tersembunyi oleh akurasi agregat | Kandidat harus menganalisis perilaku per sampel, bukan hanya accuracy |
| 2 | Liebenwein et al., *Lost in Pruning: The Effects of Pruning Neural Networks beyond Test Accuracy* | 2021 | https://proceedings.mlsys.org/paper_files/paper/2021/hash/521437c574a2bb7fcc20b222700b4181-Abstract.html | Evaluasi pruning di luar test accuracy | Klaim "akurasi tidak cukup" bukan novelty baru |
| 3 | Merkle et al., *Less is More: The Influence of Pruning on the Explainability of CNNs* | 2023/2025 | https://arxiv.org/abs/2302.08878 | Human-grounded perceived explainability pada beberapa compression rate | Menggugurkan klaim pertama tentang pruning dan explainability pada CNN |
| 4 | Demetriou et al., *A Study on the Faithfulness of Feature Attribution Explanations in Pruned Vision-Based Multi-Task Learning* | 2025 | https://ceur-ws.org/Vol-4017/paper_16.pdf | Faithfulness Grad-CAM/IROF pada structured dan unstructured pruning | Menggugurkan novelty umum faithfulness setelah pruning; membuka ekstensi klasifikasi dan multidimensi |
| 5 | Yeom et al., *Pruning by Explaining* | 2021 | https://doi.org/10.1016/j.patcog.2021.107899 | LRP digunakan sebagai kriteria pruning CNN | XAI-guided pruning bukan novelty baru |
| 6 | Yu and Xiang, *X-Pruner: eXplainable Pruning for Vision Transformers* | 2023 | https://openaccess.thecvf.com/content/CVPR2023/html/Yu_X-Pruner_eXplainable_Pruning_for_Vision_Transformers_CVPR_2023_paper.html | Explainability-aware pruning untuk ViT | Jangan mengklaim hubungan explainability--pruning belum pernah diteliti |
| 7 | Bauvin et al., *C-SWAP: Explainability-Aware Structured Pruning* | 2025 | https://bmvc2025.bmva.org/proceedings/850/ | One-shot structured pruning berbasis relasi kausal | Novelty algoritmik membutuhkan pembanding jauh lebih berat dan tidak direkomendasikan |
| 8 | Fang et al., *DepGraph: Towards Any Structural Pruning* | 2023 | https://openaccess.thecvf.com/content/CVPR2023/html/Fang_DepGraph_Towards_Any_Structural_Pruning_CVPR_2023_paper.html | Structured pruning lintas arsitektur dan dasar Torch-Pruning | Dapat menjadi komponen implementasi, bukan kontribusi ilmiah utama |
| 9 | Selvaraju et al., *Grad-CAM* | 2017 | https://openaccess.thecvf.com/content_ICCV_2017/html/Selvaraju_Grad-CAM_Visual_Explanations_ICCV_2017_paper.html | Dasar peta atribusi kelas-spesifik | Metode XAI dasar |
| 10 | Hedström et al., *Quantus* | 2023 | https://jmlr.org/papers/v24/22-0142.html | Toolkit dan taksonomi evaluasi XAI | Integrasi metrik harus disertai protokol penelitian spesifik |
| 11 | Wang and Wang, *Benchmarking Deletion Metrics with the Principled Explanations* | 2024 | https://proceedings.mlr.press/v235/wang24br.html | Kritik dan analisis insertion/deletion metrics | Faithfulness metric tidak boleh diperlakukan tanpa caveat OOD |
| 12 | Parkhi et al., *Cats and Dogs* / Oxford-IIIT Pet | 2012 | https://robots.ox.ac.uk/~vgg/data/pets/ | Dataset klasifikasi fine-grained dengan mask dan ROI kepala | Memungkinkan evaluasi localization tanpa membuat anotasi baru |

### 10.2 Verifikasi Literatur yang Masih Wajib

Sebelum kandidat diterima, pencarian literatur sistematis perlu memeriksa sekurang-kurangnya kombinasi kata kunci berikut pada IEEE Xplore, ACM Digital Library, Scopus/Google Scholar, arXiv, OpenReview, CVF Open Access, dan PMLR:

- `pruning explanation drift image classification`;
- `structured pruning attribution stability Grad-CAM`;
- `pruned model prediction agreement saliency similarity`;
- `model compression XAI faithfulness localization`;
- `accuracy preserving pruning explanation quality`;
- `pruning attribution map object mask localization`;
- `explainability of compressed neural networks benchmark`;
- `channel pruning Integrated Gradients faithfulness`.

Pencarian harus mencatat untuk setiap studi: task, dataset, arsitektur, structured/unstructured pruning, metode pruning, tingkat kompresi, metode XAI, penggunaan prediction agreement, metrik similarity, metrik faithfulness, ground-truth localization, pengukuran hardware, dan ketersediaan kode. Tabel systematic mapping tersebut diperlukan agar novelty tidak hanya bergantung pada perbedaan dataset.

### 10.3 Kesimpulan Gap Sementara

Versi ide yang hanya "membandingkan akurasi sebelum dan sesudah pruning lalu melihat Grad-CAM" memiliki novelty lemah dan tidak direkomendasikan. Versi yang masih layak adalah **analisis perubahan bukti visual pada prediksi yang dipertahankan**, dengan evaluasi berpasangan yang memisahkan drift, faithfulness, serta localization dan menghubungkannya dengan efisiensi inferensi.

### 10.4 Alternatif Jalur YOLO

Jika minat utama sebenarnya adalah YOLO, kandidat harus dirumuskan ulang sebagai:

> evaluasi dampak structured pruning terhadap akurasi deteksi, efisiensi, dan stabilitas penjelasan per-instance pada object detector.

Task, dataset, dan metrik harus diganti menjadi object detection, misalnya mAP, precision/recall, perubahan bounding box, missed detection, dan attribution yang dikondisikan pada pasangan class--box. Jalur ini lebih sulit karena matching antarhasil deteksi dan evaluasi XAI per-instance lebih kompleks. Jalur YOLO tidak disarankan sebagai scope awal satu semester kecuali tersedia GPU, pengalaman object detection, dan dataset domain yang jelas.

## 11. Penyerahan ke Penulisan LaTeX

- **Target file**: `template/proposal/chapters/bab1-pendahuluan.tex`, `template/proposal/chapters/bab2-penelitian-terkait.tex`, dan `template/proposal/chapters/bab3-metodologi.tex` setelah systematic mapping, pilot pruning, dan target komputasi dikunci.
- **Gambar/diagram**: pipeline model padat → structured pruning → fine-tuning → paired prediction audit → XAI → evaluasi drift/faithfulness/localization → profiling → Pareto frontier; matriks eksperimen; dan ilustrasi lima kategori perubahan prediksi.
- **Keputusan yang masih terbuka**: ketersediaan GPU, dua kriteria pruning final, target pengurangan MACs yang realistis, metode XAI kedua, definisi accuracy-preserving region, jumlah seed, dan perangkat CPU target.
- **Syarat sebelum drafting proposal**: pilot satu baseline ResNet-18, satu model terpangkas 50% MACs, validasi mask alignment, pengukuran satu metrik dari tiap dimensi XAI, estimasi waktu seluruh eksperimen, serta systematic mapping terhadap pembanding langsung.
