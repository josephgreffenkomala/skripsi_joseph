# Smoke test: contoh ringkasan

> Hanya pemeriksaan perangkat lunak. Contoh dan skor ini bukan hasil penelitian.

Contoh test: 40 artikel.

## Artikel 1: `130722_hiburan_riverdance`

**Ringkasan acuan**

> Para penari Irlandia mencatatkan rekor dunia di Dublin, dalam melakukan tarian Riverdance terpanjang.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.381 · ROUGE-2: 0.000 · ROUGE-L: 0.286 · BERTScore: 0.762 · waktu: 0.90 dtk

Riverdance di Irlandia akan menari di kota Dublin.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.500 · ROUGE-2: 0.111 · ROUGE-L: 0.300 · BERTScore: 0.803 · waktu: 0.73 dtk

Riverdance di Irlandia akan menjadi rekor dunia.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.476 · ROUGE-2: 0.105 · ROUGE-L: 0.381 · BERTScore: 0.810 · waktu: 0.95 dtk

Irlandia akan menggelar rekor pertunjukan Riverdance di Dublin.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.179 · ROUGE-2: 0.000 · ROUGE-L: 0.107 · BERTScore: 0.698 · waktu: 2.54 dtk

Riverdance di Irlandia disebutkan diikuti oleh ribuan orang. Lebih dari 2.000 orang dari 163 sekolah tari di 44 negara berkumpul di pinggiran sungai Liffey pada Minggu (21/07). Rekor sebelumnya dipegang oleh 652 orang yang menari dalam barisan di Nashville, Tennessee AS.

## Artikel 2: `dunia-43919872`

**Ringkasan acuan**

> Para pemimpin Korea Utara dan Korea Selatan mencapai kesepakatan untuk bekerja sama membebaskan semenanjung Korea dari senjata nuklir.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.500 · ROUGE-2: 0.294 · ROUGE-L: 0.444 · BERTScore: 0.793 · waktu: 2.55 dtk

Korea Utara dan Korea Selatan memutuskan untuk mengganti perjanjian senjata nuklir yang mengakhiri Perang Korea pada tahun 1953.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.256 · ROUGE-2: 0.054 · ROUGE-L: 0.205 · BERTScore: 0.746 · waktu: 2.39 dtk

Korea Utara mengumumkan komitmen untuk mengubah gencatan senjata yang mengakhiri Perang Korea pada tahun 1953 menjadi perjanjian damai yang lebih permanen.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.412 · ROUGE-2: 0.250 · ROUGE-L: 0.353 · BERTScore: 0.800 · waktu: 1.57 dtk

Korea Utara dan Korea Selatan mengumumkan kesepakatan antara pemimpin Kim Jong-un dengan Moon Jae-in.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.308 · ROUGE-2: 0.127 · ROUGE-L: 0.277 · BERTScore: 0.743 · waktu: 2.59 dtk

KTT antara pemimpin Korea Utara Kim Jong-un dan pemimpin Korea Selatan Moon Jae-in menyepakati kesepakatan untuk mengubah gencatan senjata yang mengakhiri Perang Korea menjadi perjanjian damai yang lebih permanen. Kedua pemimpin menunjukkan kepedulian terhadap langkah-langkah tersebut, tetapi analis tetap skeptis tentang antusiasme belakangan ini.

## Artikel 3: `120925_asiapensiun`

**Ringkasan acuan**

> Banyak pekerja di Indonesia menghadapi masa tua yang tidak jelas karena hanya sekitar 10% yang memiliki pensiun, menurut buku yang disusun Bank Pembangunan Asia (ADB).

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.118 · ROUGE-2: 0.000 · ROUGE-L: 0.059 · BERTScore: 0.691 · waktu: 1.10 dtk

Pensiun Indonesia akan diperluas lebih dari delapan kali lipat.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.118 · ROUGE-2: 0.000 · ROUGE-L: 0.059 · BERTScore: 0.691 · waktu: 0.97 dtk

Pensiun Indonesia akan diperluas lebih dari delapan kali lipat.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.138 · ROUGE-2: 0.000 · ROUGE-L: 0.069 · BERTScore: 0.703 · waktu: 0.60 dtk

Pensiun Indonesia akan diperluas.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.370 · ROUGE-2: 0.154 · ROUGE-L: 0.185 · BERTScore: 0.771 · waktu: 1.64 dtk

Buku yang disusun oleh ADB menyebutkan bahwa pensiunan Indonesia hanya PNS dan sektor swasta. "Sebagian besar penduduk Indonesia tidak punya pensiun, pada prinsipnya hanya sekitar 10% dari jumlah penduduk."

## Artikel 4: `130605_iptek_mesinsampah`

**Ringkasan acuan**

> Tiga siswi sekolah menengah atas di Yogyakarta tengah mengembangkan alat untuk menyaring sampah di sungai, temuan yang membuahkan medali emas pada lomba inventor muda.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.311 · ROUGE-2: 0.140 · ROUGE-L: 0.267 · BERTScore: 0.723 · waktu: 2.54 dtk

Alat penyaring sampah yang disebut "turbine-under-shot waste filter" (TUSF) akan digunakan untuk menyaring sampah organik dan nonorganik di sungai.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.227 · ROUGE-2: 0.095 · ROUGE-L: 0.182 · BERTScore: 0.686 · waktu: 1.95 dtk

Alat ini yang disebut "turbine-under-shot waste filter" (turbine-under-shot) akan digunakan untuk menyaring sampah organik dan nonorganik.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.286 · ROUGE-2: 0.085 · ROUGE-L: 0.204 · BERTScore: 0.735 · waktu: 2.91 dtk

Alat penyaring sampah organik yang diperkenalkan oleh Nurina Zahra, dari SMA 6 Yogyakarta, akan menjadi alat inventir muda yang akan diperkenalkan untuk menyaring sampah organik.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.351 · ROUGE-2: 0.109 · ROUGE-L: 0.175 · BERTScore: 0.717 · waktu: 1.58 dtk

Elizabeth, Nurina Zahra, dan Tri Ayu mengalahkan dalam lomba inventor muda di Malaysia. Alat "turbine-under-shot waste filter" yang diterapkan dalam lomba tersebut meraih medali emas di Malaysia untuk kategori green technology.

## Artikel 5: `130829_suriah_obama_intervensi`

**Ringkasan acuan**

> Presiden AS Barack Obama mengatakan AS telah menyimpulkan bahwa pemerintah Suriah melakukan serangan senjata kimia di dekat Damaskus.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.303 · ROUGE-2: 0.065 · ROUGE-L: 0.242 · BERTScore: 0.782 · waktu: 1.84 dtk

Presiden AS Donald Trump mengatakan, "Saya tidak punya kepentingan dalam konflik apa pun di Suriah."

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.390 · ROUGE-2: 0.205 · ROUGE-L: 0.293 · BERTScore: 0.794 · waktu: 2.62 dtk

Suriah menuduh pemerintah Barat, Rusia, dengan senjata kimia, dan mengatakan bahwa mereka tidak akan melakukan serangan senjata kimia, dan juga menudarkan pemerintah Suriah.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.467 · ROUGE-2: 0.214 · ROUGE-L: 0.467 · BERTScore: 0.848 · waktu: 1.58 dtk

Presiden AS akan mengatakan bahwa pemerintah Suriah tidak akan melakukan intervensi militer.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.256 · ROUGE-2: 0.026 · ROUGE-L: 0.154 · BERTScore: 0.732 · waktu: 3.48 dtk

Obama menyatakan bahwa ia tidak punya kepentingan dalam konflik apa pun di Suriah. Ia mengatakan bahwa penggunaan senjata kimia mempengaruhi kepentingan nasional AS dan bahwa AS tidak akan melakukan intervensi militer. Pernyataan ini dikeluarkan setelah hari penuh perdebatan di PBB. Inggris mendorong anggota-anggota permanen Dewan Keamanan PBB untuk mengeluarkan resolusi yang akan memberikan otorisasi atas tindakan-tindakan untuk mel

