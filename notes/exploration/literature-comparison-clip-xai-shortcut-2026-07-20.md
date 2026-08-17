# Pembanding Literatur — Cross-modal Attribution + Shortcut Learning untuk CLIP/VLM

Date: 2026-07-20
Target: proposal (Bab 2 Penelitian Terkait)
Status: VERIFIED — verifikasi literatur mandiri selesai. Hasil ini mengikat sebagai pembanding Bab 2 **jika** kandidat CLIP-XAI-Shortcut dipilih; jika topik lain dipilih, file ini tetap sebagai referensi umum tentang landscape XAI CLIP/VLM dan shortcut learning.

## Konteks

Setelah user memilih arah G1+G2 (kombinasi cross-modal attribution untuk CLIP + shortcut learning foundation-vs-supervised), verifikasi independen ke arXiv dilakukan sebelum grilling mendalam. Tiga query dijalankan: "CLIP explainability attribution" (20 hasil), "CLIP interpretability zero-shot" (79 hasil, 50 ditinjau), "foundation model shortcut learning vision" (29 hasil). Total 99 hasil arXiv ditinjau via subagent explore.

## Pembanding Utama (wajib di Bab 2 jika topik dipilih)

### CCI / COVAR — Agarwal, Karanam, Gandhi (Nov 2025, arXiv:2511.12978)

Inti:
- Cluster-based Concept Importance (CCI): masking-based interpretability yang mengelompokkan patch CLIP menjadi cluster semantik lalu mengevaluasi perubahan prediksi.
- SOTA faithfulness (deletion-AUC) untuk MS COCO retrieval, lebih dari 2x lipat dari metode sebelumnya.
- COVAR benchmark: variasi foreground/background sistematis pada 18 varian CLIP.
- Kategori prediksi sebagai foreground-driven atau background-driven via GroundedSAM.

Tumpang tindih dengan kita:
- SUDAH merupakan metode cross-modal attribution untuk CLIP + benchmark spurious correlation.
- SUDAH menguji 18 varian CLIP untuk background over-reliance.
- **TIDAK** membandingkan dengan supervised CNNs atau DINOv2 (hanya varian CLIP).
- **TIDAK** melakukan analisis attribution sebagai diagnostic tool foundation-vs-supervised.

Posisi kita setelah pembanding ini:
- Q1 murni (metode cross-modal attribution baru) SUDAH TIDAK BARU — CCI sudah SOTA.
- Q2 (shortcut foundation-vs-supervised) MASIH ADA GAP — CCI hanya CLIP variants.
- Kombinasi Q1+Q2 (attribution sebagai diagnostic untuk perbandingan foundation-vs-supervised) MASIH TERBUKA.

### exCLIP — Möller et al. (2024, TMLR, arXiv:2408.14153)

Inti:
- Metode second-order attribution untuk CLIP dual encoder; atribusi prediksi similarity ke interaksi fitur antara region gambar dan token caption.
- Menunjukkan CLIP belajar korespondensi fine-grained antara bagian caption dan region gambar.
- Identifikasi failure mode sistematis per kelas objek.

Tumpang tindih:
- Pembanding utama untuk metode cross-modal attribution CLIP.
- Sudah TMLR (venue kredibel).
- Kita bisa rujuk sebagai baseline metode attribution jika topik dipilih.

### EZPC — Ozdemir et al. (CVPR 2026, arXiv:2603.28211)

Inti:
- Proyeksi embedding image-text CLIP ke concept space dari deskripsi bahasa.
- Explanation konsep-level tanpa supervision tambahan, mempertahankan akurasi zero-shot.
- Benchmark: CIFAR-100, CUB-200, Places365, ImageNet-100, ImageNet-1k.

Tumpang tindih:
- Concept-based explanation untuk CLIP zero-shot — angle berbeda dari patch attribution tapi sama-sama menjelaskan zero-shot.
- CVPR 2026 = venue top.

### OSP — Bilgiç et al. (2026, arXiv:2606.14758)

