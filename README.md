# Pertemuan 10 String dan Pengolahan Teks[cite: 28]

Nama: Sheila Ni'matul Hasanah
NIM: 2225250138
Kelas: 3B

## Tujuan
Mengolah dan menormalisasi data teks dengan string Python.

## Cara Menjalankan
python3 tugas/normalisasi_data_mahasiswa.py

## Algoritma
1. Membaca input string nama lengkap mahasiswa dan kode kelas.
2. Membersihkan spasi berlebih serta menyeragamkan kapitalisasi nama menjadi format *title case* melalui fungsi `normalisasi_nama`.
3. Memecah nama menjadi list kata untuk menghitung jumlah kata dan membentuk inisial huruf depan dari setiap kata melalui fungsi `buat_inisial`.
4. Membersihkan, mengubah huruf menjadi kapital (`upper`), serta mengganti spasi pada kode kelas dengan tanda hubung (`-`) melalui fungsi `normalisasi_kode`.
5. Menampilkan seluruh hasil normalisasi secara rapi dan terstruktur.

## Test Case
| Input Nama | Input Kode | Hasil Utama | Status |
| :--- | :--- | :--- | :--- |
| `aan hendrayana` | `pmat a 2026` | `Aan Hendrayana \| PMAT-A-2026 \| AH` | Sesuai |
| `fATHIYYAH MUTHMAINNAH` | `kelas b` | `Fathiyyah Muthmainnah \| KELAS-B \| FM` | Sesuai |
| `BUDI` | `pmtk 01` | `Budi \| PMTK-01 \| B` | Sesuai |
| `siti nur aisyah` | `kelas c` | `Siti Nur Aisyah \| KELAS-C \| SNA` | Sesuai |

## Refleksi
- **Masalah Teks yang Ditemukan**: Adanya spasi ganda/berlebih di antara kata serta inkonsistensi penggunaan huruf besar dan kecil pada input teks.
- **Cara Memperbaikinya**: Menerapkan kombinasi method `.strip()`, `.split()`, dan `".join()"` untuk merapikan spasi, serta menggunakan `.title()` dan `.upper()` untuk menyeragamkan format tampilan teks.