## Artikel 6: `130114_berluscon_sidang`

**Ringkasan acuan**

> Majelis hakim di Milan memutuskan sidang atas mantan perdana menteri Italia, Silvio Berlusconi, dalam dakwaan berhubungan seks dengan perempuan di bawah umur, tidak bisa ditunda.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.053 · ROUGE-2: 0.000 · ROUGE-L: 0.053 · BERTScore: 0.645 · waktu: 1.61 dtk

Ruby Sang Pencuri Hati akan kembali mencalonkan diri dalam pemilihan umum Bulan Februari.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.000 · ROUGE-2: 0.000 · ROUGE-L: 0.000 · BERTScore: 0.634 · waktu: 0.91 dtk

Karima El Mahroug akan kembali menjadi pemilih bulan depan.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.105 · ROUGE-2: 0.000 · ROUGE-L: 0.105 · BERTScore: 0.671 · waktu: 1.85 dtk

Ruby Sang Pencuri Hati akan kembali menghadirkan di sidang untuk menyampaikan bukti-bukti.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.240 · ROUGE-2: 0.027 · ROUGE-L: 0.160 · BERTScore: 0.697 · waktu: 3.06 dtk

Kehadiran Karima El Mahroug di sidang Silvio Berlusconi tidak diperlukan lagi. Mereka menolak permintaan Berlusconi agar sidang ditunda hingga berakhirnya pemilihan umum bulan depan dan Berlusconi akan kembali mencalonkan diri. Dengan demikian, ada kemungkinan vonis atas kasus ini bisa diputuskan sebelum pemilihan umum, yang dikhawatirkan akan mempengaruhi perolehan suara Berlusconi.

## Artikel 7: `150816_trigana_air_sar`

**Ringkasan acuan**

> Tim SAR berencana menuju lokasi jatuhnya pesawat Trigana Air di Gunung Tangok, Kabupaten Pegunungan Bintang Papua, pada Senin (17/08), pukul 06.00 WIT.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.367 · ROUGE-2: 0.213 · ROUGE-L: 0.367 · BERTScore: 0.735 · waktu: 3.17 dtk

Tim SAR Jayapura akan melibatkan armada udara milik Trigana Air, TNI dan Polri dalam pencarian pesawat Trigana Air yang jatuh di kawasan Pegunungan Bintang Papua.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.372 · ROUGE-2: 0.195 · ROUGE-L: 0.372 · BERTScore: 0.751 · waktu: 2.12 dtk

Kepala Tim SAR Jayapura, Indonesia, mengatakan akan melakukan pencarian pesawat Trigana Air yang jatuh di kawasan pengunungan Bintang Papua.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.450 · ROUGE-2: 0.263 · ROUGE-L: 0.450 · BERTScore: 0.771 · waktu: 2.15 dtk

Tim SAR Jayapura akan melakukan pencarian pesawat Trigana Air yang jatuh di kawasan Pegunungan Bintang Papua.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.209 · ROUGE-2: 0.092 · ROUGE-L: 0.209 · BERTScore: 0.669 · waktu: 2.51 dtk

Tim SAR Jayapura membantu personil TNI dan Polri dalam pencarian pesawat Trigana Air yang jatuh di Papua, dengan keterangan pers dari Kementerian Perhubungan. Kepala Tim SAR Jayapura, Ludiyanto, mengatakan pencarian diutamakan melalui udara, dan pihaknya belum bisa memastikan jumlah personil yang akan dilibatkan.

## Artikel 8: `majalah-46121987`

**Ringkasan acuan**

> Seorang pria dari Negara Bagian Colorado, Amerika Serikat, mengaku bersalah telah membunuh dua putrinya dan istrinya yang sedang mengandung.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.071 · ROUGE-2: 0.000 · ROUGE-L: 0.047 · BERTScore: 0.523 · waktu: 7.66 dtk

Chris Watts, pria yang dulu menjadi seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang seorang se

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.222 · ROUGE-2: 0.059 · ROUGE-L: 0.222 · BERTScore: 0.752 · waktu: 1.88 dtk

Chris Watts mengakui telah membunuh putrinya, Bella (4) dan Celeste (3), setelah mengakui bahwa dia membunuh putrinya.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.308 · ROUGE-2: 0.250 · ROUGE-L: 0.308 · BERTScore: 0.818 · waktu: 0.92 dtk

Chris Watts mengakui telah membunuh dua putrinya.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.209 · ROUGE-2: 0.031 · ROUGE-L: 0.149 · BERTScore: 0.713 · waktu: 2.56 dtk

Chris Watts mengaku istri dan kedua anaknya hilang pada Agustus lalu. Aksi Watts terungkap kurang dari 24 jam setelah dia mengaku kepada media bahwa istrinya, Shanann Watts yang tengah hamil 15 minggu, dan dua putrinya, Bella (4) dan Celeste (3), hilang. Jasad kedua putrinya didapatkan dalam tangki minyak.

## Artikel 9: `110420_celticbomb`

**Ringkasan acuan**

> Kepolisian Skotlandia sedang menyelidiki pengiriman paket bom kepada Manajer Celtic, Neill Lennon.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.400 · ROUGE-2: 0.111 · ROUGE-L: 0.300 · BERTScore: 0.764 · waktu: 1.02 dtk

Kubu Celtic akan mengganti Neill Lennon sebagai manajer.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.308 · ROUGE-2: 0.250 · ROUGE-L: 0.308 · BERTScore: 0.778 · waktu: 1.68 dtk

Seorang manajer Celtic, Neill Lennon, telah diberi ancaman serupa terhadap aktifitasnya sebagai Manajer Celtic.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.240 · ROUGE-2: 0.087 · ROUGE-L: 0.240 · BERTScore: 0.748 · waktu: 1.42 dtk

Kubu Celtic mengatakan bahwa Neill Lennon akan mendapat ancaman dari kelompok ekstrimis Protestan.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.246 · ROUGE-2: 0.109 · ROUGE-L: 0.140 · BERTScore: 0.720 · waktu: 2.50 dtk

Neill Lennon pernah mendapat ancaman serupa terkait aktifitasnya sebagai Manajer Celtic. Polisi menyebutkan selain dikirimkan kepada Neill Lennon, paket bom juga dikirimkan kepada pengacara, Paul McBride, dan Trish Godman. Dua paket yang diperuntungi terhadap Neill dan McBride berhasil diidentifikasi saat masih berada di kantor pos.

## Artikel 10: `130409_kasus_cebongan_pengadilan`

**Ringkasan acuan**

> Keluarga korban penembakan di LP Cebongan, Sleman, Yogyakarta hari ini meminta agar tersangka pelaku yang merupakan anggota Kopassus disidangkan di pengadilan umum.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.419 · ROUGE-2: 0.146 · ROUGE-L: 0.326 · BERTScore: 0.804 · waktu: 2.79 dtk

Keluarga korban penyerangan LP Cebongan di Sleman, Jawa Barat, yang tewas dalam serangan terhadap para korban, meminta agar kasus tersebut dituntaskan.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.318 · ROUGE-2: 0.190 · ROUGE-L: 0.318 · BERTScore: 0.755 · waktu: 2.67 dtk

Kepala Dinas Penerangan TNI AD, Brigadir Jenderal Rukman Ahmad, mengatakan bahwa perwakilan keluarga korban penyerangan LP Cebongan akan berada di pengadilan umum.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.294 · ROUGE-2: 0.125 · ROUGE-L: 0.294 · BERTScore: 0.751 · waktu: 1.37 dtk

Keluarga korban Viktor Mambait meminta untuk melaporkan kasus tersebut ke pengadilan umum.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.314 · ROUGE-2: 0.163 · ROUGE-L: 0.275 · BERTScore: 0.737 · waktu: 1.91 dtk

