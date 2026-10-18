# Smoke test: contoh ringkasan

> Hanya pemeriksaan perangkat lunak. Contoh dan skor ini bukan hasil penelitian.

Contoh test: 8 artikel.

## Artikel 1: `130722_hiburan_riverdance`

**Ringkasan acuan**

> Para penari Irlandia mencatatkan rekor dunia di Dublin, dalam melakukan tarian Riverdance terpanjang.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.385 · ROUGE-2: 0.083 · ROUGE-L: 0.308 · BERTScore: 0.783 · waktu: 1.69 dtk

Pemerintah Irlandia mengatakan jumlah ribuan orang yang ikut dalam tarian Riverdance di Irlandia.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.286 · ROUGE-2: 0.000 · ROUGE-L: 0.095 · BERTScore: 0.746 · waktu: 0.97 dtk

Riverdance di Irlandia disebutkan diikuti oleh ribuan orang.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.483 · ROUGE-2: 0.148 · ROUGE-L: 0.276 · BERTScore: 0.793 · waktu: 1.51 dtk

Pembuat Riverdance di Irlandia akan mengirim pesan kepada para penari yang akan menggelar tarian di Dublin.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.179 · ROUGE-2: 0.000 · ROUGE-L: 0.107 · BERTScore: 0.698 · waktu: 2.53 dtk

Riverdance di Irlandia disebutkan diikuti oleh ribuan orang. Lebih dari 2.000 orang dari 163 sekolah tari di 44 negara berkumpul di pinggiran sungai Liffey pada Minggu (21/07). Rekor sebelumnya dipegang oleh 652 orang yang menari dalam barisan di Nashville, Tennessee AS.

## Artikel 2: `151127_majalah_film_terbaik`

**Ringkasan acuan**

> Film dokumenter yang menceritakan keluarga korban pembantaian PKI tahun 1965 di Indonesia, Senyap atau The Look of Silence karya Joshua Oppenheimer masuk dalam salah satu film terbaik hasil jajak kritikus Inggris.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.444 · ROUGE-2: 0.131 · ROUGE-L: 0.317 · BERTScore: 0.762 · waktu: 3.41 dtk

Film The Look of Silence yang merupakan lanjutan dari film The Act of Killing, dirancang oleh sutradara Inggris Joshua Oppenheimer, berada di urutan 19/20 dalam urutan film yang masuk daftar terbaik.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.417 · ROUGE-2: 0.217 · ROUGE-L: 0.333 · BERTScore: 0.745 · waktu: 1.65 dtk

The Look of Silence (Joshua Oppenheimer) akan menjadi film terbaik karya sutradara yang diterbitkan oleh The Guardian.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.143 · ROUGE-2: 0.000 · ROUGE-L: 0.095 · BERTScore: 0.653 · waktu: 1.29 dtk

The Assassin (45 Years) karya Andrew Haigh, yang menempati urutan 14.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.289 · ROUGE-2: 0.136 · ROUGE-L: 0.222 · BERTScore: 0.699 · waktu: 2.80 dtk

Poster film *The Look of Silence* di sebuah stasiun kereta di London, film ini berada di urutan 19/20 bersama film *Horse Money* (Pedro Costa) dan film dokumenter *The Look of Silence* (Joshua Oppenheimer) yang merupakan lanjutan dari *Jagal* atau *The Act of Killing*. Film ini juga berhasil membawa Hou Hsiao-Hsien sebagai sutradara terbaik di festival film Cannes.

## Artikel 3: `120925_asiapensiun`

**Ringkasan acuan**

> Banyak pekerja di Indonesia menghadapi masa tua yang tidak jelas karena hanya sekitar 10% yang memiliki pensiun, menurut buku yang disusun Bank Pembangunan Asia (ADB).

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.176 · ROUGE-2: 0.000 · ROUGE-L: 0.176 · BERTScore: 0.736 · waktu: 1.17 dtk

Pemerintah Indonesia akan menerapkan sistem pensiun yang lebih besar.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.121 · ROUGE-2: 0.000 · ROUGE-L: 0.121 · BERTScore: 0.720 · waktu: 1.05 dtk

Pemerintah Indonesia akan memperluas pensiun bagi sektor swasta.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.129 · ROUGE-2: 0.000 · ROUGE-L: 0.065 · BERTScore: 0.709 · waktu: 0.92 dtk