Inti:
- Formalisasi "semantic hallucination" pada XAI VLM (attribution map menyorot anjing bahkan untuk prompt "kucing").
- Linear Semantic Attribution (LSA) framework; OSP sebagai intervensi geometris untuk disentangle unique semantic signals.

Tumpang tindih:
- Sudah mengangkat isu faithfulness/hallucination attribution CLIP — angle metodologis terkait.

## Pembanding Q2 (foundation vs supervised shortcut)

### Marine species — Saleh & Azghadi (Jun 2026, arXiv:2607.02559)

Inti:
- Benchmark DINOv2, CLIP, ResNet-50, EfficientNet-B4 pada cross-habitat marine species recognition.
- Temuan: frozen DINOv2 + linear classifier generalize sebaik fully fine-tuned CNNs; CNN baseline encode habitat-specific shortcuts yang gagal di site baru.
- 10-20 gambar per spesies cukup untuk deploy di site baru.

Tumpang tindih:
- **Paling dekat** dengan "foundation vs supervised shortcut comparison" — tapi:
  - Domain-specific (biologi laut), bukan controlled benchmark.
  - Framing transfer/generalization, bukan shortcut benchmarking.
  - Tidak ada background-swap counterfactuals.
  - Tidak ada attribution analysis.

### Whac-A-Mole — Li et al. (CVPR 2023, arXiv:2212.04825)

Inti:
- Proposes UrbanCars (controlled spurious cues) dan ImageNet-W (watermark shortcut).
- Temuan: "large foundation models — regardless of training set, architecture, supervision — struggle with multiple shortcuts."
- Last Layer Ensemble sebagai mitigasi.

Tumpang tindih:
- Pembanding foundational untuk multi-shortcut di vision models.
- **Tidak** isolasi axis foundation-vs-supervised secara controlled.
- **Tidak** ada cross-modal attribution.

### Debiasing CLIP LTC — Yeo et al. (2025, arXiv:2505.17425)

Inti:
- Identifikasi spurious attention heads di CLIP ViT via mechanistic insights; mitigasi via ablation.
- >50% worst-group accuracy gain pada background/gender bias benchmarks.

Tumpang tindih:
- CLIP spuriosity, mechanistic. Tidak bandingkan dengan supervised CNNs.

### StarFT — Kim et al. (IJCAI 2025, arXiv:2505.13232)

Inti:
- Robust fine-tuning framework mencegah CLIP belajar spuriosity via aligning output distribution.
- +14.3% worst-group accuracy di Waterbirds.

Tumpang tindih:
- CLIP spuriosity mitigation, fine-tuning-focused.

### VLM Robustness Audit — Chengyu et al. (ICPR 2026, arXiv:2604.04473)

Inti:
- Evaluasi CLIP, robust CLIP, BLIP2, SigLIP2 pada typographic attacks, ImageNet-A, natural language-induced adversarial examples.

Tumpang tindih:
- Robustness/shortcut audit VLMs, tapi tidak ada supervised baseline.

## Pembanding Pendukung (metodologis)

### Automated Visual Attribute Reliance — Li et al. (NeurIPS 2025, arXiv:2510.21704)

- Self-reflective agent untuk deteksi visual attribute dependencies di CLIP vision encoder dan YOLOv8.
- Benchmark 130 models dengan 18 kategori attribute dependencies.
- Berbeda paradigma (agent-based) tapi same goal.

### PatchSAE — Lim et al. (ICLR 2025, arXiv:2412.05276)

- Sparse Autoencoder untuk CLIP ViT, ekstraksi patch-level concepts (shape, color, semantics).
- Studi bagaimana prompt-based adaptation remap konsep.

### VL-SAE — Shen et al. (NeurIPS 2025, arXiv:2510.21323)

- SAE untuk CLIP/LLaVA; konsep-level interpretability vision-language alignment.

### TextCAM — Zhao et al. (2025, arXiv:2510.01004)