Perwakilan keluarga korban penyerangan LP Cebongan meminta kasus tersebut dituntaskan. Perwakilan keluarga empat korban penembakan hari mendatangi kantor sejumlah lembaga meminta agar pengusutan kasus tersebut berlangsung transparan dan tuntas.

## Artikel 11: `130305_majalahlain_kurir_asi`

**Ringkasan acuan**

> Sekelompok pria bermotor berinisiatif melakukan kegiatan amal dengan menjadi pengantar air susu ibu ke rumah sakit untuk bayi prematur.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.242 · ROUGE-2: 0.129 · ROUGE-L: 0.182 · BERTScore: 0.712 · waktu: 1.84 dtk

Midland Freewheelers Emergency Rider Voluntary Service (EVR) mengantarkan ASI untuk bayi prematur atau sakit.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.217 · ROUGE-2: 0.091 · ROUGE-L: 0.130 · BERTScore: 0.707 · waktu: 2.84 dtk

Kemampuan sukarelawan Midland Freewheelers untuk mengantarkan ASI (human serum) untuk bayi prematur atau prematur yang sakit, yang diberikan kepada mereka, menjadi salah satu keunggulan dari kelompok tersebut.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.194 · ROUGE-2: 0.138 · ROUGE-L: 0.194 · BERTScore: 0.716 · waktu: 1.33 dtk

Midland Freewheelers Emergency Rider Voluntary Service mengantarkan ASI untuk bayi-bayi prematur.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.097 · ROUGE-2: 0.033 · ROUGE-L: 0.065 · BERTScore: 0.701 · waktu: 2.29 dtk

Midland Freewheelers butuh lebih banyak sukarelawan untuk mengantarkan ASI. Kelompok tersebut terdiri dari 25 pengendara motor sukarelawan yang mengantar ASI untuk bayi-bayi di Birmingham Women's Hospital. Susu ASI dari para donor digunakan untuk membantu meningkatkan sistem kekebalan tubuh dan melawan infeksi.

## Artikel 12: `140508_majalahlain_penghargaan_penyu_orangutan`

**Ringkasan acuan**

> Fitryanti Pakiding dan Melvin Gumal, masing-masing dari Papua Barat dan Sarawak, Malaysia, menerima Penghargaan Whitley di London atas usaha konservasi penyu dan orang utan.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.256 · ROUGE-2: 0.108 · ROUGE-L: 0.205 · BERTScore: 0.745 · waktu: 2.12 dtk

Dua peneliti di Sarawak, Malaysia, mengakui penghargaan Whitley Award 2014 yang diberikan kepada mereka.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.167 · ROUGE-2: 0.000 · ROUGE-L: 0.167 · BERTScore: 0.684 · waktu: 3.38 dtk

Penyu belimbing di Sarawak, yang dikenal sebagai "penyu belimbing terlalu panas" (Whitley Award) di mana penyu tersebut diperkirakan akan terlalu panas untuk diterima.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.364 · ROUGE-2: 0.190 · ROUGE-L: 0.182 · BERTScore: 0.759 · waktu: 2.26 dtk

Konservasi penyu belimbing di Sarawak, yang dikenal sebagai penyu belimbing, diberikan kepada dua peneliti, Fitry Pakiding dan Melvin Gumal.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.377 · ROUGE-2: 0.179 · ROUGE-L: 0.261 · BERTScore: 0.715 · waktu: 2.67 dtk

Fitry Pakiding dan Melvin Gumal mengaku penghargaan Whitley Award 2014 yang diterima oleh Putri Anne sebagai penghargaan konservasi. Whitley Award 2014 diserahkan oleh Putri Anne di London, Kamis malam (08/05). Fitryanti Pakiding dan Melvin Gumal menerima hadiah sebesar £15,000 dan Rp683 juta.

## Artikel 13: `majalah-38589274`

**Ringkasan acuan**

> Presiden Filipina, Rodrigo Duterte, memerintahkan pembagian alat kontrasepsi gratis kepada sekitar enam juta perempuan yang tidak bisa mendapatkannya.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.214 · ROUGE-2: 0.077 · ROUGE-L: 0.214 · BERTScore: 0.778 · waktu: 1.61 dtk

Pemerintah Filipina akan meningkatkan akses alat kontrasepsi bagi keluarga berencana.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.074 · ROUGE-2: 0.000 · ROUGE-L: 0.074 · BERTScore: 0.727 · waktu: 1.25 dtk

Pemerintah Filipina akan mengurangi tingkat kemiskinan pada tahun 2018.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.429 · ROUGE-2: 0.077 · ROUGE-L: 0.357 · BERTScore: 0.815 · waktu: 1.27 dtk

Pemerintah Filipina akan mengganti alat kontrasepsi yang diberikan kepada perempuan.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.393 · ROUGE-2: 0.259 · ROUGE-L: 0.250 · BERTScore: 0.742 · waktu: 2.68 dtk

Diperkirakan sekitar enam juta perempuan Filipina menginginkan alat kontrasepsi namun tidak bisa mendapatkannya. Tujuan utamanya adalah untuk mencegah peningkatan jumlah kehamilan yang tidak diinginkan, khususnya di kalangan kelompok miskin. Peningkatan ketersediaan alat kontrasepsi dianggap penting dalam mengurangi kemiskinan.

## Artikel 14: `120819_pakistanigirl`

**Ringkasan acuan**

> Polisi Pakistan menahan seorang gadis berusia 11 tahun yang mengalami keterbelakangan mental karena dianggap menghina Al Quran.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.114 · ROUGE-2: 0.000 · ROUGE-L: 0.114 · BERTScore: 0.735 · waktu: 2.44 dtk

Gadis kecil yang beragama Kristen, yang dulu menjadi salah satu penerima perubahan undang-undang penghinaan agama, ditemukan dibakar.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.188 · ROUGE-2: 0.000 · ROUGE-L: 0.188 · BERTScore: 0.737 · waktu: 1.94 dtk

Pemerintah Pakistan menghukum seorang perubahan undang-undang penghinaan agama (PU) yang dituduh oleh para aktivis.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.188 · ROUGE-2: 0.067 · ROUGE-L: 0.188 · BERTScore: 0.759 · waktu: 1.37 dtk

Seorang gadis kecil yang berada di bawah tekanan massa yang akan membakar rumah warga Kristen.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.133 · ROUGE-2: 0.027 · ROUGE-L: 0.107 · BERTScore: 0.700 · waktu: 3.49 dtk

Pertahanan berita berikut menyampaikan bahwa Shahbaz Bhatti dibunuh karena anjurkan perubahan undang-undang penghinaan agama. Massa lokal melaporkan bahwa massa tersebut menuntut agar kediaman gadis kecil itu dibakar. Menteri Kesatuan Nasional Paul Bhatti mengatakan bahwa gadis kecil itu ditemukan membawa kantung sampah yang terdapat dalam Al Quran. "Inilah yang membuat warga marah dan kerumunan massa menuntut tindakan terhadap

## Artikel 15: `140611_sewolpemilik`

**Ringkasan acuan**

> Sedikitnya 4.000 polisi Korea Selatan kembali menggerebek kompleks Gereja Baptis Evangelis di daerah pinggiran Kota Seoul guna mencari Yoo Byung-eun, miliuner pemilik kapal feri Sewol yang tenggelam April lalu.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.359 · ROUGE-2: 0.270 · ROUGE-L: 0.359 · BERTScore: 0.755 · waktu: 1.06 dtk

Polisi Korea Selatan mengganti pemilik kapal feri Sewol.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.356 · ROUGE-2: 0.186 · ROUGE-L: 0.311 · BERTScore: 0.759 · waktu: 1.91 dtk

Polisi Korea Selatan mengganti tugas penggerebekan kapal feri yang tenggelam di Anseong, Korea Selatan.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.211 · ROUGE-2: 0.111 · ROUGE-L: 0.211 · BERTScore: 0.728 · waktu: 0.96 dtk

