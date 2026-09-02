# Kelayakan Skripsi: Dampak Efisiensi Model Computer Vision terhadap Performa Prediktif dan Kualitas Penjelasan XAI

**Audiens:** mahasiswa dan pembimbing Skripsi Inovasi Produk UGM  
**Tanggal:** 2 September 2026  
**Cakupan:** single-label image classification; literatur dan dokumentasi yang dapat diverifikasi sampai tanggal laporan  
**Keputusan yang didukung:** memilih fokus kompresi, protokol evaluasi, dataset, model, dan bentuk produk yang realistis untuk satu semester

## 1. Ringkasan eksekutif

### Jawaban langsung

Topik ini **layak dan bernilai akademik**, tetapi hanya setelah dipersempit. Rumusan luas “menguji dampak kompresi model terhadap XAI” tidak lagi cukup novel. Pruning–XAI telah dibahas melalui studi perilaku di luar akurasi, human-grounded explainability, faithfulness pada model pruned, serta metode pruning yang memakai explainability. PTQ–XAI telah diuji langsung pada klasifikasi citra dalam preprint 2026. Knowledge distillation (KD)–XAI bahkan memiliki beberapa pembanding peer-reviewed yang menyelaraskan atau memvisualisasikan penjelasan teacher–student. Early-exit–XAI juga sudah memiliki pembanding langsung pada 2026.

Rekomendasi final adalah:

> **Audit dampak structured channel pruning pada perubahan bukti visual model klasifikasi citra, dengan membandingkan model padat, model segera setelah pruning, dan model setelah fine-tuning/recovery; evaluasi dipisahkan menjadi explanation drift, faithfulness, dan localization; deployment diukur pada CPU konsumen; produk berupa benchmark harness reproducible.**

Pilihan utama: **ResNet-18 + Oxford-IIIT Pet + satu kriteria structured pruning + tiga level pengurangan MACs + Grad-CAM dan Integrated Gradients**. ResNet-50 cukup sebagai ekstensi bila pilot menunjukkan anggaran komputasi aman. Desain inti tidak memasukkan YOLO, object detection, PTQ, KD, low-rank, dan early exit sekaligus.

Kebaruan yang aman bukan algoritmik, melainkan:

- **empiris:** menemukan sampel dan tingkat kompresi ketika akurasi/prediksi masih stabil tetapi penjelasan mulai bergeser;
- **protokol:** evaluasi berpasangan pada kelompok stable-correct, pemisahan drift–faithfulness–localization, serta tiga checkpoint sebelum/sesudah recovery;
- **produk:** harness yang menyimpan lineage model, hasil per sampel, attribution map, konfigurasi, metrik deployment, dan Pareto frontier.

### Peringkat arah penelitian

| Peringkat | Arah | Putusan |
|---|---|---|
| 1 | Structured channel pruning + tiga checkpoint + audit tiga dimensi | **Direkomendasikan**; kompromi terbaik antara feasibility, novelty protokol, dan produk |
| 2 | PTQ INT8 + audit XAI pada artifact deployment | Paling ringan dari sisi kompresi, tetapi novelty melemah dan gradient-XAI pada model INT8 aktual merupakan risiko penting |
| 3 | Low-rank decomposition + audit sebelum/sesudah recovery | Gap empiris paling terbuka, tetapi tuning rank, rekonstruksi layer, dan speedup aktual lebih berisiko |
| 4 | KD teacher–student | Layak, tetapi pembanding e2KD, Exp-KD, XDistillation, dan UniCAM membuat novelty umum lemah |
| 5 | Early exit/dynamic inference | Menarik tetapi routing, layer XAI per exit, dan profiling conditional compute membuat scope tinggi |
| 6 | Lightweight architecture saja | Sangat feasible sebagai baseline deployment, tetapi perbedaan arsitektur menjadi confound dan novelty rendah |
| 7 | Hybrid compression | Tidak direkomendasikan untuk scope inti satu semester |

## 2. “Mengecilkan” bukan selalu “meringankan”

Lima keluaran efisiensi berikut harus diukur terpisah. Tidak ada implikasi otomatis di antara kelimanya.

| Dimensi | Definisi operasional | Penyebab utama | Contoh kegagalan asumsi |
|---|---|---|---|
| Ukuran file | byte artifact/checkpoint yang disimpan | dtype, encoding sparse, metadata, kompresi berkas | bobot bernilai nol tetap tersimpan dalam tensor dense; mask pruning bahkan menambah state |
| RAM/VRAM | peak resident memory saat load/inferensi | bobot, activation, workspace kernel, allocator, batch/input | checkpoint kecil masih membutuhkan activation/workspace besar |
| Parameter | jumlah scalar yang dapat dilatih/disimpan | bentuk arsitektur dan factorization | parameter turun, tetapi activation dan data movement tidak berubah |
| MACs/FLOPs | estimasi operasi aritmetika nominal | bentuk layer, resolusi, kanal, rank | operator ber-MAC rendah dapat lebih lambat karena memory access atau kernel kecil |
| Latensi/throughput | waktu aktual pada runtime dan hardware tertentu | kernel, dtype, fusion, threads, cache, fallback, batch | INT8 dapat lebih lambat pada CPU lama karena quant/dequant overhead |
| Energi | integral daya terhadap waktu, mis. joule/inference | latensi, daya sesaat, data movement, seluruh sistem | inferensi lebih cepat dapat memakai daya lebih tinggi; MACs tidak cukup sebagai proksi |

