# Eksplorasi Topik Website XAI Toolkit

Tanggal: 2026-06-08
Target: proposal dan skripsi

## Ringkasan

Ide: membuat website XAI toolkit tempat pengguna mengunggah model dan data, lalu sistem menghasilkan penjelasan model menggunakan beberapa teknik explainability. Aplikasi ini dapat menampilkan penjelasan lokal, penjelasan global, visualisasi fitur penting, uji perubahan input, dan laporan ringkas tentang perilaku model.

Penilaian jujur: ide ini menarik sebagai Skripsi Inovasi Produk, tetapi jika terlalu umum untuk teks, visi, dan tabel sekaligus, cakupannya terlalu besar dan kebaruannya lemah karena sudah ada toolkit besar seperti Captum, SHAP, InterpretML, Alibi, ExplainerDashboard, What-If Tool, dan Learning Interpretability Tool (LIT). Agar layak, topik perlu dibatasi pada satu atau dua jenis data, format model tertentu, dan kontribusi produk yang jelas.

Rekomendasi utama: mulai dari tabular atau vision saja. Untuk skripsi yang aman, pilih salah satu:
- Tabular-first: website audit XAI untuk model klasifikasi tabular berbasis scikit-learn dengan SHAP, LIME, permutation importance, partial dependence, dan laporan otomatis.
- Vision-first: website XAI untuk model klasifikasi citra berbasis PyTorch/TorchScript atau ONNX dengan Grad-CAM, Integrated Gradients, occlusion sensitivity, dan uji perturbasi citra.

Jika tetap ingin multi-modal, batasi versi awal menjadi dua mode: tabular dan vision. Mode teks sebaiknya menjadi fitur lanjutan karena preprocessing NLP, tokenizer, model transformer, dan format input membuat kompleksitas meningkat cepat.

## Ide Produk

Produk yang dikembangkan adalah website XAI toolkit yang membantu pengguna non-ahli atau pengguna pemula mengevaluasi model machine learning melalui antarmuka unggah model dan data. Sistem menyediakan alur kerja:

1. Pengguna memilih jenis data: tabular atau citra.
2. Pengguna mengunggah model dan dataset uji.
3. Sistem menjalankan prediksi.
4. Sistem menghasilkan penjelasan model.
5. Sistem menampilkan visualisasi dan metrik evaluasi.
6. Sistem membuat laporan interpretabilitas yang dapat diunduh.

Produk tidak perlu membuat algoritma XAI baru. Kebaruannya dapat diletakkan pada integrasi, kemudahan penggunaan, batasan format yang jelas, laporan audit otomatis, dan evaluasi usability.

## Perbandingan dengan Tool yang Sudah Ada

### Captum

Captum adalah library interpretabilitas untuk PyTorch. Captum mendukung banyak metode seperti Integrated Gradients, Saliency, DeepLift, Guided Grad-CAM, Occlusion, LIME, KernelSHAP, LRP, dan TCAV. Captum juga dapat digunakan pada beberapa modalitas, termasuk vision dan text.

Implikasi:
Jika produk hanya membungkus Captum untuk menghasilkan heatmap, kebaruannya lemah. Produk perlu memberi nilai tambah berupa workflow web, validasi input, pemilihan metode otomatis, visualisasi yang mudah dipahami, dan laporan audit.

### SHAP

SHAP adalah library populer untuk menjelaskan output berbagai model machine learning menggunakan pendekatan nilai Shapley. SHAP kuat untuk data tabular, terutama tree-based models, dan menyediakan banyak visualisasi seperti summary plot, force plot, dependence plot, dan waterfall plot.

Implikasi:
Untuk tabular, produk harus lebih dari sekadar memanggil SHAP. Nilai tambah dapat berupa interpretasi otomatis dalam bahasa Indonesia, laporan model card, deteksi fitur dominan, dan panduan membaca hasil.

### LIME

LIME menjelaskan prediksi lokal dengan membuat model surrogate sederhana di sekitar satu sampel. LIME dapat digunakan untuk tabular, teks, dan citra, tetapi hasilnya dapat tidak stabil jika parameter perturbasi tidak dikendalikan.

Implikasi:
Produk dapat menambahkan evaluasi stabilitas LIME, misalnya menjalankan beberapa seed dan melaporkan konsistensi fitur penting.

### InterpretML

InterpretML adalah toolkit untuk memahami model dan mendukung responsible machine learning. InterpretML menyediakan glass-box model seperti Explainable Boosting Machine dan black-box explainers seperti LIME/SHAP, serta visualisasi global dan lokal.