- CAM + CLIP-derived semantic channel representations; "where + what" explanations.
- Applied to supervised CNNs/ViTs, bukan CLIP zero-shot sendiri.

### Distance Explainer — Meijer & Bos (xAI 2026, arXiv:2505.15516)

- Adaptasi RISE untuk explain distance antara embedded points; evaluasi CLIP cross-modal.
- Faithfulness, Sensitivity, Randomization metrics.

### LaZSL — Chen et al. (ICCV 2025, arXiv:2506.23822)

- Local visual-semantic alignment via optimal transport untuk interpretable zero-shot CLIP.

### Fel et al. (NeurIPS 2024, arXiv:2407.06076)

- V-information-based feature complexity metric; analisis 10.000 fitur ImageNet-trained model.
- Foundational shortcut-learning theory, tapi pada supervised models.

### CLIP Generalization — Mayilvahanan et al. (ICLR 2024, arXiv:2310.09562)

- CLIP OOD performance bukan karena train-test similarity tinggi; properti lain dari training data yang mendorong generalisasi.

## Klaim Kebaruan yang Defensible (setelah verifikasi)

1. **Controlled foundation-vs-supervised shortcut benchmark**: general-domain benchmark sistematis (background swap, texture swap, spurious cues) membandingkan CLIP, DINOv2, ResNet, ViT-supervised — belum ada. Marine species domain-specific; Whac-A-Mole tidak isolasi axis foundation-vs-supervised secara controlled; CCI hanya CLIP variants.

2. **Attribution sebagai diagnostic tool untuk perbandingan foundation-vs-supervised**: menggunakan metode attribution (existing, bukan baru) untuk mendiagnosis *mengapa* foundation vs supervised berbeda shortcut behavior — tidak ada paper yang melakukan ini.

3. **Background-swap counterfactual + attribution agreement analysis**: tidak ada paper yang mengukur apakah cross-modal attribution maps shift appropriately saat background ditukar, membandingkan foundation vs supervised.

4. **DINOv2 attribution + shortcut behavior**: DINOv2 (self-supervised, non-language) nyaris tidak covered untuk attribution. Bisa jadi contrast menarik vs CLIP (cross-modal).

## Klaim yang GUGUR / tidak boleh dipakai

- "Pertama mengusulkan cross-modal attribution untuk CLIP" — CCI, exCLIP, EZPC, OSP, Distance Explainer, LaZSL sudah ada.
- "Pertama menguji shortcut learning di CLIP" — CCI/COVAR, Debiasing-CLIP, StarFT, VLM Robustness Audit sudah ada.
- "Belum ada benchmark shortcut untuk VLM" — COVAR sudah ada (CLIP variants only).
- "Metode XAI baru untuk CLIP" — pure method contribution risiko tinggi tidak baru.

## Verifikasi Q2 mendalam (tambahan, 2026-07-20)

Query tambahan "vision foundation model robustness benchmark supervised" (102 hasil) dianalisis via subagent explore untuk memastikan tidak ada controlled foundation-vs-supervised shortcut + attribution study yang terlewat. Lima paper paling dekat dengan Q2:

### EarthShift — Doerksen & Kerner (Mei 2026, arXiv:2605.29330)
- 8 GFM vs generic VFM vs fully-supervised pada Earth observation, 5 shift types.
- **Distributional robustness, BUKAN shortcut/spurious correlation benchmark.** Shifts = domain transfer nyata, bukan controlled spurious cue.
- Tidak ada attribution. Domain-specific (Earth obs).
- **Tidak membunuh Q2.** Fenomena berbeda (distribution shift vs shortcut).