[ShuffleNet V2](https://openaccess.thecvf.com/content_ECCV_2018/html/Ningning_Light-weight_CNN_Architecture_ECCV_2018_paper.html) menunjukkan bahwa FLOPs bukan proksi langsung kecepatan: memory-access cost, parallelism, platform, dan implementasi operator memengaruhi runtime. Dokumentasi [ONNX Runtime quantization](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html) juga menyatakan speedup INT8 bergantung pada model dan instruksi hardware; quant/dequant overhead dapat membuat hardware lama lebih lambat. Karena itu, skripsi harus melaporkan parameter, MACs, byte artifact, peak RAM, latency batch-1, throughput, dan bila tersedia joule/inference secara terpisah.

## 3. Taksonomi dan proses teknik kompresi

### 3.1 Unstructured pruning

**Yang diubah.** Bobot individual di-nol-kan menurut magnitude, gradient/Taylor, Hessian, atau kriteria lain. Bentuk tensor dan graph biasanya tidak berubah.

**Alur.** Umumnya train -> prune -> fine-tune, sering iteratif; versi one-shot melakukan train -> prune -> evaluate/recover. Tutorial resmi [PyTorch pruning](https://docs.pytorch.org/tutorials/intermediate/pruning_tutorial.html) memakai `weight_orig`, `weight_mask`, dan hook. `prune.remove` menghilangkan reparameterization, tetapi tensor tetap dense berisi nol.

**Dampak.** Sparsity dan jumlah bobot nonzero turun. File/RAM/latency baru turun bila artifact memakai sparse encoding dan runtime memiliki sparse kernel/pattern yang cocok. Pada CPU/GPU umum, sparsity acak moderat sering tidak memberi speedup.

**Kebutuhan.** Implementasi algoritmik mudah, tetapi klaim deployment sulit. XAI berbasis gradien tetap kompatibel selama graph PyTorch differentiable.

**Failure modes.** Mask tidak mengubah ukuran graph; checkpoint dapat membesar; sparsity tidak dieksploitasi; accuracy per kelas/OOD memburuk; recovery mengubah representasi.

**Kelayakan.** 4/5 untuk eksperimen ilmiah, 2/5 untuk produk deployment CPU tanpa sparse runtime khusus. Cocok sebagai baseline, bukan teknik utama bila tujuan produk adalah percepatan nyata.

### 3.2 Structured pruning

**Yang diubah.** Kanal, filter, head, row/column, block, atau layer dihapus sebagai struktur. Dependency graph harus memperbarui layer berikutnya agar bentuk tensor benar-benar mengecil.

**Alur.** Train -> score structures -> prune -> evaluate segera -> fine-tune/recovery -> evaluate. Dapat one-shot atau iteratif. [DepGraph](https://openaccess.thecvf.com/content/CVPR2023/html/Fang_DepGraph_Towards_Any_Structural_Pruning_CVPR_2023_paper.html) merupakan pembanding implementasi penting untuk menangani dependency antarlayer.

**Dampak.** Parameter dan MACs turun; artifact dense mengecil; latensi pada CPU/GPU umum lebih mungkin turun karena operator tetap dense. Speedup tetap tidak linear karena kernel, alignment, memory access, dan layer bottleneck.

**Kebutuhan.** Data training/fine-tuning dan GPU terbatas berguna. ResNet-18 + transfer learning realistis di Colab/satu GPU. Grad-CAM dan IG kompatibel bila target layer semantik dipilih konsisten.

**Failure modes.** Pruning kanal residual yang salah merusak graph; target MACs meleset; extreme pruning menurunkan faithfulness; target layer Grad-CAM berubah resolusinya; recovery memulihkan accuracy tetapi memindahkan fokus.

**Kelayakan.** 4/5. Ini pilihan utama karena memberikan intervention yang jelas, checkpoint sebelum/sesudah recovery, dan deployment artifact yang dapat diukur tanpa sparse kernel khusus.

### 3.3 Post-training quantization (PTQ)

**Yang diubah.** Bobot dan/atau activation FP32 dipetakan ke integer/low-bit melalui scale dan zero-point. Static PTQ memakai calibration set; dynamic PTQ menghitung parameter activation saat inferensi.

**Alur.** Train FP32 -> prepare/calibrate -> convert INT8 -> evaluate/export. Untuk CNN, [ONNX Runtime](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html) merekomendasikan static quantization; dynamic quantization menambah overhead runtime.

**Dampak.** INT8 secara ideal menyimpan bobot sekitar seperempat FP32 dan dapat memperkecil bandwidth/compute. Speedup memerlukan operator, execution provider, dan instruksi INT8 yang didukung. Unsupported operators atau Q/DQ nodes dapat mengurangi manfaat.

**Kebutuhan.** Tidak membutuhkan retraining, tetapi membutuhkan calibration data yang representatif. Implementasi kompresi sangat feasible.

**Failure modes.** Outlier activation, calibration shift, saturation, operator fallback, accuracy/class-specific behavior berubah. Risiko utama bagi topik ini: converted quantized operators biasanya forward-only; Grad-CAM/IG mungkin hanya berjalan pada fake-quant surrogate, bukan artifact deployment INT8. Dokumentasi [torchao QAT](https://docs.pytorch.org/ao/stable/workflows/qat.html) membedakan fake quantization floating-point dari model converted low-bit.

**Kelayakan.** 5/5 untuk kompresi, 3/5 untuk audit gradient-XAI yang benar-benar menjelaskan artifact deployed. Perturbation-based XAI dapat meng-query artifact exact, tetapi lebih mahal.

### 3.4 Quantization-aware training (QAT)

**Yang diubah.** Fake-quant nodes mensimulasikan rounding/clamping selama training/fine-tuning; sesudahnya model dikonversi ke low-bit actual.

**Alur.** Train/initialize FP32 -> prepare QAT -> fine-tune dengan fake quantization -> convert -> export/evaluate.

**Dampak.** Ukuran/runtime ditentukan artifact converted dan backend, bukan graph fake-quant. QAT sering mempertahankan accuracy lebih baik daripada PTQ pada quantization agresif, tetapi membutuhkan data, backward pass, dan tuning.

**Failure modes.** Fake-quant dan runtime INT8 tidak identik; backend/version support berubah; gradient XAI pada fake-quant tidak otomatis faithful terhadap artifact INT8; scope training bertambah.

**Kelayakan.** 3/5 untuk satu semester. Jadikan ekstensi PTQ, bukan bagian wajib.

### 3.5 Knowledge distillation

**Yang diubah.** Arsitektur student yang lebih kecil dilatih mengikuti label dan output/feature/explanation teacher. Tidak ada transformasi mekanis tunggal dari teacher menjadi student.

**Alur.** Train/load teacher -> pilih student -> train student dengan supervised + distillation loss -> evaluate. Inference hanya menjalankan student.

**Dampak.** Ukuran, RAM, MACs, dan latency mengikuti arsitektur student. Training lebih mahal karena teacher forward dan kemungkinan feature/explanation alignment. Dense student umumnya mudah dideploy.

**Failure modes.** Capacity gap, transfer shortcut/bias teacher, prediction agreement rendah, perbedaan arsitektur membuat explanation similarity sulit diinterpretasi.

**Kelayakan.** 3/5. Pembanding langsung sangat padat: [Good Teachers Explain](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09286.pdf), [Exp-KD](https://doi.org/10.1016/j.patcog.2024.111095), [XDistillation](https://arxiv.org/abs/2111.06945), dan [UniCAM](https://openaccess.thecvf.com/content/WACV2025/html/Adhane_On_Explaining_Knowledge_Distillation_Measuring_and_Visualising_the_Knowledge_Transfer_WACV_2025_paper.html) menggugurkan novelty umum teacher–student explanation comparison.

### 3.6 Low-rank matrix/tensor decomposition

**Yang diubah.** Matrix/tensor besar diganti produk faktor ber-rank r; misalnya W(m x n) menjadi A(m x r)B(r x n). Convolution dapat difaktorkan secara spatial/channel/tensor.

**Alur.** Train -> decompose pada beberapa rank -> evaluate segera -> fine-tune/recovery -> evaluate. Alternatifnya rank dipelajari selama training.

**Dampak.** Parameter dan MACs turun bila r cukup kecil. Dua operator kecil dapat menambah kernel launch/data movement; speedup teoritis tidak menjamin latency. [Yu et al. CVPR 2017](https://openaccess.thecvf.com/content_cvpr_2017/html/Yu_On_Compressing_Deep_CVPR_2017_paper.html) dan [Idelbayev & Carreira-Perpinan CVPR 2020](https://openaccess.thecvf.com/content_CVPR_2020/papers/Idelbayev_Low-Rank_Compression_of_Neural_Nets_Learning_the_Rank_of_Each_CVPR_2020_paper.pdf) adalah pembanding kompresi utama, tetapi tidak mengaudit tiga dimensi XAI.

**Failure modes.** Pemilihan layer/rank, error rekonstruksi bertumpuk, graph lebih dalam, latency tidak turun, fine-tuning sensitif.

**Kelayakan.** 3/5. Gap empiris XAI paling terbuka, tetapi absence of evidence bukan bukti “belum pernah.”

### 3.7 Lightweight architecture

**Yang diubah.** Model dirancang efisien sejak awal dengan depthwise convolution, bottleneck, channel shuffle, compound scaling, dan blok hardware-aware. Contoh: [MobileNetV2](https://openaccess.thecvf.com/content_cvpr_2018/html/Sandler_MobileNetV2_Inverted_Residuals_CVPR_2018_paper.html), [EfficientNet](https://proceedings.mlr.press/v97/tan19a.html), dan ShuffleNet V2.

**Alur.** Train/fine-tune arsitektur kecil secara langsung, atau gunakan sebagai student KD.

**Dampak.** Artifact dan MACs biasanya kecil, tetapi operator depthwise dan fragmentasi graph dapat memberi latency berbeda antar-platform.

**Failure modes.** Perbandingan dengan ResNet mencampur compression intervention dan inductive bias arsitektur; resolusi feature map/target Grad-CAM berbeda.

**Kelayakan.** 5/5 sebagai baseline deployment; novelty 1–2/5 sebagai topik utama.

### 3.8 Dynamic inference/early exit

**Yang diubah.** Side classifiers/exit ditambahkan; input mudah berhenti di layer awal menurut confidence/entropy/routing policy. [BranchyNet](https://doi.org/10.1109/ICPR.2016.7900006) adalah dasar klasik.

**Alur.** Train backbone + exits -> calibrate threshold/policy -> infer conditional path -> evaluate per-exit dan agregat.

**Dampak.** Average MACs/latency dapat turun, tetapi worst-case sama atau lebih tinggi karena side-head overhead. Batching GPU dapat mengurangi keuntungan karena divergence.

**Failure modes.** Confidence miscalibration, hard examples selalu ke exit akhir, prediction/explanation berbeda antar-exit, sulit menyamakan target layer. [XAI-Exit](https://doi.org/10.1109/TNNLS.2026.3685408) sudah menggabungkan early exit dan attribution, sehingga novelty umum gugur.

**Kelayakan.** 2–3/5 untuk scope inti.

### 3.9 Hybrid compression

Urutan pruning -> fine-tune -> quantize, QAT + pruning, atau KD -> pruning/quantization dapat menghasilkan artifact lebih efisien, tetapi interaksi teknik membuat causal attribution sulit. [Pruning vs Quantization](https://papers.neurips.cc/paper_files/paper/2023/file/c48bc80aa5d3cbbdd712d1cc107b8319-Paper-Conference.pdf) menunjukkan perbandingan kedua teknik sendiri sudah nontrivial. Untuk satu semester, hybrid hanya layak setelah satu pipeline tunggal selesai dan memiliki fallback.

## 4. Peta literatur kompresi–XAI

| Kelompok | Bukti langsung terkuat | Apa yang sudah diteliti | Gap yang masih defensible |
|---|---|---|---|
| Pruning–XAI | Merkle 2025; Demetriou et al. 2025; Yeom et al. 2021; X-Pruner 2023; C-SWAP 2025 | perceived explainability; IROF faithfulness; XAI sebagai pruning criterion; qualitative maps | paired three-axis audit pada single-label multiclass; stable-correct; pre/post recovery; actual CPU profiling |
| Quantization–XAI | Chung et al. 2025 workshop; Rabbi et al. 2026 preprint; qZACH-ViT 2026 preprint | map drift, deletion/insertion, quantization-aware intrinsic explanation | peer-reviewed multiclass result dengan mask; exact deployed artifact; PTQ vs QAT; calibration sensitivity |
| KD–XAI | Cheng et al. 2020; XDistillation 2021; e2KD 2024; Exp-KD 2025; UniCAM 2025 | knowledge visualization; explanation alignment; localization; teacher–student agreement | independent model-relative faithfulness; stable-correct audit tanpa mengoptimalkan explanations; shortcut inheritance |
| Low-rank–XAI | tidak ditemukan paper langsung yang lengkap | low-rank compression dan low-rank computation of CAM adalah dua hal berbeda | audit drift + faithfulness + localization sebelum/sesudah recovery; gap potensial dengan risiko pencarian |
| Lightweight–XAI | e2KD cross-architecture; benchmark XAI lintas arsitektur | explanation alignment/rankings bergantung arsitektur | deployment baseline; bukan causal compression trajectory |
| Early-exit–XAI | XAI-Exit 2026; attention-consistency preprint 2026 | interpretable routing/exit attribution | rigorous post-hoc three-axis audit per exit dan routing stratum |
| Comparative/hybrid–XAI | Shinde & Sharma 2026 representations; generic compression comparisons | representation degradation, pruning-vs-quantization utility | matched realized latency/bytes dengan XAI tiga dimensi; scope berisiko |

### Pembanding terdekat yang wajib ditempatkan paling awal

1. [What Do Compressed Deep Neural Networks Forget?](https://arxiv.org/abs/1911.05248): accuracy agregat menyembunyikan dampak kelas/sampel; bukan attribution-map study.
2. [Lost in Pruning](https://proceedings.mlsys.org/paper_files/paper/2021/file/521437c574a2bb7fcc20b222700b4181-Paper.pdf): accuracy-only stopping tidak cukup untuk OOD/noise/functional behavior.
3. [Less Is More](https://arxiv.org/abs/2302.08878): pruning + Grad-CAM + 37.500 human tasks; perceived explainability bukan faithfulness.
4. [Faithfulness in Pruned Vision Multi-Task Learning](https://ceur-ws.org/Vol-4017/paper_16.pdf): IROF pada structured/unstructured pruning; task bukan single-label.
5. [Same Predictions, Different Reasons](https://arxiv.org/abs/2607.22872): PTQ INT8/INT4 + Grad-CAM/LIME + similarity + insertion/deletion; novelty killer paling dekat untuk PTQ.
6. [Good Teachers Explain](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09286.pdf): KD yang menyelaraskan explanations, agreement, OOD, dan localization.
7. [Do Coresets, Pruning, and Quantization Preserve Representations?](https://proceedings.mlr.press/v326/shinde26a.html): REPS pada CIFAR-10/ResNet-18; representational similarity bukan XAI faithfulness.

## 5. Tiga dimensi evaluasi XAI

### 5.1 Explanation drift

Pertanyaan estimand: **pada input dan target kelas yang sama, seberapa berubah attribution map model terkompresi terhadap baseline?** Drift mengukur preservasi, bukan otomatis kualitas. Map yang berbeda dapat tetap faithful; map yang mirip dapat sama-sama salah.

Protokol utama:

1. bentuk kelompok **stable-correct**: baseline benar, compressed benar, dan prediksi kelas sama;
2. jelaskan logit target yang sama, idealnya kelas benar/common prediction;
3. simpan strata lain: stable-wrong, correct-to-wrong, wrong-to-correct, changed-wrong;
4. laporkan proporsi strata agar conditioning tidak menyembunyikan failures;
5. hitung distribusi per sampel dan paired bootstrap CI, bukan mean saja.

| Metrik | Kekuatan | Kelemahan | Status rekomendasi |
|---|---|---|---|
| Spearman rank correlation | fokus pada urutan; tahan scaling monotonic | ties dan pixel noise; mengabaikan magnitude | **Primer** setelah normalisasi/flatten konsisten |
| Top-k overlap/Jaccard | mudah menilai perpindahan region paling penting | sensitif k/threshold | **Primer**, laporkan k=5%, 10%, 20% |
| Cosine similarity | mempertahankan pola arah global | sensitif centering/sign; map nonnegative dapat tampak mirip | Sekunder |
| SSIM | menangkap struktur spasial lokal | dirancang untuk natural-image quality; sensitif dynamic range/window | Sekunder/sensitivity analysis |
| RBO | top-weighted ranking overlap | pixel ties dan full fixed ranking membuat interpretasi lemah | Tidak primer; hanya jika unit adalah superpixel/ranked region |

[Sanity Checks for Saliency Maps](https://proceedings.neurips.cc/paper/2018/hash/294a8ed24b1ad22ec2e7efea049b8737-Abstract.html) memakai rank correlation dan SSIM untuk membandingkan peta dan menunjukkan bahwa visual appeal saja dapat menyesatkan. Drift metric harus disertai model-parameter randomization sanity check.

### 5.2 Faithfulness

Pertanyaan estimand: **apakah fitur yang diberi importance tinggi benar-benar mengubah output model yang sedang dijelaskan?** Faithfulness selalu relatif terhadap predictor saat ini, bukan kemiripan dengan baseline/teacher.

| Metrik | Operasi | Interpretasi | Caveat |
|---|---|---|---|
| Deletion AUC | hapus region penting secara progresif | AUC lebih rendah biasanya lebih faithful | masking OOD, baseline dan step size menentukan hasil |
| Insertion AUC | masukkan region penting dari baseline | AUC lebih tinggi biasanya lebih faithful | baseline/inpainting dan ranking confound |
| IROF | hapus superpixel menurut mean relevance | region-level, lebih hemat daripada pixel removal | segmenter dan baseline tetap memengaruhi |
| Faithfulness correlation | korelasikan attribution mass dan output change pada subset acak | tinggi lebih baik | stochastic variance, linearity, OOD |
| Comprehensiveness/sufficiency | remove/retain rationale | necessity/sufficiency | berasal dari NLP; image adaptation sama-sama perturbation-based |

[Benchmarking Deletion Metrics](https://proceedings.mlr.press/v235/wang24br.html) menunjukkan bahwa insertion/deletion harus ditangani hati-hati, termasuk masalah OOD. Mitigasi yang disarankan:

- pra-registrasi unit perturbasi, target score/logit, jumlah step, dan baseline;
- gunakan patch/superpixel, bukan pixel tunggal;
- uji sedikitnya dua baseline, misalnya blur/mean dan ROAD-style imputation;
- sertakan random serta least-relevant controls;
- gunakan protokol identik untuk seluruh model;
- laporkan sensitivitas baseline, bukan memilih baseline terbaik sesudah melihat hasil.

[ROAR](https://papers.nips.cc/paper_files/paper/2019/hash/fe4b8556000d0f0cae99daa5c5c5a410-Abstract.html) mengurangi distribution mismatch dengan retraining, tetapi predictor yang dievaluasi berubah dan biayanya tinggi. [ROAD](https://proceedings.mlr.press/v162/rong22a.html) mengurangi masking confound tanpa retraining, tetapi tetap mendefinisikan intervention tertentu. Tidak ada masking metric yang baseline-free.

### 5.3 Localization/plausibility

Pertanyaan estimand: **apakah attribution berada pada region yang secara eksternal dianggap relevan?** Ini external plausibility, bukan model faithfulness.

| Metrik | Keterangan | Rekomendasi |
|---|---|---|
| Relevance Mass Accuracy / attribution mass in mask | positive attribution di dalam mask dibagi total positive attribution | **Primer** untuk dense mask |
| Energy-Based Pointing Game | pada map nonnegative hampir satu keluarga dengan RMA | Jangan dihitung sebagai bukti independen ganda |
| Pointing Game | apakah pixel maksimum berada di mask/box | Sekunder; sangat kasar |
| Top-k mask overlap | intersection attribution top-k dengan mask | Sekunder; laporkan beberapa k |
| IoU thresholded map | overlap dua mask biner | Sensitif threshold dan luas box; bukan primer tunggal |

Mask segmentation bukan ground truth proses internal. Pada klasifikasi ras, kepala/telinga dapat lebih diskriminatif daripada seluruh tubuh; background juga dapat benar-benar dipakai model. Karena itu, Oxford Pet sebaiknya melaporkan localization pada **trimap seluruh hewan** dan **head ROI** secara terpisah, ditambah random-map/area baseline.

## 6. Analisis novelty arah A–H

| Ide | Status | Bukti yang menggugurkan klaim luas | Reformulasi defensible |
|---|---|---|---|
| A. Pruning + drift + faithfulness + localization | **Sudah diteliti sebagian; gap metodologis** | Merkle; Demetriou; Yeom; X-Pruner; C-SWAP | single-label multiclass, stable-correct, tiga checkpoint, tiga dimensi, actual CPU |
| B. PTQ/QAT + tiga dimensi | **PTQ diteliti langsung sebagian; QAT belum cukup bukti** | Rabbi 2026; Chung 2025; qZACH-ViT | exact artifact vs fake-quant, mask localization, calibration/QAT comparison, deployment parity |
| C. KD teacher–student tiga dimensi | **Sudah diteliti langsung/sebagian; padat** | e2KD, Exp-KD, XDistillation, UniCAM | independent faithfulness per model dan shortcut inheritance; novelty sedang-rendah |
| D. Low-rank + performa/XAI | **Berpotensi novel tetapi berisiko** | paper kompresi low-rank tidak mengaudit XAI; LowRank-CAM bukan compression predictor | tiga-axis audit pada decomposed/recovered model; hindari klaim “pertama” |
| E. Dua teknik pada budget sama | **Gap protokol kuat; scope risk** | pruning-vs-quantization studies memakai utility/representation, bukan paket XAI lengkap | samakan satu budget primer, idealnya measured latency atau bytes; report metrik lain apa adanya |
| F. Baseline–segera compressed–recovered | **Gap metodologis kuat** | studi recovery umum ada, tetapi full paired XAI trajectory tidak ditemukan kuat | jadikan kontribusi protokol inti |
| G. Titik accuracy stabil, XAI turun | **Fenomena sudah ditunjukkan; estimasi breakpoint masih terbuka** | Rabbi 2026; input-compression paper 2026; Merkle sweet spot | definisikan accuracy-preserving region dan breakpoint per dimensi sebelum analisis |
| H. Fine-tuning memulihkan accuracy dengan fokus/shortcut baru | **Belum cukup bukti langsung; menjanjikan** | recovery diketahui mengubah bobot, tetapi bukti compression-XAI lengkap jarang | klaim sebagai audit perubahan, bukan pembuktian shortcut kausal tanpa intervention khusus |

### Jenis novelty

- **Algoritmik:** tidak ditargetkan; sangat sulit karena Yeom, X-Pruner, C-SWAP, e2KD, dan qZACH sudah mengoptimalkan kompresi/explanation.
- **Empiris:** kuat bila menghasilkan paired per-sample evidence dan breakpoint baru pada setting terkontrol.
- **Protokol evaluasi:** paling defensible melalui stable-correct, tiga dimensi, tiga checkpoint, dan deployment metrics terpisah.
- **Produk/benchmark harness:** sangat sesuai Skripsi Inovasi Produk bila reproducible dan bukan sekadar notebook.
- **Dataset-only:** lemah. Mengganti dataset tanpa construct/protocol baru bukan novelty kuat.

## 7. Matriks perbandingan teknik

Skala: feasibility/akademik/novelty/kesesuaian produk 1 rendah–5 tinggi; **beban komputasi dan scope risk 1 rendah–5 tinggi**.

| Teknik | Proses | File | RAM | MACs | Latency CPU | Grad-CAM/IG | Kepadatan prior | F | A | N | Beban | Risk | Produk |
|---|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| Unstructured pruning | train-prune-FT | hanya dengan sparse encoding | tidak otomatis | nonzero teoretis turun | rendah tanpa sparse kernel | baik | tinggi | 4 | 3 | 2 | 3 | 3 | 3 |
| Structured channel pruning | train-prune-eval-FT | turun | cenderung turun | turun | **potensial nyata**, ukur | **baik** | tinggi tetapi audit lengkap jarang | 4 | 5 | 3 | 3 | 3 | 5 |
| Static PTQ INT8 | train-calibrate-convert | **turun ~4x ideal** | cenderung turun | nominal conv sama, bit-op turun | baik pada CPU mendukung | **converted graph berisiko** | direct 2025–26 | 5 | 4 | 2 | 1 | 3 | 4 |
| QAT INT8 | prepare-train-convert | turun | cenderung turun | bit-op turun | backend-dependent | fake-quant baik; artifact risk | sedang/baru | 3 | 4 | 3 | 4 | 4 | 4 |
| KD | teacher-train student | sesuai student | sesuai student | sesuai student | umumnya baik | baik | **sangat padat** | 3 | 4 | 2 | 4 | 4 | 4 |
| Low-rank | train-decompose-eval-FT | turun | dapat turun | turun bila rank tepat | tidak pasti karena extra ops | baik | XAI langsung jarang | 3 | 4 | 4 | 4 | 4 | 4 |
| Lightweight architecture | train/fine-tune kecil | turun | turun | turun | biasanya baik tetapi platform-specific | baik, target layer berbeda | tinggi | 5 | 2 | 1 | 2 | 2 | 4 |
| Early exit | train exits-calibrate route | bisa naik karena heads | bisa naik sedikit | average turun | input/batch-dependent | rumit per exit | direct 2026 | 2 | 4 | 3 | 4 | 5 | 4 |
| Hybrid | beberapa tahap | paling potensial | potensial | potensial | paling backend-dependent | kompleks | tinggi pada efficiency | 2 | 4 | 3 | 5 | 5 | 4 |

## 8. Dataset dan model

### Dataset

| Dataset | Ukuran/anotasi | Lisensi/status | Kesesuaian |
|---|---|---|---|
| **Oxford-IIIT Pet** | 7.349 citra, 37 breed, head ROI, pixel trimap setiap citra | official page menyatakan CC BY-SA 4.0; copyright gambar tetap pemilik | **Terbaik** untuk satu semester dan dual localization construct |
| CUB-200-2011 | 11.788, 200 spesies, box, 15 parts, 312 attributes; segmentations tambahan | non-commercial research/education; overlap ImageNet/Flickr | kaya tetapi lebih berat dan leakage pretraining harus diaudit |
| FGVC-Aircraft | 10.000, 100 variants, box | non-commercial research | realistis, box-only, context correlation |
| PASCAL VOC/Open Images | multilabel scenes, boxes/masks | hak gambar heterogen | kurang cocok sebagai core single-label |

Sumber resmi: [Oxford-IIIT Pet](https://www.robots.ox.ac.uk/~vgg/data/pets/) dan [CUB-200-2011](https://www.vision.caltech.edu/datasets/cub_200_2011/).

### Model

ResNet-18 dipilih sebagai model utama karena graph residual cukup representatif, ukuran training/fine-tuning realistis, target convolutional stage jelas, dan structured pruning memiliki tooling matang. ResNet-50 boleh menjadi validasi ukuran keluarga bila komputasi tersedia.

Membandingkan ResNet-50 teacher dengan MobileNetV2 student mencampur teknik KD, kapasitas, operator, receptive field, feature-map resolution, dan inductive bias. Explanation drift lintas arsitektur tidak dapat diinterpretasikan sebagai efek kompresi tunggal. Jika dipakai, framing-nya harus “teacher–student functional transfer,” bukan before/after compression yang identik.

## 9. Tiga kandidat penelitian

### Kandidat 1 — paling feasible: audit PTQ INT8 pada artifact deployment

**Judul Indonesia:** *Audit Performa, Pergeseran Penjelasan, dan Lokalisasi Model Klasifikasi Citra Terkuantisasi pada CPU Konsumen*  
**Judul Inggris:** *Auditing Predictive Performance, Explanation Drift, and Localization of Quantized Image Classifiers on Consumer CPUs*

**Masalah.** PTQ mudah mengecilkan artifact dan dapat mempercepat CPU, tetapi accuracy tidak menjamin explanation preservation; gradient-XAI mungkin tidak berjalan pada graph INT8 actual.

**RQ.** (1) Bagaimana INT8 PTQ mengubah accuracy/agreement dan latency? (2) Pada stable-correct, apakah attribution exact-deployment drift? (3) Apakah faithfulness dan localization berubah? (4) Seberapa berbeda fake-quant surrogate dari artifact actual?

**Hipotesis.** INT8 mempertahankan accuracy lebih baik daripada map similarity; efek bergantung arsitektur/calibration; perturbation-XAI pada artifact dapat mendeteksi drift yang tidak terlihat dari accuracy.

**Kontribusi aman.** Audit multiclass dengan mask, deployment parity, dan protokol per sampel; bukan paper pertama quantization–XAI.

**Pembanding.** Rabbi et al. 2026; Chung et al. 2025; qZACH-ViT 2026. Perbedaan: Oxford Pet 37 kelas, mask/ROI, exact CPU artifact, calibration sensitivity, stable-correct.

**Desain.** ResNet-18; Oxford Pet; FP32 + static PTQ INT8 dengan MinMax/Entropy/Percentile atau dua calibration sizes; XAI utama perturbation-based (RISE/LIME) pada artifact; Grad-CAM/IG hanya bila exact graph mendukung backward, atau dilabeli jelas sebagai surrogate analysis. Predictive: accuracy, macro-F1, NLL/ECE, agreement. XAI: Spearman/top-k, deletion/insertion atau ROAD, RMA/head-ROI. Deployment: bytes, peak RSS, batch-1 median/p95, throughput, optional joule/inference.

**Varian.** 4–7 artifact; tanpa multi-seed training bila baseline checkpoint sama, tetapi ulang calibration/bootstrap.  
**Hardware.** Tanpa GPU memungkinkan; CPU dengan instruksi INT8 lebih baik.  
**Risiko.** Gradient-XAI incompatibility dan novelty preprint 2026.  
**Fallback.** Batasi INT8 static, gunakan black-box XAI, dan jadikan gradient parity sebagai limitation.  
**Batas klaim.** Hanya backend/hardware/version yang diuji.  
**Produk.** Export-and-audit harness untuk FP32/INT8.

### Kandidat 2 — novelty paling kuat: low-rank decomposition tiga checkpoint

**Judul Indonesia:** *Audit Perubahan Performa dan Penjelasan XAI pada Kompresi Low-Rank Model Klasifikasi Citra*  
**Judul Inggris:** *Auditing Predictive and XAI Explanation Changes under Low-Rank Compression of Image Classifiers*

**Masalah.** Low-rank mengurangi parameter/MACs, tetapi efek terhadap bukti visual dan pemulihan sesudah fine-tuning belum memiliki bukti langsung yang padat.

**RQ.** Bagaimana rank memengaruhi accuracy, latency, drift, faithfulness, dan localization sebelum/sesudah recovery? Apakah recovery memulihkan prediction melalui fokus visual yang berbeda?

**Hipotesis.** Moderate rank reduction mempertahankan accuracy, tetapi decomposition segera meningkatkan drift; recovery memulihkan accuracy lebih cepat daripada localization/faithfulness.

**Kontribusi aman.** Studi empiris/protokol pada gap yang jarang, bukan algoritma factorization baru dan bukan klaim “pertama.”

**Pembanding.** Yu et al. 2017 dan Idelbayev & Carreira-Perpinan 2020 untuk compression; tidak mengaudit XAI. LowRank-CAM tidak relevan karena mengompresi perhitungan explanation, bukan predictor.

**Desain.** ResNet-18; factorize subset Conv/FC yang pra-registrasi; ranks yang menargetkan 25/50/70% MAC reduction; checkpoint baseline, decomposed-immediate, recovered; Grad-CAM + IG; metric suite sama dengan rekomendasi.

**Varian.** 1 + 3 immediate + 3 recovered = 7 per seed; 3 seed ideal (21).  
**Hardware.** Satu GPU memadai; Colab mungkin dengan satu seed/pilot.  
**Risiko.** Rank allocation, graph engineering, dan latency tidak turun.  
**Fallback.** Factorize hanya layer 3–4/FC dan gunakan dua rank; jadikan parameter/MACs sebagai efficiency utama bila latency gagal, dengan klaim terbatas.  
**Produk.** Low-rank model lineage and XAI audit harness.

### Kandidat 3 — kompromi terbaik dan rekomendasi final: structured pruning recovery audit

**Judul Indonesia:** *Evaluasi Pergeseran, Faithfulness, dan Lokalisasi Penjelasan XAI pada Model Klasifikasi Citra yang Mengalami Structured Pruning*  
**Judul Inggris:** *Evaluating Explanation Drift, Faithfulness, and Localization in Structurally Pruned Image Classifiers*

**Masalah.** Structured pruning dapat menghasilkan model dense yang lebih kecil dan cepat, tetapi accuracy-only selection dapat melewatkan perubahan bukti visual; recovery dapat mengubah fokus.

**RQ.** (1) Bagaimana level pruning memengaruhi accuracy, agreement, MACs, latency, dan memory? (2) Pada stable-correct, kapan drift meningkat? (3) Apakah faithfulness/localization menurun di accuracy-preserving region? (4) Apakah recovery memulihkan metrik prediktif dan XAI dengan laju sama?

**Hipotesis.** Ada region pruning moderat dengan accuracy stabil tetapi drift meningkat; extreme pruning menurunkan faithfulness/localization; recovery memulihkan accuracy lebih cepat daripada seluruh dimensi XAI.

**Kontribusi aman.** Paired three-axis, recovery-trajectory, per-sample deployment audit; bukan pruning/XAI algorithm baru.

**Pembanding.** Merkle 2025; Demetriou 2025; Yeom 2021; X-Pruner 2023; C-SWAP 2025. Perbedaan: single-label multiclass, stable-correct, mask + head ROI, three checkpoints, actual CPU.

**Model/dataset.** ResNet-18 utama; Oxford Pet 37 kelas; ResNet-50 opsional. Satu kriteria channel importance (L1/L2 norm) sebagai inti; Taylor hanya ekstensi setelah pilot.

**Level.** target pengurangan MACs 25%, 50%, 70%; target disesuaikan pilot agar tidak menghasilkan graph invalid.  
**XAI.** Grad-CAM + Integrated Gradients.  
**Prediktif.** top-1, macro-F1, NLL, ECE, per-class recall, agreement.  
**XAI.** Spearman/top-k/SSIM sekunder; deletion/IROF/ROAD sensitivity; RMA + Pointing Game; randomization sanity check.  
**Deployment.** params, MACs, bytes ONNX/TorchScript, peak RSS, load time, median/p95 latency batch-1, throughput, optional joule/inference.

**Desain.** Baseline -> prune level -> immediate evaluation -> fixed-budget recovery -> evaluation. Hasil per sample disimpan sebagai Parquet/JSONL; paired bootstrap CI dan effect size; accuracy-preserving region dipraregistrasi, misalnya <=1 pp absolute accuracy drop.

**Varian.** 7 model per seed; 3 seeds ideal = 21. Minimum defensible: satu seed training yang dikunci + bootstrap per sampel, dengan klaim generalisasi terbatas.  
**Hardware.** Colab/satu GPU memadai.  
**Risiko.** 70% MACs gagal, Grad-CAM target layer berubah, eksperimen 3 seed mahal.  
**Fallback.** ResNet-18 saja, level 25/50%, Grad-CAM full test + IG stratified subset, satu importance criterion.  
**Batas klaim.** Tidak membuktikan reasoning kausal, tidak menggeneralisasi ke semua pruner/hardware.  
**Produk.** CLI/config-driven benchmark harness dengan model lineage, profiler, metric registry, artifact cache, dan report generator.

## 10. Rekomendasi final dan alasan

Pilih **Kandidat 3: structured channel pruning recovery audit**.

Alasannya:

1. artifact hasil pruning tetap dense dan lebih mudah memberi speedup pada CPU umum daripada unstructured masks;
2. Grad-CAM/IG tetap dapat dihitung pada model actual, berbeda dari risiko graph quantized;
3. tiga checkpoint menyediakan intervention yang jelas untuk menilai kerusakan langsung dan efek recovery;
4. Oxford Pet memberi label klasifikasi, dense foreground mask, dan head ROI dalam dataset kecil berlisensi jelas;
5. novelty luas memang gugur, tetapi kombinasi stable-correct + tiga dimensi + recovery trajectory + actual deployment masih merupakan gap protokol yang defensible;
6. harness audit sesuai struktur Skripsi Inovasi Produk UGM: masalah nyata, rancangan produk, implementasi, pengujian, evaluasi.

Low-rank menjadi pilihan kedua bila pembimbing memprioritaskan novelty dan GPU tersedia. PTQ menjadi fallback tanpa GPU, dengan konsekuensi harus memakai black-box/perturbation XAI untuk artifact actual atau membatasi klaim surrogate.

## 11. Pilot terkecil

Pilot harus selesai sebelum judul final dikunci.

| Komponen | Minimum pilot |
|---|---|
| Dataset | Oxford Pet split resmi; verifikasi transform mask pada 20 citra |
| Model | ResNet-18 transfer learning, satu seed |
| Compression | baseline; structured pruning target 50% MACs; immediate; recovery 5–10 epoch |
| Sampel XAI | Grad-CAM 256 test images; IG pada 64 stable-correct stratified images |
| Drift | Spearman + top-10% Jaccard; target class sama |
| Faithfulness | deletion 20 steps dengan blur; random/least-relevant control; ROAD bila tersedia |
| Localization | RMA pada trimap dan head ROI; Pointing Game sekunder |
| Deployment | warm-up, thread count tetap, >=1000 batch-1 repeats; median/p95; peak RSS; artifact bytes |
| Output | satu Parquet/JSONL per sampel, config, hashes, 12 contoh audit visual, Pareto mini-report |

Kriteria go/no-go:

- physical pruning benar-benar mengubah tensor shape dan MACs;
- model dapat diekspor dan latency terukur stabil (CV rendah setelah warm-up);
- sedikitnya sekitar 150 stable-correct images tersedia untuk paired pilot;
- mask alignment benar pada audit visual;
- semua tahap selesai dalam anggaran komputasi yang dapat dikalikan ke eksperimen penuh;
- tidak ada silent mismatch antara target logit/model/layer XAI.

## 12. Rekomendasi berdasarkan hardware

| Kondisi | Rekomendasi |
|---|---|
| Tanpa GPU | PTQ INT8 + black-box XAI exact artifact; atau gunakan pretrained/frozen baseline dan pilot structured pruning tanpa full retraining; scope satu model |
| GPU terbatas/Colab | **ResNet-18 structured pruning**, 2–3 levels, fixed recovery budget, Grad-CAM full + IG subset |
| Satu GPU memadai | desain rekomendasi 3 levels x 3 seeds; tambah ResNet-50 hanya setelah ResNet-18 lengkap; atau pilih low-rank untuk novelty lebih tinggi |

## 13. Risiko dan fallback

| Risiko | Dampak | Mitigasi/fallback |
|---|---|---|
| Novelty dikalahkan paper baru | klaim utama lemah | framing kontribusi protokol/produk; literature update sebelum proposal final |
| Metric OOD/masking | faithfulness misleading | dua baseline, ROAD/random control, sensitivity report |
| Stable-correct selection bias | failures tersembunyi | laporkan semua strata dan counts; drift utama tetap stable-correct |
| Mask bukan ground truth reasoning | overclaim localization | sebut plausibility; trimap/head ROI terpisah; random-area baseline |
| CPU latency noisy | perbandingan tidak stabil | lock threads/power, warm-up, repeated timing, median/p95, hardware metadata |
| Recovery compute tinggi | eksperimen tidak selesai | ResNet-18 saja, dua level, satu criterion, fixed short recovery |
| IG terlalu mahal | evaluasi tertunda | subset stratified pra-registrasi; Grad-CAM full |
| Pruning graph gagal | artifact invalid | gunakan dependency-aware library; audit tensor shapes/export di pilot |
| Hasil null | kontribusi dianggap lemah | null yang ketat tetap bernilai: batas equivalence/CI, product validation, per-sample failure taxonomy |
| Scope creep | tidak selesai | larang penambahan YOLO/dataset/technique sebelum core matrix selesai |

## 14. Daftar sumber beranotasi

1. **Hooker et al. — What Do Compressed Deep Neural Networks Forget?** Preprint, 2019–2021. [Paper](https://arxiv.org/abs/1911.05248). Menunjukkan aggregate accuracy menyembunyikan dampak kelas/sampel dan Pruning Identified Exemplars. Bukan XAI-map study.
2. **Liebenwein et al. — Lost in Pruning.** MLSys 2021, peer-reviewed. [Paper](https://proceedings.mlsys.org/paper_files/paper/2021/file/521437c574a2bb7fcc20b222700b4181-Paper.pdf). Pruning harus dinilai pada functional/OOD/noise metrics, bukan accuracy saja.
3. **Merkle et al. — Less Is More.** IEEE Access 2025, peer-reviewed; [preprint](https://arxiv.org/abs/2302.08878). VGG16/Imagenette, iterative unstructured pruning, Grad-CAM, 37.500 human tasks; perceived explainability berbeda dari decision utility/faithfulness.
4. **Demetriou et al. — Faithfulness of Feature Attribution in Pruned Vision MTL.** xAI 2025 late-breaking workshop. [Paper](https://ceur-ws.org/Vol-4017/paper_16.pdf). IROF pada structured/unstructured pruning; bukan single-label classification.
5. **Yeom et al. — Pruning by Explaining.** Pattern Recognition 2021. [First-party page](https://research.google/pubs/pruning-by-explaining-a-novel-criterion-for-deep-neural-network-pruning/). LRP dipakai sebagai pruning criterion; bukan post-compression input-attribution audit.
6. **Yu & Xiang — X-Pruner.** CVPR 2023. [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Yu_X-Pruner_eXplainable_Pruning_for_Vision_Transformers_CVPR_2023_paper.html). Explainability-aware masks untuk structured ViT pruning; map evidence terutama kualitatif.
7. **Bauvin et al. — C-SWAP.** BMVC 2025. [Paper](https://bmva-archive.org.uk/bmvc/2025/assets/papers/Paper_850/paper.pdf). Causal-aware one-shot structured pruning tanpa fine-tuning; sangat dekat untuk novelty algorithmic.
8. **Rabbi et al. — Same Predictions, Different Reasons.** arXiv preprint, Juli 2026. [Paper](https://arxiv.org/abs/2607.22872). PTQ INT8/INT4, Grad-CAM/LIME, similarity dan deletion/insertion; direct novelty killer untuk PTQ–XAI, tetapi dua dataset biner kecil dan tanpa hardware profiling.
9. **Chung et al. — Understanding the Impact of Quantization on Model Explainability.** HCAI/CIKM workshop 2025. [Paper](https://xai.kaist.ac.kr/static/files/2025_hcai_workshop/paper_33.pdf). Preliminary evidence pada Grad-CAM, IG, dan LRP.
10. **Parchami-Araghi et al. — Good Teachers Explain.** ECCV 2024. [Paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09286.pdf). Explanation-enhanced KD meningkatkan agreement, OOD, dan localization; generic KD–explanation alignment bukan novelty.
11. **Sun et al. — Explainability-based Knowledge Distillation.** Pattern Recognition 2025. [DOI](https://doi.org/10.1016/j.patcog.2024.111095). CAM alignment sebagai knowledge; audit terikat algoritma baru.
12. **Adhane et al. — On Explaining Knowledge Distillation.** WACV 2025. [Paper](https://openaccess.thecvf.com/content/WACV2025/html/Adhane_On_Explaining_Knowledge_Distillation_Measuring_and_Visualising_the_Knowledge_Transfer_WACV_2025_paper.html). UniCAM/FSS/RS memvisualisasikan distilled/residual features; bukan standard faithfulness/localization audit.
13. **Cheng et al. — Explaining KD by Quantifying the Knowledge.** CVPR 2020. [Paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Cheng_Explaining_Knowledge_Distillation_by_Quantifying_the_Knowledge_CVPR_2020_paper.html). Menganalisis visual concepts dan optimization stability dalam KD.
14. **Shinde & Sharma — Do Coresets, Pruning, and Quantization Preserve Representations?** GRaM/PMLR workshop 2026. [Paper](https://proceedings.mlr.press/v326/shinde26a.html). REPS pada CIFAR-10/ResNet-18; representation similarity bukan explanation faithfulness.
15. **Hedström et al. — Quantus.** JMLR 2023. [Paper](https://jmlr.org/papers/v24/22-0142.html). Toolkit/taksonomi >35 metrics; library availability bukan validasi konstruk.
16. **Adebayo et al. — Sanity Checks for Saliency Maps.** NeurIPS 2018. [Paper](https://proceedings.neurips.cc/paper/2018/hash/294a8ed24b1ad22ec2e7efea049b8737-Abstract.html). Beberapa saliency methods tidak sensitif pada model/data; randomization checks wajib.
17. **Wang & Wang — Benchmarking Deletion Metrics with Principled Explanations.** ICML 2024. [Paper](https://proceedings.mlr.press/v235/wang24br.html). Membahas OOD dan failure modes insertion/deletion.
18. **Hooker et al. — ROAR benchmark.** NeurIPS 2019. [Paper](https://papers.nips.cc/paper_files/paper/2019/hash/fe4b8556000d0f0cae99daa5c5c5a410-Abstract.html). Remove-and-retrain menangani distribution mismatch tetapi mengganti predictor dan mahal.
19. **Rong et al. — ROAD.** ICML 2022. [Paper](https://proceedings.mlr.press/v162/rong22a.html). Removal/debias tanpa retraining; mengurangi leakage confound.
20. **Selvaraju et al. — Grad-CAM.** ICCV 2017. [Paper](https://openaccess.thecvf.com/content_ICCV_2017/html/Selvaraju_Grad-CAM_Visual_Explanations_ICCV_2017_paper.html). Dasar class-discriminative localization; coarse map dan layer choice harus dilaporkan.
21. **Parkhi et al. — Oxford-IIIT Pet.** CVPR 2012; [dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/). 37 breed, head ROI, trimap; pilihan utama.
22. **Wah et al. — CUB-200-2011.** Caltech technical report/dataset; [official page](https://www.vision.caltech.edu/datasets/cub_200_2011/). Rich annotations, tetapi non-commercial dan overlap pretraining.
23. **Ma et al. — ShuffleNet V2.** ECCV 2018. [Paper](https://openaccess.thecvf.com/content_ECCV_2018/html/Ningning_Light-weight_CNN_Architecture_ECCV_2018_paper.html). Bukti primer bahwa FLOPs dan latency tidak ekuivalen.
24. **ONNX Runtime — Quantize ONNX Models.** Dokumentasi resmi, diakses 2026-09-02. [Docs](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html). Static/dynamic PTQ, data types, backend caveats, dan failure to speed up.
25. **PyTorch/torchao — QAT Workflow.** Dokumentasi resmi, 2026. [Docs](https://docs.pytorch.org/ao/stable/workflows/qat.html). Fake-quant prepare/train/convert dan support constraints.
26. **Yu et al. — Low Rank and Sparse Decomposition.** CVPR 2017. [Paper](https://openaccess.thecvf.com/content_cvpr_2017/html/Yu_On_Compressing_Deep_CVPR_2017_paper.html). Compression baseline; tidak mengaudit XAI.
27. **Idelbayev & Carreira-Perpinan — Learning Rank of Each Layer.** CVPR 2020. [Paper](https://openaccess.thecvf.com/content_CVPR_2020/papers/Idelbayev_Low-Rank_Compression_of_Neural_Nets_Learning_the_Rank_of_Each_CVPR_2020_paper.pdf). Low-rank baseline dan rank learning; tidak mengaudit attribution.
28. **Teerapittayanon et al. — BranchyNet.** ICPR 2016. [DOI](https://doi.org/10.1109/ICPR.2016.7900006). Early-exit foundation.
29. **Rahmath et al. — XAI-Exit.** IEEE TNNLS 2026. [DOI](https://doi.org/10.1109/TNNLS.2026.3685408). Early exit dengan attribution trajectories; novelty killer untuk framing umum.
30. **Kuzmin et al. — Pruning vs Quantization: Which Is Better?** NeurIPS 2023. [Paper](https://papers.neurips.cc/paper_files/paper/2023/file/c48bc80aa5d3cbbdd712d1cc107b8319-Paper-Conference.pdf). Menunjukkan matched compression comparison sendiri kompleks dan budget definition penting.

## Lampiran A. Claim-to-source ledger dan gap matrix

| Klaim material | Bukti utama | Confidence | Kontradiksi/batas | Gap berikutnya |
|---|---|---|---|---|
| Accuracy tidak menjamin perilaku sama | Hooker; Liebenwein; Rabbi | tinggi | behavior, explanation, representation adalah construct berbeda | paired per-sample audit |
| Pruning–XAI bukan novelty umum | Merkle; Demetriou; Yeom; X-Pruner; C-SWAP | tinggi | sebagian bukan single-label atau bukan posthoc audit | three-axis recovery protocol |
| PTQ dapat mengubah explanation saat prediction sama | Rabbi 2026 | sedang–tinggi | preprint, dataset kecil, reproducibility wording PTQ tidak konsisten | multiclass/mask/exact backend replication |
| KD explanation alignment sudah padat | e2KD; Exp-KD; XDistillation; UniCAM | tinggi | alignment bukan faithfulness | independent model-relative audit |
| Low-rank–XAI direct evidence jarang | targeted search + compression originals | sedang | absence search tidak membuktikan nonexistence | literature update sebelum klaim novelty |
| FLOPs tidak sama latency | ShuffleNet V2; ONNX docs | tinggi | hasil hardware-specific | measure target CPU |
| Gradient XAI pada INT8 artifact berisiko | torchao docs + converted operator behavior | tinggi | support dapat berubah menurut backend/version | local pilot exact graph |
| Localization bukan faithfulness | Quantus taxonomy; CLEVR-XAI/RMA family | tinggi | external mask tetap berguna untuk plausibility | report constructs separately |

### Catatan metode pencarian dan alasan berhenti

Pencarian dilakukan secara bertahap pada exact seed titles, pasangan istilah compression–XAI, venue primer (CVF/PMLR/JMLR/OpenReview/IEEE/ACM/arXiv), dokumentasi framework/runtime resmi, dan situs dataset resmi. Gelombang kedua menargetkan pembanding yang dapat menggugurkan novelty: explanation-aware pruning/KD, PTQ explanation drift 2025–2026, early-exit XAI, low-rank direct audit, matched-budget comparison, serta fine-tuning recovery. Pencarian dihentikan ketika setiap teknik memiliki pembanding/gap yang dapat dinilai, klaim deployment memiliki sumber resmi, konflik metric OOD dan quantized-gradient telah dibatasi, dan tambahan hasil berulang tidak mengubah peringkat rekomendasi. Gap yang tetap tidak pasti dinyatakan eksplisit, terutama absence of direct low-rank–XAI study dan exact backward support pada backend quantization yang akan dipilih.