Implikasi:
Produk umum untuk tabular sudah banyak. Kebaruan perlu diarahkan ke kemudahan pemakaian, laporan audit, atau konteks pengguna tertentu.

### Alibi Explain

Alibi Explain menyediakan metode untuk menjelaskan model machine learning, termasuk counterfactual, contrastive explanation, anchors, integrated gradients, dan metode lain. Banyak metode Alibi dapat bekerja dengan model black-box selama tersedia fungsi prediksi.

Implikasi:
Jika ingin model-agnostic, Alibi adalah pembanding penting. Produk skripsi dapat mengambil sudut yang lebih sempit: bukan membuat library XAI baru, tetapi antarmuka audit dan laporan untuk format model tertentu.

### ExplainerDashboard

ExplainerDashboard memungkinkan data scientist membuat web app explainable AI secara cepat, terutama berbasis SHAP untuk model tabular. Tool ini sudah sangat dekat dengan ide dashboard XAI.

Implikasi:
Untuk tabular dashboard, kebaruan harus jelas. Misalnya: fitur upload model + dataset melalui web, laporan bahasa Indonesia, wizard pemilihan metode, validasi format, dan evaluasi usability.

### What-If Tool dan Learning Interpretability Tool (LIT)

What-If Tool dari TensorFlow menyediakan antarmuka visual untuk mengeksplorasi model black-box, mengedit contoh input, dan melihat perubahan prediksi, tetapi dokumentasi TensorFlow menyatakan What-If Tool tidak lagi aktif dipelihara dan mengarahkan pengguna ke LIT. LIT mendukung eksplorasi model melalui antarmuka browser, termasuk local explanation, aggregate analysis, counterfactual generation, slicing, dan side-by-side comparison. Versi terbaru LIT mendukung text, image, dan tabular.

Implikasi:
Ide multi-modal XAI web app sudah ada dalam bentuk LIT. Karena itu, produk skripsi tidak realistis jika diklaim baru sebagai "web XAI multi-modal". Kebaruan harus lebih spesifik, misalnya web XAI ringan untuk pengguna pemula dengan setup upload sederhana, laporan otomatis, atau fokus pada satu domain/model.

## Apakah Ada Kebaruan?

Ada, tetapi bukan pada level "membuat XAI toolkit umum". Kebaruan yang masih masuk akal:

- Membuat XAI toolkit berbasis web yang lebih sederhana untuk pengguna non-ahli.
- Menyediakan workflow upload model dan data tanpa menulis kode.
- Menghasilkan laporan interpretabilitas otomatis dalam bahasa Indonesia.
- Menyediakan rekomendasi metode XAI berdasarkan jenis model dan data.
- Menambahkan evaluasi stabilitas penjelasan, bukan hanya visualisasi.
- Membuat mode edukatif yang menjelaskan cara membaca SHAP, LIME, Grad-CAM, atau Integrated Gradients.
- Membatasi pada format lokal yang jelas, misalnya scikit-learn `.pkl` untuk tabular atau PyTorch/TorchScript/ONNX untuk citra.
- Menyediakan perbandingan beberapa teknik XAI dalam satu alur kerja yang konsisten.

Kebaruan lemah jika:

- Hanya membuat wrapper SHAP/LIME/Captum tanpa fitur audit.
- Membuat dashboard tabular yang mirip ExplainerDashboard.
- Mengklaim mendukung semua model, semua framework, dan semua jenis data.
- Tidak ada evaluasi produk atau pengujian usability.

## Rekomendasi Batasan yang Masuk Akal

### Rekomendasi paling aman: Tabular-first

Judul:
Pengembangan Website Explainable AI untuk Audit Model Klasifikasi Tabular Berbasis Laporan Interpretabilitas Otomatis

Lingkup:
- Jenis data: tabular.
- Tugas model: klasifikasi biner atau multikelas.
- Format model: scikit-learn `.pkl` atau joblib.
- Format data: CSV.
- Metode XAI: SHAP, LIME, permutation importance, partial dependence plot.
- Fitur produk: upload model, upload CSV, pilih target/fitur, prediksi, penjelasan global, penjelasan lokal, laporan PDF/HTML.

Kelebihan:
- Paling mudah diimplementasikan.
- Risiko format input lebih rendah.
- Evaluasi lebih jelas.
- Cocok untuk Skripsi Inovasi Produk.