Polisi Korea Selatan mengganti tindakan penggerebekan gereja.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.213 · ROUGE-2: 0.109 · ROUGE-L: 0.170 · BERTScore: 0.687 · waktu: 3.39 dtk

Polisi Korea Selatan belum kunjung menemukan pemilik kapal feri Sewol. Pria berusia 70-an tahun itu merupakan salah seorang pendiri gereja tersebut. Para petugas, yang mengusung tameng dan pentungan, bergerak dari satu bangunan ke bangunan lain di kawasan seluas beberapa lapangan sepak bola. Ratusan jemaah di lokasi memprotes kedatangan ribuan polisi. Beberapa orang membuntuti polisi, lainnya menyerukan slogan, “Mari lawan polisi dan jaksa”.

## Artikel 16: `media-51457957`

**Ringkasan acuan**

> Setelah kekhalifahan ISIS hancur, banyak petempurnya hijrah ke Asia. Tepatnya ke Pulau Sulu, Mindanao, Filipina.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.000 · ROUGE-2: 0.000 · ROUGE-L: 0.000 · BERTScore: 0.662 · waktu: 1.70 dtk

Kepala Katedral Jolo, Victoriana, mengatakan akan tetap mengamankan gereja di sana.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.160 · ROUGE-2: 0.000 · ROUGE-L: 0.160 · BERTScore: 0.712 · waktu: 1.69 dtk

ISIS mengguncang katedral di Jolo, Filipina, dengan mengguncang 23 orang.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.083 · ROUGE-2: 0.000 · ROUGE-L: 0.083 · BERTScore: 0.684 · waktu: 1.02 dtk

ISIS mengganti pria-pria yang telah mengganti pribadi mereka.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.053 · ROUGE-2: 0.000 · ROUGE-L: 0.053 · BERTScore: 0.646 · waktu: 3.32 dtk

Pasangan suami istri pengebom bunuh diri ISIS asal Indonesia, Ruille Zeke dan Ulfa, melancarkan misinya di Katedral Jolo. Mereka meledakkan bom bunuh diri di Katedral Jolo dan menewaskan 23 orang. Serangan yang dilakukan mereka menimbulkan trauma bagi komunitas Kristen di wilayah tersebut. Victoriana, salah satu umat Katedral Jolo, mengaku masih takut kembali ke gereja, bahkan satu tahun berselang usai insiden.

## Artikel 17: `130620_pendidikan_malaysia_asap`

**Ringkasan acuan**

> Sekitar 200 sekolah di Muar, Malaysia, ditutup untuk sementara karena kualitas udara akibat kabut asap dari Indonesia sudah mencapai tingkat berbahaya.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.229 · ROUGE-2: 0.061 · ROUGE-L: 0.229 · BERTScore: 0.770 · waktu: 1.89 dtk

Kebakaran hutan di Muar, di pantai barat Malaysia, menyebabkan asap hutan yang paling buruk.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.263 · ROUGE-2: 0.056 · ROUGE-L: 0.158 · BERTScore: 0.766 · waktu: 2.57 dtk

Kebakaran hutan di Muar, Sumatera, yang terjadi di kawasan Indonesia, menyebabkan asap menyebar ke Malaysia dan Singapura.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.148 · ROUGE-2: 0.080 · ROUGE-L: 0.148 · BERTScore: 0.733 · waktu: 0.75 dtk

Kebakaran hutan di Muar dan Sumatera.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.209 · ROUGE-2: 0.062 · ROUGE-L: 0.149 · BERTScore: 0.736 · waktu: 2.43 dtk

Murid sekolah di Muar, di pantai barat Malaysia, berseberangan dengan Pulau Sumatera. Kebakaran hutan di kawasan Indonesia di Sumatera dan Kalimantan telah menyebabkan asap menyebar ke Malaysia dan Singapura. Wartawan BBC di Kuala Lumpur, Jennifer Pak, melaporkan bahwa Muar memiliki indeks polusi udara yang paling buruk.

## Artikel 18: `130423_israel_suriah_kimia`

**Ringkasan acuan**

> Israel untuk pertama kalinya menuduh Suriah beberapa kali menggunakan senjata kimia terhadap pasukan pemberontak.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.385 · ROUGE-2: 0.083 · ROUGE-L: 0.385 · BERTScore: 0.839 · waktu: 1.65 dtk

Suriah mengatakan bahwa senjata kimia telah digunakan dalam serangan terhadap tentara pemberontak.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.250 · ROUGE-2: 0.091 · ROUGE-L: 0.250 · BERTScore: 0.791 · waktu: 1.30 dtk

Israel mengatakan bahwa senjata kimia (chemical weapons) digunakan dalam serangan.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.273 · ROUGE-2: 0.100 · ROUGE-L: 0.273 · BERTScore: 0.774 · waktu: 0.88 dtk

Suriah mengatakan bahwa senjata kimia digunakan dalam serangan.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.182 · ROUGE-2: 0.038 · ROUGE-L: 0.145 · BERTScore: 0.744 · waktu: 2.24 dtk

Israel mengatakan bukti foto menunjukkan bahwa senjata kimia digunakan dalam serangan, termasuk dalam serangan pada 19 Maret. Kepala Divisi Penelitian Intelijen Militer Israel Brigjen Itai Baron mengatakan bahwa situasi ini terjadi karena pemerintah Suriah menuduh bahwa senjata kimia digunakan dalam serangan.

## Artikel 19: `121011_alonso`

**Ringkasan acuan**

> Pemimpin sementara klasemen pembalap di Formula 1, Fernando Alonso, mengatakan persaingan untuk menjadi juara masih sangat terbuka.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.235 · ROUGE-2: 0.062 · ROUGE-L: 0.176 · BERTScore: 0.724 · waktu: 2.14 dtk

Sebastian Alonso mengatakan, meski Vettel memulai pekan ini dengan juara, mereka tidak akan mengalahkan pembala-pembalap lain.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.069 · ROUGE-2: 0.000 · ROUGE-L: 0.069 · BERTScore: 0.725 · waktu: 1.32 dtk

Sebastian Vettel mengatakan bahwa tim Red Bull akan memulai musim balap 2012.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.143 · ROUGE-2: 0.077 · ROUGE-L: 0.143 · BERTScore: 0.740 · waktu: 1.08 dtk

Sebastian Alonso mengatakan tidak perlu panik melihat kebangkitan tim Red Bull.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.091 · ROUGE-2: 0.031 · ROUGE-L: 0.091 · BERTScore: 0.672 · waktu: 2.58 dtk

Alonso bersaing ketat dengan Vettel, Raikkonen, dan Hamilton di F1. Sebastian Vettel dari Red Bull menempelkan Alonso dengan hanya terpaut empat angka setelah Vettel menjuarai Grand Prix Jepang. Alonso mengatakan bahwa ia tidak perlu panik melihat kebangkitan Vettel. Meski demikian Alonso mengatakan dia tidak perlu panik melihat kebangkitan Vettel.

## Artikel 20: `150428_seni_lukisan_tiruan`

**Ringkasan acuan**

> Sejak bulan Februari lalu, sebuah lukisan tiruan dipamerkan di Galeri Lukisan Dulwich, London tenggara.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.000 · ROUGE-2: 0.000 · ROUGE-L: 0.000 · BERTScore: 0.659 · waktu: 1.19 dtk

Young Woman karya Jean-Honore Fragonard kembali dipajang kembali.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.065 · ROUGE-2: 0.000 · ROUGE-L: 0.065 · BERTScore: 0.683 · waktu: 2.01 dtk

Jean-Honore Fragonard, pelukis karya klasik abad ke-18, telah mengajak pengunjung untuk menemukan lukisan yang asli.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.077 · ROUGE-2: 0.000 · ROUGE-L: 0.077 · BERTScore: 0.676 · waktu: 1.31 dtk

Young Woman karya Jean-Honore Fragonard yang asli diganti dengan versi tiruan.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.088 · ROUGE-2: 0.000 · ROUGE-L: 0.088 · BERTScore: 0.683 · waktu: 2.78 dtk

