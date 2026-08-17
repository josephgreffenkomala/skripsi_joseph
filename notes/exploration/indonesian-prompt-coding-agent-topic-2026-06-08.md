# Pengaruh Bahasa Instruksi terhadap Kinerja Coding Agent

Date: 2026-06-08
Target: proposal

## Summary

Topik yang disarankan adalah mengevaluasi apakah instruksi tugas perangkat lunak dalam Bahasa Indonesia menurunkan kemampuan LLM-based coding agent dibanding instruksi ekuivalen dalam Bahasa Inggris. Agar memiliki kontribusi inovasi produk, penelitian tidak berhenti pada evaluasi, tetapi membangun benchmark dan middleware mitigasi yang menerjemahkan atau menormalisasi instruksi Indonesia sebelum agent bekerja.

## Recommended Title

**Bahasa Indonesia**

Evaluasi dan Mitigasi Kesenjangan Kinerja Coding Agent pada Instruksi Bahasa Indonesia dan Bahasa Inggris

**English**

Evaluating and Mitigating the Performance Gap of Coding Agents under Indonesian and English Instructions

## Research Gap

Penelitian multilingual code generation seperti HumanEval-XL dan mHumanEval telah menguji pengaruh bahasa natural pada pembuatan fungsi. Namun, tugas tersebut bersifat single-turn dan function-level.

Benchmark agent seperti SWE-bench, Multi-SWE-bench, dan SWE-PolyBench mengevaluasi penyelesaian issue pada repositori nyata. Akan tetapi, istilah "multilingual" pada Multi-SWE-bench dan SWE-PolyBench merujuk terutama pada bahasa pemrograman, bukan bahasa natural instruksi pengguna.

Dengan demikian, ruang riset yang layak adalah pengaruh Bahasa Indonesia pada coding agent repository-level yang harus:

- memahami issue;
- menelusuri repositori;
- menggunakan terminal dan alat;
- membaca pesan error berbahasa Inggris;
- membuat serta merevisi patch;
- memenuhi test suite.

## Initial Evidence

mHumanEval melaporkan Pass@1 untuk prompt Bahasa Inggris dan Indonesia pada tugas Python yang sama:

| Model | Inggris | Indonesia | Selisih |
|---|---:|---:|---:|
| Claude 3.5 | 0.938 | 0.849 | -0.089 |
| GPT-4o | 0.910 | 0.809 | -0.101 |
| GPT-3.5 | 0.770 | 0.478 | -0.292 |
| DeepSeek-Coder | 0.902 | 0.511 | -0.391 |
| WizardCoder | 0.800 | 0.080 | -0.720 |
| Aya | 0.650 | 0.482 | -0.168 |

Angka tersebut mendukung hipotesis adanya kesenjangan bahasa, tetapi belum membuktikan bahwa pola yang sama terjadi pada coding agent modern dan tugas repository-level.

## Proposed Product

Sebuah evaluation harness bernama sementara **IndoAgentBench** yang menyediakan:

- pasangan issue Bahasa Inggris dan Indonesia yang ekuivalen;
- repositori dan container yang identik untuk kedua kondisi;
- runner coding agent;
- eksekusi test otomatis;
- pencatatan trajectory, token, biaya, waktu, dan tool calls;
- klasifikasi kegagalan;
- modul mitigasi language bridge.

Language bridge dapat memiliki beberapa strategi:

1. Direct Indonesian: instruksi Indonesia diberikan langsung.
2. English baseline: instruksi asli berbahasa Inggris.
3. Translate-then-act: instruksi Indonesia diterjemahkan ke Inggris sebelum agent bekerja.
4. Terminology-preserving normalization: Bahasa Indonesia dipertahankan, tetapi identifier, API, nama file, error, dan istilah teknis dijaga dalam Bahasa Inggris.
5. Bilingual structured prompt: requirement, constraints, dan acceptance criteria ditulis dalam struktur dwibahasa.

## Research Questions

1. Apakah bahasa instruksi menyebabkan perbedaan task resolution rate pada coding agent?
2. Apakah besar kesenjangan berbeda menurut model, jenis tugas, dan tingkat kesulitan?
3. Pada tahap mana instruksi Indonesia paling sering menyebabkan kegagalan: pemahaman requirement, pencarian lokasi kode, implementasi, atau validasi?
4. Apakah language bridge dapat mengurangi kesenjangan tanpa menambah biaya dan waktu secara berlebihan?

## Experimental Design

Gunakan desain within-task paired comparison: tugas, commit, repository state, test suite, agent, dan budget dibuat identik; hanya representasi bahasa instruksi yang berubah.

Scope sarjana yang realistis:

- 50-100 tugas repository-level;
- Python sebagai satu bahasa pemrograman;
- 2-3 LLM dari keluarga berbeda;
- satu agent harness, misalnya OpenHands/SWE-agent atau agent sederhana yang dikontrol;
- 3-5 kondisi bahasa;
- minimal 3 pengulangan bila sampling tidak deterministik.