Kekurangan:
- Kurang sesuai jika minat utamamu Computer Vision.
- Sudah banyak tool sejenis, jadi kebaruan harus ada pada laporan otomatis, UX, dan evaluasi usability.

Tingkat kesulitan: sedang.

### Rekomendasi paling sesuai minat CV x XAI: Vision-first

Judul:
Pengembangan Website Explainable AI untuk Audit Model Klasifikasi Citra Berbasis Peta Atribusi dan Uji Perturbasi

Lingkup:
- Jenis data: citra.
- Tugas model: klasifikasi citra.
- Format model: PyTorch `.pt`/TorchScript atau ONNX.
- Format data: folder citra atau ZIP berisi citra dan label.
- Metode XAI: Grad-CAM, Integrated Gradients, Occlusion Sensitivity, SmoothGrad.
- Fitur produk: upload model, upload citra/dataset, prediksi, heatmap, uji perturbasi brightness/blur/crop/occlusion, skor stabilitas penjelasan, laporan audit.

Kelebihan:
- Lebih dekat dengan minat Computer Vision x XAI.
- Produk lebih visual dan mudah dipamerkan.
- Kebaruan lebih bisa diarahkan ke audit stabilitas penjelasan, bukan sekadar heatmap.

Kekurangan:
- Upload model vision lebih rumit karena arsitektur, preprocessing, ukuran input, normalisasi, class labels, dan dependency.
- Perlu membatasi format model dengan ketat.

Tingkat kesulitan: sedang-tinggi.

### Opsi ambisius: Tabular + Vision

Judul:
Pengembangan Website Multi-modal Explainable AI untuk Interpretasi Model Klasifikasi Tabular dan Citra

Lingkup:
- Jenis data: tabular dan citra.
- Tugas: klasifikasi.
- Format model: scikit-learn untuk tabular dan ONNX untuk vision.
- Metode XAI: SHAP/LIME untuk tabular, Grad-CAM/Integrated Gradients untuk citra.
- Fitur produk: workflow terpisah per modalitas, visualisasi, laporan otomatis.

Kelebihan:
- Terlihat lebih lengkap sebagai produk.
- Bisa menjadi portofolio bagus.

Kekurangan:
- Risiko scope creep tinggi.
- Sulit diuji mendalam.
- Mirip dengan LIT jika klaimnya terlalu umum.

Tingkat kesulitan: tinggi.

### Opsi yang tidak direkomendasikan untuk skripsi awal: Text + Vision + Tabular

Masalah:
- Tiga modalitas sekaligus terlalu luas.
- Text membutuhkan tokenizer, model transformer, attribution token, counterfactual teks, dan interpretasi yang berbeda.
- Vision membutuhkan preprocessing dan model format yang rumit.
- Tabular membutuhkan schema validation dan handling kategori/numerik.
- Produk dapat menjadi dangkal karena semua fitur hanya sedikit-sedikit.

Tingkat kesulitan: sangat tinggi.

Kesimpulan:
Untuk proposal, jangan mulai dari text + vision + tabular sekaligus. Jika ingin tetap multi-modal, pilih tabular + vision saja dan jadikan text sebagai batasan di luar ruang lingkup atau rencana pengembangan.

## Ide Fitur

### Fitur inti

- Registrasi eksperimen atau sesi audit.
- Upload model.
- Upload data uji.
- Validasi format input.
- Inferensi model.
- Visualisasi prediksi.
- Penjelasan global.
- Penjelasan lokal.
- Perbandingan beberapa metode XAI.
- Laporan audit otomatis.

### Fitur tabular

- Feature importance global.
- SHAP summary plot.
- SHAP waterfall untuk satu sampel.
- LIME local explanation.
- Partial dependence plot.
- Counterfactual sederhana dengan perubahan fitur terpilih.
- Deteksi fitur dominan yang terlalu kuat.

### Fitur vision

- Heatmap Grad-CAM.
- Integrated Gradients.
- Occlusion sensitivity.
- SmoothGrad.
- Perturbasi brightness, blur, crop, noise, dan occlusion.
- Skor stabilitas prediksi.
- Skor stabilitas heatmap.
- Perbandingan heatmap antar metode.

### Fitur laporan

- Ringkasan model dan dataset.
- Ringkasan performa.
- Penjelasan global.
- Contoh penjelasan lokal.
- Hasil uji perturbasi.
- Catatan potensi risiko interpretasi.
- Rekomendasi tindak lanjut, misalnya cek data leakage, cek fitur dominan, atau tambah data uji.

## Kemungkinan Jenis TA

### Skripsi Inovasi Produk