Karya Jean-Honore Fragonard yang asli dan tiruan Young Woman kini dipajang di Cina. Lukisan asli Young Woman diambil kembali dari tempat penyimpanan, dengan harga £70 atau sekitar Rp1,5 juta dan dibuat di Cina. Tiruan Young Woman dibuat oleh Meishing Oil Painting Manufacture Company, yang mempekerjakan 150 pelukis, dan dibuat untuk pasar internasional.

## Artikel 21: `130417_iptek_hobbit_floris`

**Ringkasan acuan**

> Para ilmuwan Jepang mengatakan spesies kecil manusia purba, yang kerangkanya ditemukan di Pulau Flores mungkin mengecil karena menyesuaikan diri dengan lingkungannya.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.200 · ROUGE-2: 0.000 · ROUGE-L: 0.133 · BERTScore: 0.724 · waktu: 1.06 dtk

Homo floresiensis adalah manusia yang memiliki otak yang kecil.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.133 · ROUGE-2: 0.000 · ROUGE-L: 0.133 · BERTScore: 0.718 · waktu: 0.96 dtk

Homo floresiensis adalah makhluk manusia yang memiliki otak besar.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.323 · ROUGE-2: 0.069 · ROUGE-L: 0.323 · BERTScore: 0.736 · waktu: 0.97 dtk

Homo floresiensis adalah manusia yang pertama kali ditemukan di Flores.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.235 · ROUGE-2: 0.061 · ROUGE-L: 0.147 · BERTScore: 0.726 · waktu: 2.79 dtk

Teori menyebutkan manusia kerdil hobit pindah ke Flores dan mengecil. Makhluk yang disebut homo floresiensis ditemukan tahun 2003. Studi baru yang diterbitkan di *Journal of Royal Society* menyebutkan bahwa kerangka itu berasal dari spesies manusia purba yang mengecil atau "hobit" dalam beberapa generasi melalui proses pengerdilan insuler.

## Artikel 22: `140103_cina_ekstasi_narkoba`

**Ringkasan acuan**

> Sekitar 3.000 polisi Cina dengan dukungan kapal cepat dan helikopter menggerebek desa di bagian selatan yang dikatakan sebagai pusat produksi pil ekstasi.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.303 · ROUGE-2: 0.065 · ROUGE-L: 0.242 · BERTScore: 0.721 · waktu: 1.36 dtk

Desa Boshe di provinsi Guangdong, Cina, menjadi pusat produksi narkoba.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.457 · ROUGE-2: 0.182 · ROUGE-L: 0.400 · BERTScore: 0.803 · waktu: 1.37 dtk

Polisi Cina menggencarkan razia di desa yang dikenal sebagai pusat produksi narkoba.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.194 · ROUGE-2: 0.069 · ROUGE-L: 0.194 · BERTScore: 0.718 · waktu: 0.97 dtk

Desa Boshe, Provinsi Guangdong, menjadi pusat produksi narkoba.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.225 · ROUGE-2: 0.077 · ROUGE-L: 0.175 · BERTScore: 0.709 · waktu: 3.30 dtk

Polisi Cina melakukan razia di desa yang dikenal sebagai pusat produksi narkoba. Mereka menyita tiga ton narkoba dan menangkap 182 orang setelah mengepung Desa Boshe, Provinsi Guangdong. Wakil Direktur Departemen Keamanan Umum Provinsi Guangdong mengatakan bahwa operasi ini melibatkan para saudara laki-laki dan perempuan, serta teman-teman. Surat kabar setempat melaporkan kepala desa dan kepala kepolisian

## Artikel 23: `160210_indonesia_pesawat_tni_jatuh`

**Ringkasan acuan**

> Sebuah pesawat latih TNI AU jatuh di sebuah pemukiman di Malang. Dilaporkan seorang tewas. BBC sedang mengumpulkan informasi lebih jauh.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.372 · ROUGE-2: 0.146 · ROUGE-L: 0.372 · BERTScore: 0.740 · waktu: 3.21 dtk

Pilot pesawat TNI AU yang berada di lapangan udara TNI AU Malang, Jatim, jatuh di sebuah perkampungan padat di kawasan Blimbing, Malang, Jatim.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.474 · ROUGE-2: 0.278 · ROUGE-L: 0.474 · BERTScore: 0.767 · waktu: 1.95 dtk

Sejumlah saksi mata melihat pesawat latih milik TNI AU jatuh di sebuah perkampungan padat di kota Malang, Jatim.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.333 · ROUGE-2: 0.176 · ROUGE-L: 0.222 · BERTScore: 0.724 · waktu: 2.48 dtk

Sejumlah warga kampung padat di Malang, Jatim, mendengar pesawat TNI AU jatuh dan menimpa rumah penduduk.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.269 · ROUGE-2: 0.154 · ROUGE-L: 0.269 · BERTScore: 0.719 · waktu: 2.88 dtk

Sejumlah saksi mata mengatakan bahwa pesawat TNI AU jatuh dan menimpa rumah penduduk di perkampungan padat di kota Malang, Jatim. Sejumlah saksi mata melihat pesawat latih milik TNI AU jatuh di sebuah perkampungan padat di Jalan Laksamana Adisutjipto, Kecamatan Blimbing, Kota Malang, sekitar pukul 10.00 WIB.

## Artikel 24: `130821_rupiah`

**Ringkasan acuan**

> Mata uang rupiah terus melemah terhadap dolar Amerika Serikat dan pada perdangangan Rabu (21/08) bahkan sempat menembus lebih dari Rp11.000 per dolar.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.222 · ROUGE-2: 0.160 · ROUGE-L: 0.222 · BERTScore: 0.718 · waktu: 0.65 dtk

Rupiah terus melemah.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.333 · ROUGE-2: 0.118 · ROUGE-L: 0.333 · BERTScore: 0.749 · waktu: 1.42 dtk

Kurs mata uang Indonesia (Rupiah) terjadi pada harga 11.200 per dolar.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.143 · ROUGE-2: 0.077 · ROUGE-L: 0.143 · BERTScore: 0.676 · waktu: 0.68 dtk

Rupiah terus terjadi penurunan.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.060 · ROUGE-2: 0.000 · ROUGE-L: 0.060 · BERTScore: 0.657 · waktu: 2.38 dtk

Penaikan dolar di Jakarta terjadi di beberapa negara berkembang lain di Asia, termasuk di Indonesia. Di sisi, kurs dolar di Jakarta menurun seiring waktu. Pemimpin ekonom, Andiko Sati Purwoko, mengatakan bahwa kebijakan Bank Indonesia akan segera mengumumkan paket kebijakan untuk mengatasi gejolak pasar.

## Artikel 25: `150623_majalah_interstellar_sekolah`

**Ringkasan acuan**

> Film Interstellar seharusnya diputar pada mata pelajaran ilmu pengetahuan di sekolah, demikian diusulkan sebuah jurnal ilmiah.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.154 · ROUGE-2: 0.083 · ROUGE-L: 0.154 · BERTScore: 0.759 · waktu: 1.11 dtk

Lubang hitam dalam film Interstellar dibuat oleh para ahli fisika.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.059 · ROUGE-2: 0.000 · ROUGE-L: 0.059 · BERTScore: 0.668 · waktu: 1.80 dtk

Lubang hitam di bumi yang terbuka di bumi ini akan menjadi tempat yang terbaik untuk mempelajari lubang hitam.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.167 · ROUGE-2: 0.059 · ROUGE-L: 0.167 · BERTScore: 0.766 · waktu: 2.01 dtk

Dr David Jackson mengatakan bahwa film Interstellar akan diperlihatkan dalam kelas kelas fisika untuk menyampaikan makalah ilmiah yang akan diterbitkan.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.094 · ROUGE-2: 0.032 · ROUGE-L: 0.094 · BERTScore: 0.679 · waktu: 2.56 dtk