Dataset dapat dibuat dari subset benchmark repository-level yang lisensinya memungkinkan, lalu issue diterjemahkan dan diverifikasi oleh penutur Indonesia yang memahami software engineering. Alternatif lebih terkontrol adalah membuat task dari beberapa repositori open-source kecil dengan patch dan test sebagai oracle.

## Metrics

- task resolution rate;
- test pass rate;
- pass@k;
- jumlah langkah dan tool calls;
- token serta biaya;
- waktu penyelesaian;
- invalid patch rate;
- regression rate;
- requirement coverage;
- terminological misunderstanding rate;
- failure taxonomy berdasarkan trajectory agent.

Analisis utama sebaiknya memakai paired significance test dan confidence interval karena setiap versi bahasa berasal dari task yang sama.

## Novelty

> **PERINGATAN 2026-07-20**: Klaim kebaruan di bawah ditulis 2026-06-08 sebelum verifikasi literatur mandiri. Setelah verifikasi ke arXiv, klaim "benchmark Bahasa Indonesia pertama untuk repository-level coding agents" **masih benar** (belum ada yang Bahasa Indonesia spesifik), TAPI klaim implisit "pertama menguji efek bahasa natural pada coding agent repository-level" **GUGUR** karena Ren et al. (2026, arXiv:2604.14210) sudah menguji efek bahasa Cina pada SWE-bench Lite. Lihat `literature-comparison-2026-07-20.md` untuk detail. Kebaruan yang tersisa: Bahasa Indonesia low-resource, translate-then-act, failure taxonomy, audit ekuivalensi, transformasi task anti-kontaminasi.

Kontribusi yang defensible bukan klaim umum bahwa "LLM lebih buruk dalam Bahasa Indonesia", karena indikasi tersebut sudah ada pada code generation.

Kebaruan yang lebih kuat (per 2026-06-08, perlu re-evaluasi):

- benchmark Bahasa Indonesia untuk repository-level coding agents;
- eksperimen kausal terkontrol dengan parallel issue pairs;
- analisis trajectory dan failure mode, bukan hanya output akhir;
- evaluasi interaksi antara bahasa instruksi dan kemampuan model;
- language bridge sebagai intervensi/produk untuk mengurangi kesenjangan.

## Important Controls

- Terjemahan harus mempertahankan semantics dan acceptance criteria.
- Nama fungsi, identifier, path, API, dan pesan error tidak diterjemahkan.
- Panjang serta struktur prompt sebaiknya diseimbangkan.
- Repository dan environment harus identik.
- Hindari menyimpulkan sebab dari satu model atau satu kali run.
- Pisahkan efek kualitas terjemahan dari efek bahasa dengan human-authored Indonesian prompts dan audit bilingual.

## Feasibility and Risks

Feasibility: sedang-tinggi jika memakai 50-100 task dan API models atau model lokal berukuran moderat.

Risiko terbesar adalah biaya eksperimen agent dan kualitas pasangan terjemahan. Scope dapat dikurangi menjadi 40-60 task, dua model, dan tiga kondisi utama: English, direct Indonesian, dan translate-then-act.

Kontaminasi benchmark juga perlu dipertimbangkan. Penggunaan task baru atau transformasi issue dengan test tersembunyi akan memperkuat validitas.

## Sources

- mHumanEval, NAACL 2025: https://aclanthology.org/2025.naacl-long.570/
- HumanEval-XL, LREC-COLING 2024: https://aclanthology.org/2024.lrec-main.735/
- StudentEval, ACL Findings 2024: https://aclanthology.org/2024.findings-acl.501/
- Multi-SWE-bench: https://arxiv.org/abs/2504.02605
- SWE-PolyBench: https://arxiv.org/abs/2504.08703
- DevEval, ACL Findings 2024: https://aclanthology.org/2024.findings-acl.214/
- Cross-Lingual-Thought Prompting, EMNLP Findings 2023: https://aclanthology.org/2023.findings-emnlp.826/
- Self-Explained Keywords, ACL Findings 2025: https://aclanthology.org/2025.findings-acl.324/

## Writing Handoff

Masalah nyata: developer atau mahasiswa Indonesia dapat memberi instruksi coding dalam bahasa yang paling mereka kuasai, tetapi kualitas agent mungkin tidak setara dengan penggunaan Bahasa Inggris.

Produk: benchmark harness dan language bridge untuk mengukur serta mengurangi kesenjangan tersebut.

Hipotesis utama: instruksi Indonesia menurunkan resolution rate, terutama pada model code-specialized atau model dengan kemampuan multilingual lebih lemah; strategi translate-then-act atau terminology-preserving normalization dapat mengurangi kesenjangan.

## Open Questions

- Coding agent/framework yang akan digunakan.
- Akses API/GPU dan batas biaya.
- Sumber task: benchmark existing atau task baru.
- Target pengguna: developer umum atau mahasiswa pemrograman.