Paling cocok jika produk akhirnya berupa website yang bisa digunakan. Luaran utama berupa aplikasi/prototipe XAI toolkit. Bab skripsi dapat membahas identifikasi masalah, ide inovatif, kajian ilmiah XAI, perancangan sistem, implementasi, dan pengujian produk.

Evaluasi produk:
- Pengujian fungsional fitur.
- Pengujian kompatibilitas format model/data.
- Pengujian performa waktu proses.
- Pengujian usability dengan calon pengguna.
- Studi kasus pada 1-2 dataset/model.

### Skripsi Ilmiah Akademik

Cocok jika fokus utamanya membandingkan metode XAI, mengukur stabilitas penjelasan, atau merancang metrik evaluasi interpretabilitas. Produk web bisa menjadi alat bantu, tetapi bukan kontribusi utama.

Evaluasi penelitian:
- Perbandingan metode XAI.
- Analisis stabilitas penjelasan.
- Analisis faithfulness.
- Analisis sensitivitas terhadap perturbasi.

### Proyek Industri

Cocok hanya jika ada mitra yang membutuhkan dashboard audit model, misalnya startup, lab, instansi, atau perusahaan yang memakai model ML. Tanpa mitra, jenis ini tidak relevan.

### Proyek Kolaboratif

Cocok jika dikerjakan bersama pihak lain, misalnya satu mahasiswa fokus frontend/backend, satu mahasiswa fokus model/evaluasi, atau kolaborasi dengan pengguna domain.

## Rekomendasi Akhir

Rekomendasi paling kuat untuk minatmu:

Pengembangan Website Audit Explainable AI untuk Model Klasifikasi Citra Berbasis Peta Atribusi, Uji Perturbasi, dan Laporan Interpretabilitas

Alasan:
- Masih sesuai dengan Computer Vision x XAI.
- Cocok untuk Skripsi Inovasi Produk karena ada alat yang jelas.
- Tidak terlalu dekat dengan Amara et al. (2024) karena domainnya menjadi toolkit umum untuk model citra, bukan hanya ACE pada PlantVillage.
- Kebaruan bisa diletakkan pada uji perturbasi dan laporan audit, bukan sekadar heatmap.
- Lebih realistis daripada membuat toolkit teks, tabel, dan citra sekaligus.
- Lebih menarik daripada tabular karena hasil visualnya mudah dipahami dan dipamerkan saat seminar/pameran produk.

Scope final yang disarankan:
- Hanya klasifikasi citra.
- Hanya model ONNX atau TorchScript, bukan semua model PyTorch bebas.
- Dataset uji berupa ZIP citra dengan file label CSV.
- Metode XAI: Grad-CAM, Integrated Gradients, dan Occlusion Sensitivity.
- Uji perturbasi: brightness, blur, crop, noise, dan occlusion.
- Output: dashboard visual dan laporan audit HTML/PDF.

Formulasi produk yang paling rapi:
Produk ini adalah website yang membantu pengguna mengaudit model klasifikasi citra melalui penjelasan visual dan uji sensitivitas input. Pengguna mengunggah model, metadata preprocessing, daftar label kelas, serta dataset uji. Sistem menjalankan inferensi, menghasilkan peta atribusi, membandingkan hasil beberapa metode XAI, melakukan perturbasi terkontrol pada citra, lalu menyusun laporan interpretabilitas yang menunjukkan stabilitas prediksi dan stabilitas penjelasan.

Kontribusi yang dapat diklaim:
- Integrasi beberapa metode XAI untuk klasifikasi citra dalam satu workflow web.
- Uji perturbasi terkontrol untuk melihat apakah prediksi dan penjelasan berubah drastis akibat perubahan kecil pada input.
- Skor stabilitas prediksi dan stabilitas penjelasan sebagai ringkasan kuantitatif.
- Laporan audit otomatis dalam bahasa Indonesia agar hasil XAI tidak hanya berupa heatmap yang subjektif.
- Antarmuka upload model dan dataset yang lebih sederhana dibandingkan library XAI yang biasanya membutuhkan kode.

Yang sebaiknya tidak diklaim:
- Jangan klaim membuat algoritma XAI baru.
- Jangan klaim mendukung semua jenis model computer vision.
- Jangan klaim hasil explanation selalu benar; XAI tetap perlu diperlakukan sebagai alat bantu audit.
- Jangan klaim sistem dapat menggantikan evaluasi domain expert.

