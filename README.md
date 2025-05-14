# rename-file-folder

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/jhonrylewis/rename-file-folder)](https://github.com/jhonrylewis/rename-file-folder/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/jhonrylewis/rename-file-folder)](https://github.com/jhonrylewis/rename-file-folder/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/jhonrylewis/rename-file-folder)](https://github.com/jhonrylewis/rename-file-folder/issues)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.1%20adopted-ff69b4.svg)](https://www.contributor-covenant.org/version/2/1/code_of_conduct/)
[![Last Commit](https://img.shields.io/github/last-commit/jhonrylewis/rename-file-folder)](https://github.com/jhonrylewis/rename-file-folder/commits/main)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/) <br>

> Skrip Python sederhana untuk mengganti nama file dalam folder secara otomatis berdasarkan pola tertentu.

<p align="center">
  <img src="https://via.placeholder.com/150?text=Rename+Files" alt="Logo Proyek" width="150">
</p>

<br>

## 🚀 Fitur Utama

* Mengganti nama banyak file sekaligus.
* Fleksibel dalam menentukan pola penggantian nama.
* Mudah digunakan melalui *command line*.
* Mendukung berbagai jenis operasi penggantian nama (misalnya, menambahkan awalan, mengganti kata, dll.).

## 🛠️ Instalasi

1.  **Prasyarat:**
    * Python 3.7 atau lebih tinggi terinstal di sistem Anda.

2.  **Klon Repositori:**
    ```bash
    git clone [https://github.com/jhonrylewis/rename-file-folder.git](https://github.com/jhonrylewis/rename-file-folder.git)
    cd rename-file-folder
    ```

3.  **Tidak ada dependensi eksternal yang diperlukan untuk skrip dasar ini.** Jika Anda menambahkan fitur yang memerlukan pustaka tambahan, sebutkan di sini dan tambahkan file `requirements.txt`.

## 💻 Penggunaan

Jelaskan cara menggunakan skrip `rename-file-folder.py`.

```bash
python rename-file-folder.py <path_ke_folder> <pola_lama> <pola_baru>
```

* `<path_ke_folder>`: Jalur ke folder yang berisi file yang ingin diubah namanya. Contoh: `E:/DATA/DONE` atau `/home/user/files`.
* `<pola_lama>`: Teks atau pola yang ingin Anda ganti dalam nama file.
* `<pola_baru>`: Teks baru yang akan menggantikan `<pola_lama>`.

**Contoh:**

Untuk mengganti semua spasi dalam nama file di folder `E:/DATA/DONE` dengan garis bawah:

```bash
python rename-file-folder.py "path/project/anda" " " "_"
```

Untuk menambahkan awalan "gambar-" ke semua file `.jpg` di folder saat ini:

```bash
python rename-file-folder.py "." "^(.*\.jpg)$" "gambar-$1" -regex
```

**Opsi Tambahan (jika ada):**

* `-regex` atau `--regular-expression`: Aktifkan penggunaan ekspresi reguler untuk pola pencarian.

## 🧪 Contoh

Misalkan Anda memiliki file dengan nama:

```
file dengan spasi.txt
contoh lainnya.pdf
dokumen penting.docx
```

Setelah menjalankan perintah:

```bash
python rename-file-folder.py "." " " "_"
```

Nama file akan berubah menjadi:

```
file_dengan_spasi.txt
contoh_lainnya.pdf
dokumen_penting.docx
```

## 📚 Dokumentasi

Untuk informasi lebih lanjut tentang penggunaan ekspresi reguler atau opsi lanjutan, silakan lihat [tautan ke dokumentasi (jika ada)].

## 🤝 Kontribusi

Kontribusi dipersilakan! Silakan *fork* repositori dan buat *Pull Request*. Untuk perubahan besar, mohon diskusikan terlebih dahulu melalui *issues*.

## 🛡️ Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat file [LICENSE](https://github.com/jhonrylewis/rename-file-folder/blob/main/LICENSE) untuk detailnya.

## 🙏 Ucapan Terima Kasih

Terima kasih kepada komunitas *open source* atas inspirasi dan alat-alat yang bermanfaat.

## 📧 Kontak

[Alamat Email Anda (jika ingin dicantumkan)]
[Profil GitHub Anda: https://github.com/jhonrylewis](https://github.com/jhonrylewis)

-----

Dibuat dengan ❤️