Artikel ini membahas bahwa film *Interstellar* dibintangi oleh Matthew McConaughey, Anne Hathaway, Jessica Chastain, dan Sir Michael Caine, serta temuan yang disampaikan oleh Dr David Jackson dalam makalah ilmiah. Para ahli memastikan bahwa penggambaran "lubang ulat" dalam film tersebut akurat secara ilmiah, dan penerbitan makalah ini berjalan lancar.

## Artikel 26: `121005_kenya_gugatan`

**Ringkasan acuan**

> Pengadilan Tinggi Inggris memutuskan tiga warga Kenya yang disiksa oleh penguasa kolonial Inggris boleh meneruskan gugatannya kepada pemerintah Inggris.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.286 · ROUGE-2: 0.061 · ROUGE-L: 0.171 · BERTScore: 0.749 · waktu: 2.26 dtk

Pemerintah Inggris akan mengajukan banding atas keputusan terbaru pengadilan Kenya untuk menggugat tahanan yang telah meninggal.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.389 · ROUGE-2: 0.176 · ROUGE-L: 0.389 · BERTScore: 0.790 · waktu: 2.19 dtk

Pemerintah Inggris mengakui bahwa pasukannya melakukan penyiksaan atas tahanan warga Kenya yang telah diperlakukan oleh pemerintah Inggris.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.138 · ROUGE-2: 0.074 · ROUGE-L: 0.138 · BERTScore: 0.761 · waktu: 1.39 dtk

Pemerintah Inggris mengakui bahwa pasukannya melakukan penyiksaan atas para tahanan.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.194 · ROUGE-2: 0.100 · ROUGE-L: 0.194 · BERTScore: 0.721 · waktu: 2.58 dtk

Seorang warga Kenya yang menggugat pemerintah Inggris telah meninggal. Dalam keputusan tersebut, hakim McCombe mengatakan bahwa penggugat memiliki kasus yang tepat untuk diperiksa. Pemerintah Inggris telah mengakui bahwa pasukannya melakukan penyiksaan atas para tahanan namun mengatakan akan mengajukan banding atas keputusan terbaru ini.

## Artikel 27: `120810_marty_yangjiechi_southchinasea`

**Ringkasan acuan**

> Menlu Indonesia Marty Natalegawa dan Menlu Cina Yang Jiechi sepakat untuk mengedepankan diplomasi dalam menyelesaikan sengketa laut Cina Selatan, yang dipertikaikan Cina dan sejumlah negara ASEAN.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.383 · ROUGE-2: 0.133 · ROUGE-L: 0.213 · BERTScore: 0.729 · waktu: 2.64 dtk

Kementrian Luar Negeri Cina dan Indonesia akan melibatkan dalam kerjasama diplomatik untuk membangun rasa percaya dan kerjasama di Laut Cina Selatan.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.345 · ROUGE-2: 0.107 · ROUGE-L: 0.172 · BERTScore: 0.710 · waktu: 4.12 dtk

Kementrian Luar Negeri (LUN) Menlu Yan Jiechi, yang akan menghadiri pertemuan antar negara ASEAN, akan mengatakan, "Cina akan membangun rasa saling percaya, meningkatkan kerjasama, memelihara perdamaian dan stabilitas di Laut Cina Selatan."

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.286 · ROUGE-2: 0.100 · ROUGE-L: 0.143 · BERTScore: 0.716 · waktu: 1.88 dtk

Kementrian Luar Negeri Menlu Yan Jiechi dan Menlu Marty Natalegawa akan bertemu di Kementrian Luar Negeri.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.230 · ROUGE-2: 0.068 · ROUGE-L: 0.131 · BERTScore: 0.690 · waktu: 2.27 dtk

Menlu Cina Yan Jiechi disambut oleh Menlu Marty Natalegawa sebelumnya, dalam pertemuan dengan Presiden Susilo Bambang Yudhoyono. Hal itu ditegaskan dalam pernyataan pers, bahwa kerjasama bilateral di Kementrian Luar Negeri, Jakarta, Jumat (10/08) sore.

## Artikel 28: `150821_olahraga_vangaal_woodward`

**Ringkasan acuan**

> Manajer Manchester United Louis Van Gaal menyatakan ia 'percaya' pada wakil presiden klub, Ed Woodward dalam urusan transfer pemain.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.353 · ROUGE-2: 0.125 · ROUGE-L: 0.353 · BERTScore: 0.799 · waktu: 1.62 dtk

Manajer United City, Louis Van Gaal, tidak akan mengganti pemain yang akan bergabung ke club.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.103 · ROUGE-2: 0.000 · ROUGE-L: 0.103 · BERTScore: 0.723 · waktu: 1.81 dtk

Manchester City akan mengurangi pemain asal Barcelona, Pedro Gomez, untuk menggantikan pemain asal yang akan berada di musim panas ini.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.229 · ROUGE-2: 0.061 · ROUGE-L: 0.229 · BERTScore: 0.745 · waktu: 1.68 dtk

Manajer United tidak ingin memperkenalkan transfer pemain yang akan dianggap sebagai "pemain yang tidak akan diturunkan".

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.262 · ROUGE-2: 0.136 · ROUGE-L: 0.197 · BERTScore: 0.715 · waktu: 2.22 dtk

Louis Van Gaal tidak ingin mencampuri urusan transfer pemain. Sejauh ini Woodward telah mengawasi negosiasi mendatangkan pemain Matteo Darmian, Memphis Depay, Morgan Schneiderlin dan Bastian Schweinsteiger. Namun United kehilangan target mereka, Pedro, pemain asal Barcelona yang bergabung ke Chelsea dan Nicolas Otamendi.

## Artikel 29: `130701_pakistan_quetta`

**Ringkasan acuan**

> Kota Quetta berkabung selama satu hari menyusul rangkaian kekerasan di Pakistan yang menewaskan sedikitnya 56 orang.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.207 · ROUGE-2: 0.000 · ROUGE-L: 0.138 · BERTScore: 0.689 · waktu: 1.76 dtk

Pemakaman para korban di Quetta, Pakistan, akan dilaksanakan pada Senin (1 Juli) besok.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.167 · ROUGE-2: 0.000 · ROUGE-L: 0.167 · BERTScore: 0.724 · waktu: 0.95 dtk

Kawasan Quetta, Pakistan, akan menjadi sasaran serangan bom.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.143 · ROUGE-2: 0.000 · ROUGE-L: 0.143 · BERTScore: 0.728 · waktu: 1.30 dtk

Kawasan Hazara di Quetta akan tutup di tengah persiapan pemakaman para korban.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.091 · ROUGE-2: 0.000 · ROUGE-L: 0.091 · BERTScore: 0.687 · waktu: 1.55 dtk

Perkantoran dan pertokoan dan pertokoan di Quetta menghadapi penutupan di masa krisis. Pemakaman para korban di Quetta terjadi di tengah persiapan pemakaman, dengan pasar di Quetta juga tutup.

## Artikel 30: `indonesia-45117963`

**Ringkasan acuan**

> Facebook menyatakan pihaknya "menyesal" karena banyak posting tentang gempa yang menewaskan ratusan orang di Lombok, muncul dengan pesannya dihiasi balon dan potongan kertas warna-warni.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.200 · ROUGE-2: 0.000 · ROUGE-L: 0.200 · BERTScore: 0.725 · waktu: 0.76 dtk

Facebook mengunggah gempa di Indonesia.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.158 · ROUGE-2: 0.000 · ROUGE-L: 0.158 · BERTScore: 0.717 · waktu: 1.79 dtk

Facebook menghentikan fitur yang menyatakan "selamat ulang" dalam konten yang berisi pesan "congratulations".

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.069 · ROUGE-2: 0.000 · ROUGE-L: 0.069 · BERTScore: 0.702 · waktu: 0.56 dtk

Facebook menghentikan fitur tersebut.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.167 · ROUGE-2: 0.024 · ROUGE-L: 0.119 · BERTScore: 0.672 · waktu: 3.30 dtk