Batasan minimum agar feasible:
- Model hanya untuk klasifikasi citra.
- Format model utama: ONNX. TorchScript boleh menjadi opsional.
- Input model harus satu tensor citra dengan ukuran tetap.
- Dataset uji maksimal dibatasi, misalnya 100-500 citra per sesi audit, agar waktu proses terkendali.
- Label ground truth opsional: jika ada label, sistem tampilkan akurasi/F1; jika tidak ada, sistem hanya tampilkan prediksi dan penjelasan.
- Pengguna wajib mengisi metadata preprocessing: ukuran input, mean, standard deviation, dan daftar label kelas.

Fitur wajib versi proposal:
- Upload model ONNX.
- Upload dataset uji dalam ZIP.
- Konfigurasi preprocessing.
- Prediksi batch.
- Grad-CAM atau metode sejenis yang kompatibel dengan model.
- Integrated Gradients atau Occlusion Sensitivity sebagai pembanding.
- Uji perturbasi brightness, blur, dan occlusion.
- Ringkasan stabilitas prediksi.
- Laporan audit sederhana.

Fitur opsional jika waktu cukup:
- SmoothGrad.
- Side-by-side comparison antar model.
- Ekspor laporan PDF.
- Penyimpanan riwayat audit.
- Segmentasi area objek untuk menghitung rasio heatmap pada objek/latar belakang.
- Rekomendasi otomatis metode XAI berdasarkan tipe model.

Versi yang paling aman untuk implementasi:
Gunakan satu domain studi kasus, misalnya model klasifikasi penyakit tanaman atau klasifikasi objek umum. Tetapi produk jangan terlalu dikunci ke domain itu. Domain dipakai untuk pengujian produk, sedangkan aplikasinya tetap disebut sebagai website audit XAI untuk model klasifikasi citra.

Tingkat kesulitan:
Sedang-tinggi, tetapi masih realistis jika format model dibatasi ke ONNX dan fitur XAI dibatasi ke 2-3 metode. Bagian tersulit bukan dashboard-nya, melainkan kompatibilitas model, preprocessing, dan pemilihan layer/target untuk Grad-CAM. Karena itu perlu desain input metadata yang ketat.

Nilai kebaruan:
Sedang. Bukan kebaruan algoritmik, tetapi kebaruan produk/integrasi. Ini cukup masuk untuk Skripsi Inovasi Produk jika evaluasinya jelas: pengujian fungsional, uji beberapa model, waktu proses, kualitas laporan, dan usability pengguna.

Jika ingin risiko lebih rendah:

Pengembangan Website Explainable AI untuk Audit Model Klasifikasi Tabular Berbasis Laporan Interpretabilitas Otomatis

Ini lebih mudah dan cepat selesai, tetapi kurang sesuai dengan minat Computer Vision.

## Sumber

- Captum, dokumentasi resmi dan API reference. Peran: pembanding library interpretabilitas PyTorch multi-metode dan multi-modalitas. URL: https://captum.ai/api/index.html
- PyTorch Tutorials, "Model Interpretability using Captum". Peran: contoh resmi penggunaan Captum untuk atribusi citra dan teks. URL: https://docs.pytorch.org/tutorials/recipes/recipes/Captum_Recipe.html
- SHAP GitHub. Peran: pembanding library XAI populer berbasis nilai Shapley. URL: https://github.com/shap/shap
- InterpretML. Peran: pembanding toolkit interpretabilitas untuk model glass-box dan black-box. URL: https://interpret.ml/
- Alibi Explain documentation. Peran: pembanding toolkit XAI dengan metode black-box dan counterfactual. URL: https://docs.seldon.ai/alibi-explain/
- ExplainerDashboard documentation. Peran: pembanding web app/dashboard XAI berbasis SHAP. URL: https://explainerdashboard.readthedocs.io/
- TensorFlow What-If Tool documentation. Peran: pembanding dashboard eksplorasi model; juga menunjukkan bahwa WIT tidak lagi aktif dipelihara dan diarahkan ke LIT. URL: https://www.tensorflow.org/tensorboard/what_if_tool
- Learning Interpretability Tool documentation. Peran: pembanding utama untuk web interpretability tool yang mendukung text, image, dan tabular. URL: https://pair-code.github.io/lit/documentation/
- Google Research, "The Language Interpretability Tool: Extensible, Interactive Visualizations and Analysis for NLP Models". Peran: paper pembanding untuk LIT. URL: https://research.google/pubs/the-language-interpretability-tool-extensible-interactive-visualizations-and-analysis-for-nlp-models/