Pensiun Indonesia akan diperluas dalam 2015.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.370 · ROUGE-2: 0.154 · ROUGE-L: 0.185 · BERTScore: 0.771 · waktu: 1.72 dtk

Buku yang disusun oleh ADB menyebutkan bahwa pensiunan Indonesia hanya PNS dan sektor swasta. "Sebagian besar penduduk Indonesia tidak punya pensiun, pada prinsipnya hanya sekitar 10% dari jumlah penduduk."

## Artikel 4: `150706_trensosial_christians4ramadan`

**Ringkasan acuan**

> Sejumlah pengguna media sosial berpartisipasi dalam gerakan #Christians4Ramadan, sebagai bentuk solidaritas umat Kristiani untuk warga Muslim di bulan puasa.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.187 · ROUGE-2: 0.000 · ROUGE-L: 0.187 · BERTScore: 0.750 · waktu: 2.29 dtk

Gerakan #Muslim4Lent yang mengambil nama #Christians4Ramadan di Amerika Serikat terinspirasi oleh gerakan #Muslims4Lent.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.171 · ROUGE-2: 0.061 · ROUGE-L: 0.114 · BERTScore: 0.712 · waktu: 1.88 dtk

Aisha Fatima, seorang Muslim yang beragama Kristen, mengatakan bahwa gerakan #christians4ramadan akan terus dilakukan selama Ramadan.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.100 · ROUGE-2: 0.000 · ROUGE-L: 0.100 · BERTScore: 0.669 · waktu: 0.43 dtk

#christians4ramadan

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.200 · ROUGE-2: 0.042 · ROUGE-L: 0.120 · BERTScore: 0.723 · waktu: 1.83 dtk

Ulil mengatakan bahwa gerakan #Christians4Ramadan menarik perhatiannya dan memberikan contoh pengalamannya saat di Boston. Dalam konteks ini, Anthony Murley mengatakan bahwa tagar ini digunakan oleh banyak orang untuk memicu dialog antaragama.

## Artikel 5: `160501_indonesia_sandera_abusayyaf`

**Ringkasan acuan**

> Menteri Luar Negeri Indonesia Retno Marsudi mengatakan 10 anak buah kapal (ABK) yang sebelumnya disandera oleh kelompok pemberontak Filipina, Abu Sayyaf, akan langsung menjalani pemeriksaan kesehatan di Jakarta.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.250 · ROUGE-2: 0.000 · ROUGE-L: 0.200 · BERTScore: 0.728 · waktu: 1.62 dtk

Presiden Joko Widodo mengatakan akan melakukan pembebasan 10 ABK WNI dari Filipina.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.360 · ROUGE-2: 0.000 · ROUGE-L: 0.200 · BERTScore: 0.761 · waktu: 2.47 dtk

Presiden Joko Widodo mengatakan bahwa pemeriksaan akan dilakukan di kota Jolo, Filipina, untuk mengenali 10 ABK WNI yang masih dalam kondisi kesehatan.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.118 · ROUGE-2: 0.062 · ROUGE-L: 0.118 · BERTScore: 0.716 · waktu: 0.83 dtk

Pemeriksaan kesehatan terjadi pada hari ini.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.328 · ROUGE-2: 0.068 · ROUGE-L: 0.230 · BERTScore: 0.743 · waktu: 2.10 dtk

ABK tiba di Halim Perdanakusuma, Jakarta, dengan 10 ABK WNI tiba di Halim Perdanakusuma, Filipina selatan. Retno Marsudi menyampaikan kepastian bahwa 10 ABK WNI akan dibawa ke rumah sakit untuk dilakukan pemeriksaan kesehatan.

## Artikel 6: `media-49507761`

**Ringkasan acuan**

> Sidang Konvensi Perdagangan Internasional jenis-jenis hewan dan tumbuhan yang terancam punah (Cites) melarang ekspor gajah liar Afrika ke kebun binatang di seluruh dunia.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.293 · ROUGE-2: 0.051 · ROUGE-L: 0.244 · BERTScore: 0.749 · waktu: 2.29 dtk

Pemerintah Swiss mengumumkan keputusan baru yang menghapus pelarangan untuk mengambil gajah dari alam liar dan kebun binatang.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.000 · ROUGE-2: 0.000 · ROUGE-L: 0.000 · BERTScore: 0.537 · waktu: 6.59 dtk