### FAS VFM Benchmark — Feng et al. (CVPRW 2026, arXiv:2604.19196)
- 15 model: supervised CNNs, supervised ViTs, self-supervised ViTs (termasuk DINOv2 with Registers) pada Face Anti-Spoofing cross-domain.
- Domain generalization benchmark, bukan controlled shortcut.
- **PARTIAL attribution**: attention artifacts suppression sebagai diagnostic signal — tapi tentang attention artifact, bukan shortcut/spurious correlation.
- **Paling dekat secara arsitektural** (CNN vs ViT vs SSL-ViT + attention diagnostic), tapi domain-specific (FAS) dan fenomena berbeda (attention artifact vs shortcut).
- **Tidak membunuh Q2, tapi menyempitkan framing** — thesis harus eksplisit bedakan "shortcut/spurious-correlation behavior" dari "attention artifact suppression" dan generalisasi ke domain umum.

### ShellfishNet — Zhou et al. (Mei 2026, arXiv:2605.07338)
- 80 model (CNN, ViT, SSM, SSL) pada marine molluscs + corruption robustness.
- Recognition + corruption robustness, bukan shortcut benchmark. Tidak ada attribution. Domain-specific.
- **Tidak membunuh Q2.**

### Marine species — Saleh & Azghadi (Jun 2026, arXiv:2607.02559) — sudah dikenal
- DINOv2 vs CLIP vs ResNet vs EfficientNet, 4 adaptation strategies, 928 runs.
- **Bukan controlled shortcut benchmark**, TAPI punya shortcut finding post-hoc: "baselines encoded habitat-specific shortcuts that fail at new sites" vs DINOv2 "habitat-invariant representations."
- Tidak ada attribution — shortcut behavior diinfer dari transfer accuracy gap.
- **Tidak membunuh Q2, tapi menutup klaim "belum ada yang menunjukkan foundation vs supervised shortcut differences."** Thesis tidak bisa klaim pertama; harus reframe sebagai controlled + general-domain + attribution version.

### Whac-A-Mole — Li et al. (CVPR 2023, arXiv:2212.04825) — sudah dikenal
- UrbanCars (controlled spurious cues: background, texture, watermark) + ImageNet-W.
- **INI controlled multi-shortcut benchmark** — ancaman konseptual terbesar.
- Tapi: (a) 2022/2023, predate DINOv2; (b) mitigation-focused, bukan diagnostic/attribution; (c) lump "all vision models including foundation models", tidak isolasi pretraining paradigm sebagai variable; (d) tidak framing sebagai foundation-vs-supervised comparison.
- **Membunuh sebagian**: Q2 tidak bisa klaim "pertama controlled shortcut benchmark yang include foundation models." Harus extend dengan DINOv2/DINOv3 + attribution + foundation-vs-supervised sebagai primary axis.

## Matriks overlap Q2 (verifikasi final)

| Fitur Q2 | EarthShift | FAS Bench | ShellfishNet | Marine 2607 | Whac-A-Mole |
|---|---|---|---|---|---|
| Controlled shortcut/spurious benchmark | ✗ | ✗ | ✗ | ✗ (observasional) | ✓ |
| Foundation vs supervised head-to-head | ~ | ✓ | ✓ | ✓ | ~ (lumped) |
| Attribution/XAI diagnostic | ✗ | ~ (attention artifact) | ✗ | ✗ | ? (mitigation) |
| General-domain | ✗ | ✗ | ✗ | ✗ | ✓ |
| **Semua 4 fitur Q2** | **✗** | **✗** | **✗** | **✗** | **✗** |

**Tidak ada paper yang mengisi keempat fitur Q2 sekaligus.** Kombinasi `{controlled shortcut benchmark} × {foundation-vs-supervised primary axis, modern SSL ViT} × {attribution as diagnostic} × {general-domain}` kosong di literatur yang ditinjau.

## Diferensiasi wajib (untuk survive reviewer yang cite papers di atas)

