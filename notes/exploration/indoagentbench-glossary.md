# Glossary Kandidat: IndoAgentBench

> **Status: STORED** — glossary ini berlaku **hanya jika** kandidat IndoAgentBench dipilih sebagai topik final. Saat ini topik belum di-accept. Dipindahkan dari `CONTEXT.md` saat `CONTEXT.md` dijadikan general lintas-topik pada 2026-07-20.

## Entitas inti produk

**Coding agent**:
Program berbasis LLM yang menyelesaikan tugas software engineering repository-level secara otonom — membaca issue, menelusuri kode, memakai terminal, membuat patch, menjalankan test.
_Avoid_: AI programmer, autonomous developer, bot.

**Repository-level task**:
Satu unit pekerjaan yang harus diselesaikan agent pada sebuah repositori, dievaluasi dengan test suite otomatis; bukan single-turn code generation.
_Avoid_: function-level task, snippet task, single-file task.

**Issue**:
Ringkasan kebutuhan perangkat lunak yang ditulis pengguna sebagai input agent; dalam produk ini direpresentasikan dalam Bahasa Indonesia, Bahasa Inggris, atau keduanya.
_Avoid_: ticket, request, bug report.

**Task instance**:
Pasangan (repository state, issue, test suite) yang siap dieksekusi agent; satu task instance bisa memiliki beberapa versi bahasa instruksi.
_Avoid_: example, sample, data point.

**Issue pair**:
Dua versi task instance yang identik kecuali bahasa instruksi: versi Indonesia dan versi Inggris yang ekuivalen secara semantik dan acceptance criteria.
_Avoid_: parallel task, translated task, bilingual task.

**Benchmark harness**:
Produk utama berupa perangkat self-service untuk menjalankan coding agent pada kumpulan task instance, mencatat trajectory, menjalankan test, dan menghasilkan laporan; dapat dipakai ulang oleh pihak lain.
_Avoid_: evaluation script, test runner, experiment framework.

## Konsep ilmiah

**Resolution rate**:
Proporsi task instance yang berhasil diselesaikan agent, ditandai oleh lulusnya test suite pada patch yang dihasilkan.
_Avoid_: success rate, accuracy, solve rate.

**Trajectory**:
Urutan langkah dan tool call yang dijalankan agent selama satu task instance, termasuk pesan, aksi terminal, observasi, dan keputusan.
_Avoid_: trace, log, history.

**Failure taxonomy**:
Klasifikasi mode kegagalan agent berdasarkan analisis trajectory; terdiri dari 4 kategori a priori (requirement misunderstanding, wrong location, invalid patch, test validation failure) ditambah 1-2 kategori emergent dari analisis; dianotasi oleh 2 annotator dengan ukur agreement Cohen's kappa.
_Avoid_: error types, failure modes, bug classification.

**Instruction language gap**:
Selisih performa agent antara kondisi instruksi Bahasa Indonesia dan Bahasa Inggris pada task instance yang setara; diukur dengan paired comparison.
_Avoid_: language bias, language penalty, language degradation.

## Status produk

**Self-service benchmark**:
Bentuk akhir produk: dapat dipasang dan dipakai oleh pengguna lain tanpa intervensi penulis, dengan dokumentasi, CLI, contoh task, dan laporan otomatis.
_Avoid_: demo script, one-off experiment, internal tool.

## Komponen eksperimen

**Agent harness**:
Kerangka eksekusi agent yang menjalankan coding agent pada task instance dalam environment terisolasi; memilih OpenHands sebagai harness baseline.
_Avoid_: agent framework, runtime, executor.

**Model LLM**:
Dua model dari keluarga berbeda untuk perbandingan kesenjangan bahasa: Gemini 2.0 Flash (Google AI Studio free tier, keluarga Google) dan Llama-3.3-70B (Groq free tier, keluarga Meta). Pilihan ditentukan oleh keterbatasan anggaran $0 dan ketiadaan GPU lokal.
_Avoid_: LLM, language model, backend model.

**Task transformation**:
Prosedur mengubah identifier, fungsi, atau test non-public pada task instance yang berasal dari benchmark populer untuk mengurangi kontaminasi training data; gold test disimpan di luar prompt agent.
_Avoid_: perturbation, mutation, augmentation.

**Equivalence audit**:
Protokol verifikasi bahwa versi Bahasa Indonesia dan Bahasa Inggris dari sebuah issue memiliki semantics dan acceptance criteria yang setara; dilakukan oleh penutur Indonesia yang memahami software engineering dengan rubrik anotasi dan ukur agreement antar annotator.
_Avoid_: translation check, bilingual review, manual verification.