Pemerintah Zimbabwe mengumumkan keputusan untuk menghapus penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian penghentian peng

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.114 · ROUGE-2: 0.000 · ROUGE-L: 0.114 · BERTScore: 0.721 · waktu: 1.50 dtk

Pemerintah Swiss mengatakan bahwa keputusan ini akan memperkuat pembatasan perdagangan gajah.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.200 · ROUGE-2: 0.000 · ROUGE-L: 0.100 · BERTScore: 0.698 · waktu: 1.18 dtk

Keputusan pelarangan yang dibuat Selasa (27/08) di Genewa, Swiss, ini semakin memperketat pembatasan perdagangan gajah.

## Artikel 7: `130114_iptek_stroke`

**Ringkasan acuan**

> Saat anda berpikir mengenai pasien stroke "tipikal", anda langsung teringat pada seseorang yang berusia lanjut, kelebihan berat badan, malas berolahraga dan merokok.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.056 · ROUGE-2: 0.000 · ROUGE-L: 0.056 · BERTScore: 0.672 · waktu: 2.12 dtk

Pemerintah Inggris mengatakan bahwa ada 150.000 orang di negaranya terkena stroke setiap tahun.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.154 · ROUGE-2: 0.054 · ROUGE-L: 0.154 · BERTScore: 0.660 · waktu: 1.85 dtk

Andrew Marr, penyiar BBC yang berusia 50 dan penyiar BBC yang berusia 50, tidak memenuhi kategori itu.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.146 · ROUGE-2: 0.051 · ROUGE-L: 0.146 · BERTScore: 0.675 · waktu: 1.92 dtk

Andrew Marr, penyiar BBC yang berusia 50 tahun dan seorang penyiar yang sudah berpengalaman dalam berbagai tajuk dan berita.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.135 · ROUGE-2: 0.028 · ROUGE-L: 0.081 · BERTScore: 0.671 · waktu: 2.84 dtk

Andrew Marr, penyiar BBC yang berusia 50-an dan rajin berolahraga, tidak memenuhi kategori penyiar. Usia adalah salah satu faktor risiko terbesar, tetapi siapa saja dari usia berapa saja dapat terserang stroke. Lebih dari 150.000 orang di Inggris terserang stroke setiap tahun, dengan seperempat dari mereka berusia di bawah 65 tahun.

## Artikel 8: `151004_indonesia_komnasham_kancil`

**Ringkasan acuan**

> Komisi Nasional Hak Asasi Manusia pada hari Senin (05/10) akan menyelidiki perkara penganiayaan dan pembunuhan aktivis antitambang bernama Salim alias Kancil di Desa Selok Awar Awar, Kecamatan Pasirian, Kabupaten Lumajang.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.043 · ROUGE-2: 0.000 · ROUGE-L: 0.043 · BERTScore: 0.695 · waktu: 2.12 dtk

Kepolisian resor Lumajang mengumumkan bahwa dua personil polisi diduga menerima suap dalam kasus penambangan pasir.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.029 · ROUGE-2: 0.000 · ROUGE-L: 0.029 · BERTScore: 0.568 · waktu: 6.96 dtk

Kepolisian Resor Lumajang, Kepolisian Resor Lumajang, Kepolisian Resor Lumajang, Kepolisian Resor Lumajang, Kepolisian Resor Lumajang, Kepolisian Resor Lumajang, Kepolisian Resor Lumajang, Kepolisian Resor Lumajang, Kepolisian Resor Lumajang, Kepolisian Resor Lumajang, Kepolisian Resor Lumajang, Kepolisian Resor Lumajang, Kepolisian Resor Lumaj

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.143 · ROUGE-2: 0.000 · ROUGE-L: 0.143 · BERTScore: 0.697 · waktu: 1.59 dtk

Kepuspekannya, Komnas HAM akan mengumpulkan bukti dan saksi terkait kematian Salim.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.088 · ROUGE-2: 0.000 · ROUGE-L: 0.088 · BERTScore: 0.668 · waktu: 2.40 dtk

Komnas HAM akan mengumpulkan bukti dan saksi terkait kematian Salim. Dalam kesempatan itu, Komnas HAM akan mengumpulkan bukti, dokumen dan keterangan dari sejumlah pihak, termasuk korban, saksi, dan Kepolisian, serta dugaan pembiaran oleh aparatur negara dan pemerintah.