1. **Controlled + designed shortcut benchmark dengan modern foundation model** (extend Whac-A-Mole ke DINOv2/DINOv3/CLIP/SigLIP — Whac-A-Mole 2022 predate DINOv2).
2. **Foundation-vs-supervised sebagai primary experimental axis** (Whac-A-Mole lump arsitektur; FAS ada tapi domain-specific) — pretraining paradigm sebagai variable, arsitektur/scale dijaga konstan.
3. **Attribution sebagai diagnostic tool** (bukan evaluation) — Grad-CAM/saliency/concept/CAV untuk explain *mengapa* shortcut-reliant, bukan sekadar *that* gagal OOD. **Ini diferensiator terkuat** — tidak ada paper yang melakukan ini di konteks shortcut foundation-vs-supervised.
4. **General-domain** (vs Earth obs, FAS, marine, molluscs yang domain-specific) — ImageNet-derived shortcut (background, texture, watermark, color bias).
5. **Positioning eksplisit vs Whac-A-Mole**: "Whac-A-Mole established multi-shortcut benchmark defeat foundation models (2022), tapi predate DINOv2, mitigation-focused, tanpa attribution, tanpa isolasi pretraining paradigm. We extend with controlled foundation-vs-supervised attribution-diagnostic study."
6. **Positioning eksplisit vs Marine 2607**: cite sebagai evidence observasional yang memotivasi controlled study.

## Posisi Ilmiah Akhir (final, setelah verifikasi Q1 + Q2)

Topik ini **bukan** "metode XAI baru untuk CLIP" (Q1 murni sudah crowded oleh CCI/exCLIP/EZPC/OSP) dan **bukan** "benchmark shortcut CLIP" (CCI/COVAR sudah ada untuk CLIP variants). Topik ini adalah **studi empiris terkontrol** yang menggunakan metode attribution existing sebagai diagnostic tool untuk membandingkan shortcut behavior foundation model (CLIP, DINOv2) vs supervised CNN/ViT pada controlled perturbation benchmark general-domain.

**Kebaruan Q2 DEFENSIBLE** setelah verifikasi mendalam: kombinasi 4 fitur (controlled shortcut + foundation-vs-supervised primary axis + attribution diagnostic + general-domain) kosong di literatur. Anak terbesar: Whac-A-Mole (CVPR 2023) — tapi predate DINOv2, mitigation-focused, tanpa attribution.

Framing jujur dan defensible. Jenis TA: **Ilmiah Akademik** (eksperimen/analisis, bukan produk). Feasibility OK: CLIP ViT-B/32, DINOv2 ViT-S/14, ResNet-50, ViT-S supervised — semua inference CPU, pre-trained open-source, dataset publik (ImageNet, CUB, Waterbirds, ImageNet-W, UrbanCars).

## Catatan Feasibility (di awal, bukan akhir)

- **Hardware OK**: CLIP ViT-B/32, DINOv2 ViT-S/14, ResNet-50, ViT-S supervised — semua inference di CPU 9GB RAM feasible (lambat tapi jalan). Tidak perlu training.
- **Anggaran $0 OK**: model pre-trained open-source (OpenCLIP, DINOv2, torchvision weights). Dataset publik (ImageNet, CUB, Waterbirds, ImageNet-W).
- **Durasi 6 bulan OK**: inference + analisis, tanpa training, feasible untuk S1.
- **Risiko utama**: kompleksitas integrasi multi-model + multi-attribution-method; perlu batasi scope ketat.

## Rekomendasi Posisi

Pilih salah satu dari dua framing:

**Framing A (Ilmiah Akademik, lebih natural)**: "Studi empiris terkontrol: perbandingan shortcut behavior foundation model (CLIP, DINOv2) vs supervised CNN/ViT menggunakan attribution sebagai diagnostic." Tidak ada produk; kontribusi adalah findings + benchmark protocol.

**Framing B (Inovasi Produk, lebih dibungkus)**: "Toolkit audit shortcut untuk vision model: rancang bangun perangkat benchmark + diagnostic attribution untuk membandingkan shortcut behavior foundation vs supervised." Ada produk (toolkit), tapi risiko kontribusi ilmiahnya jadi lebih tipis kalau produk terlalu sederhana.

Framing A lebih jujur ke kontribusi ilmiah dan lebih kecil risiko kebaruan gugur.