Gempa berkekuatan 7 Skala Richter terjadi hari Minggu (05/08) di Indonesia, dengan data jumlah korban tewas antara 150-an hingga lebih dari 330-an. Data jumlah korban tewas masih bervariasi, karena berbagai lembaga menggunakan sumber data yang berbeda. Berbagai pesan keprihatinan terkait gempa yang diunggah di Facebook mendapat hiasan tanda ceria dan gembira, karena adanya penggunaan kata "selamat."

## Artikel 31: `dunia-47910980`

**Ringkasan acuan**

> Kementerian Luar Negeri Brunei menyatakan hukum rajam sampai meninggal untuk LGBT dilakukan untuk "pencegahan" dan bukan untuk "hukuman".

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.258 · ROUGE-2: 0.000 · ROUGE-L: 0.194 · BERTScore: 0.737 · waktu: 2.00 dtk

Brunei mengatakan hukuman syariat akan diterapkan untuk kelompok lesbian, gay, biseksual dan transgender.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.111 · ROUGE-2: 0.000 · ROUGE-L: 0.111 · BERTScore: 0.725 · waktu: 2.29 dtk

Sultan Brunei Hassanal Bolkiah mengatakan bahwa hukuman syariat yang akan diterapkan pada 2014 akan diterapkan pada pemerintah Brunei.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.343 · ROUGE-2: 0.061 · ROUGE-L: 0.286 · BERTScore: 0.749 · waktu: 2.35 dtk

Brunei mengatakan akan mengeluarkan pernyataan bahwa hukuman rajam akan dilakukan untuk kelompok lesbian, gay, biseksual dan transgender.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.400 · ROUGE-2: 0.151 · ROUGE-L: 0.327 · BERTScore: 0.774 · waktu: 2.55 dtk

Sultan Brunei Hassanal Bolkiah mengatakan bahwa pernyataan kementerian mengeluarkan pernyataan terkait hukuman rajam untuk kelompok lesbian, gay, biseksual dan transgender. Menteri Luar Negeri Brunei, Erywan Yusof, menyatakan bahwa hukuman Syariat itu "dipusatkan pada pencegahan dan bukan hukuman."

## Artikel 32: `150321_facebook_bunuhdiri_palsu`

**Ringkasan acuan**

> Seorang lelaki yang memampang ancaman palsu untuk bunuh diri di Facebook, telah ditahan dan dikirim ke rumah sakit jiwa selama hampir tiga hari.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.200 · ROUGE-2: 0.071 · ROUGE-L: 0.133 · BERTScore: 0.769 · waktu: 1.00 dtk

Facebook akan menguji program pencegahan bunuh diri.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.242 · ROUGE-2: 0.065 · ROUGE-L: 0.182 · BERTScore: 0.758 · waktu: 1.15 dtk

Facebook meminta penggunaan Facebook untuk menguji program pencegahan bunuh diri.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.188 · ROUGE-2: 0.067 · ROUGE-L: 0.188 · BERTScore: 0.755 · waktu: 1.07 dtk

Facebook meminta pengguna menguji program pencegahan bunuh diri Facebook.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.179 · ROUGE-2: 0.053 · ROUGE-L: 0.154 · BERTScore: 0.693 · waktu: 3.47 dtk

Menurut Shane Tusch, Facebook tidak perlu terlibat dalam pencegahan bunuh diri. Ia mengatakan bahwa Facebook telah memblokir akunnya. Facebook juga telah memperpanjang program pencegahan bunuh diri pada bulan Februari, yang memungkinkan pembaca untuk menandai posting yang menunjukkan seseorang mungkin berkecenderungan bunuh diri. Pengecekan Tugas Facebook memungkinkan pembaca untuk menandai posting "kecenderungan bunuh diri" dan memperbaiki

## Artikel 33: `140512_india_pemilu`

**Ringkasan acuan**

> Pemungutan suara hari terakhir dalam pemilu di India telah selesai dan jajak pendapat menunjukkan koalisi oposisi yang dipimpin BJP menang.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.138 · ROUGE-2: 0.000 · ROUGE-L: 0.069 · BERTScore: 0.741 · waktu: 1.20 dtk

India akan memilih sebanyak 500 juta orang untuk pemilu.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.160 · ROUGE-2: 0.000 · ROUGE-L: 0.080 · BERTScore: 0.706 · waktu: 0.75 dtk

India akan menghadiri pemilu 2014.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.154 · ROUGE-2: 0.000 · ROUGE-L: 0.077 · BERTScore: 0.732 · waktu: 0.85 dtk

India akan mengumumkan hasil pemilu 2014.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.206 · ROUGE-2: 0.061 · ROUGE-L: 0.147 · BERTScore: 0.730 · waktu: 2.68 dtk

Pemilu marathon di India dimulai sejak 7 April lalu, dibagi sembilan tahap demi keamanan. BJP yang dipimpin oleh Narendra Modi memimpin pemilu, dan para analis memperingatkan bahwa pemilu ini akan dihitung pada tanggal 16 Mei. Hasilnya akan diumumkan pada 17 Mei, dengan jumlah pemilih mencapai rekor 66,38%.

## Artikel 34: `dunia-37935296`

**Ringkasan acuan**

> Ribuan pengunjuk rasa turun ke jalan-jalan di sejumlah kota di Amerika Serikat untuk memprotes kemenangan Donald Trump di pemilihan presiden dengan mengalahkan Hillary Clinton.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.286 · ROUGE-2: 0.121 · ROUGE-L: 0.286 · BERTScore: 0.730 · waktu: 1.13 dtk

Presiden Amerika Serikat Donald Trump mengganti Barack Obama sebagai presiden.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.216 · ROUGE-2: 0.057 · ROUGE-L: 0.108 · BERTScore: 0.732 · waktu: 1.32 dtk

Trump telah menyerahkan seruan untuk memprotes kebijakan yang diterima oleh rakyat Amerika.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.242 · ROUGE-2: 0.065 · ROUGE-L: 0.182 · BERTScore: 0.770 · waktu: 0.88 dtk

Presiden Barack Obama mengatakan akan memprotes kemenangan Trump.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.177 · ROUGE-2: 0.052 · ROUGE-L: 0.101 · BERTScore: 0.683 · waktu: 2.76 dtk

Pertahanan membakar bonek Donald Trump di Los Angeles. Demo besar di Chicago menuntut rakyat Amerika menerima pilpres yang digelar hari Selasa (08/11). Aksi protes di New York Times memberitakan polisi menahan 15 orang dalam aksi ini. Aksi protes di Oakland, California, beberapa demonstran memecah kaca toko dan melempar benda ke politi antihuru-hara.

## Artikel 35: `140210_adebayor_villasboas`

**Ringkasan acuan**

> Penyerang Tottenham Hotspur, Emmanuel Adebayor, mengungkapkan dirinya pernah mengkritik mantan manajer Andre Villas-Boas secara terbuka di depan para pemain Spurs.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.267 · ROUGE-2: 0.071 · ROUGE-L: 0.267 · BERTScore: 0.775 · waktu: 1.29 dtk

Adebayor mengatakan taktik Villas-Boas tidak akan membantu Spurs.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.267 · ROUGE-2: 0.071 · ROUGE-L: 0.267 · BERTScore: 0.775 · waktu: 1.13 dtk

Adebayor mengatakan taktik Villas-Boas tidak akan membantu Spurs.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.267 · ROUGE-2: 0.071 · ROUGE-L: 0.267 · BERTScore: 0.780 · waktu: 1.07 dtk

Adebayor meminta manajer Villas-Boas untuk tidak membantu tim.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.195 · ROUGE-2: 0.051 · ROUGE-L: 0.195 · BERTScore: 0.764 · waktu: 1.14 dtk

Adebayor mengatakan bahwa taktik Villas-Boas tidak membantu penampilan Spurs. Adebayor menegaskan bahwa kritik ini tidak akan membantu tim Spurs.

## Artikel 36: `131225_hull_mu`

**Ringkasan acuan**

> Manajer Manchester United, David Moyes, mengatakan timnya tidak akan menganggap enteng Hull, saat kedua tim bertemu di lanjutan Liga Primer, hari Kamis (26/12).

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.194 · ROUGE-2: 0.000 · ROUGE-L: 0.129 · BERTScore: 0.705 · waktu: 0.93 dtk

Hull akan menggandakan poin di kandang Liverpool.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.000 · ROUGE-2: 0.000 · ROUGE-L: 0.000 · BERTScore: 0.676 · waktu: 0.87 dtk

Liverpool menghadapi Liverpool dalam pertandingan pertandingan pertama mereka.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.242 · ROUGE-2: 0.000 · ROUGE-L: 0.182 · BERTScore: 0.703 · waktu: 1.07 dtk

Hull United akan menggandakan kebobolan di delapan pertandingan terakhir.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.211 · ROUGE-2: 0.000 · ROUGE-L: 0.105 · BERTScore: 0.665 · waktu: 2.50 dtk

Tim asuhan Moyes saat ini berada di papan tengah, tertinggal delapan poin dari Liverpool, hanya tiga kali kebobolan di delapan pertandingan. Hull memiliki rekor mengesankan di kandang sendiri, hanya tiga kali kebobolan di delapan pertandingan. Bruce mengatakan United di bawah Moyes akan kembali menjadi tim yang sangat ditakuti, seperti saat diasuh Ferguson.

## Artikel 37: `olahraga-38704769`

**Ringkasan acuan**

> Dua bekas juara Australia Terbuka, Rafael Nadal dan Serena Williams, lolos dari hadangan lawan-lawannya untuk melaju ke babak keempat Grand Slam Pertama 2017 ini.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.286 · ROUGE-2: 0.121 · ROUGE-L: 0.171 · BERTScore: 0.725 · waktu: 1.18 dtk

Nadal akan menghadapi Gael Monfils di Grand Slam Australia Terbuka.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.186 · ROUGE-2: 0.000 · ROUGE-L: 0.140 · BERTScore: 0.719 · waktu: 2.24 dtk

Nadal Sastari, yang menjadi juara Prancis Terbuka 2014, akan menghadapi remaja Prancis yang mengalahkan dia di set keempat.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.129 · ROUGE-2: 0.069 · ROUGE-L: 0.129 · BERTScore: 0.704 · waktu: 0.76 dtk

Nadal akan menghadapi Rafael Nadal setelahnya.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.222 · ROUGE-2: 0.077 · ROUGE-L: 0.148 · BERTScore: 0.664 · waktu: 1.63 dtk

Nadal memenangkan satu-satunya gelar Australia TErbuka, pada delapan tahun lalu. Rafael Nadal yang menjuarinya sebagai juara enam kali, mengalahkan remaja Zverev dalam lima set setelah ketinggalan dua set.

## Artikel 38: `131117_dakwaan_musharraf`

**Ringkasan acuan**

> Mantan penguasa militer Pakistan, Jenderal Pervez Musharraf, akan diadili dengan dakwaan pengkhianatan.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.500 · ROUGE-2: 0.286 · ROUGE-L: 0.500 · BERTScore: 0.804 · waktu: 0.74 dtk

Jenderal Musharraf akan diadili.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.476 · ROUGE-2: 0.105 · ROUGE-L: 0.381 · BERTScore: 0.798 · waktu: 1.07 dtk

Jenderal Musharraf Khan akan diadili oleh Mahkamah Agung Pakistan.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.364 · ROUGE-2: 0.200 · ROUGE-L: 0.364 · BERTScore: 0.786 · waktu: 1.38 dtk

Jenderal Musharraf akan diadili karena mengumumkan keadaan darurat ketika berkuasa.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.146 · ROUGE-2: 0.000 · ROUGE-L: 0.146 · BERTScore: 0.728 · waktu: 1.92 dtk

Jenderal Musharraf diadili karena berlakukan keadaan darurat saat berkuasa. Khalid Nisar Ali Khan mengatakan pemerintah telah selesai melakukan penyelidikan terhadap Jenderal Musharraf dan keputusan ini diambil untuk kepentingan nasional.

## Artikel 39: `160328_dunia_belgia_faycal`

**Ringkasan acuan**

> Seorang pria yang dikenal sebagai Faycal C, satu-satunya orang yang ditangkap dan didakwa terlibat dalam penyerangan di Brussels, telah dibebaskan karena kurangnya bukti-bukti.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.341 · ROUGE-2: 0.205 · ROUGE-L: 0.341 · BERTScore: 0.785 · waktu: 2.50 dtk

Seorang pria berusia 30 tahun yang dikenal sebagai "Faycal Cheffou" dinyatakan dibebaskan oleh dewan magistrat Belgia.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.340 · ROUGE-2: 0.157 · ROUGE-L: 0.264 · BERTScore: 0.743 · waktu: 2.93 dtk

Polisi Belgium mengatakan tersangka yang dikenal sebagai "Negara Islam" (ISIS) telah mengambil tindak tegas terhadap seorang pria yang dikenal sebagai salah satu penyerang bom di bandar udara Zaventem.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.381 · ROUGE-2: 0.200 · ROUGE-L: 0.381 · BERTScore: 0.755 · waktu: 1.61 dtk

Seorang pria yang dikenal sebagai salah satu dari tiga tersangka dalam serangan bom di bandar udara Zaventem.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.179 · ROUGE-2: 0.000 · ROUGE-L: 0.119 · BERTScore: 0.688 · waktu: 2.28 dtk

Foto yang disebarkan oleh Polisi Federal Belgia memperlihatkan tersangka ketiga yang terekam di kamera pengamat CCTV di bandar udara Zaventem. Polisi merilis foto ini dalam upaya mengetahui identitas pria ini. Media massa di Belgia menyebutkan nama lengkap pria itu adalah Faycal Cheffou.

## Artikel 40: `150122_trensosial_savekpk`

**Ringkasan acuan**

> Berita penangkapan Wakil Ketua Komisi Pemberantasan Korupsi (KPK) Bambang Widjojanto langsung memicu reaksi besar di media sosial.

### full_lora

Route G2–G6: `[1, 1, 1, 1, 1]`  
ROUGE-1: 0.077 · ROUGE-2: 0.000 · ROUGE-L: 0.077 · BERTScore: 0.655 · waktu: 1.11 dtk

Tagar #SaveKPK menjadi topik paling populer di Twitter Indonesia.

### static_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.333 · ROUGE-2: 0.214 · ROUGE-L: 0.267 · BERTScore: 0.749 · waktu: 1.73 dtk

KPK (Ketua Komisi Pemberantasan Korupsi) menangkap dua orang yang dugaan rekayasa keterangan palsu.

### router_lora

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.067 · ROUGE-2: 0.000 · ROUGE-L: 0.067 · BERTScore: 0.603 · waktu: 2.07 dtk

Tagar #SaveKPK, #SavePOLRIKPK, dan #SavePOLRIKPK, serta #SavePOLRIKPK, menjadi topik paling populer di Indonesia.

### router_only

Route G2–G6: `[1, 1, 0, 1, 1]`  
ROUGE-1: 0.075 · ROUGE-2: 0.000 · ROUGE-L: 0.025 · BERTScore: 0.585 · waktu: 3.43 dtk

Tanda pagar #SaveKPK sudah digunakan lebih dari 43.000 tweet dalam tiga jam terakhir dan menjadi topik paling terpopuler di Indonesia. Selain itu tagar #SavePOLRIKPK, sebagai seruan untuk menyelamatkan dua instiusi tersebut juga banyak dipakai, dengan lebih dari 13.000 kicauan dalam 24 jam terakhir. Kata kunci lain yang digunakan adalah Cicak vs Buaya, KPK vs POLRI, Penangkapan BW, serta #WhereAreYouJokowi, yang mem
