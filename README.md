# Pertemuan 12 - File I/O dan Error Handling

Nama: ...  
NIM: ...  
Kelas: ...

## Tujuan

Membaca, memvalidasi, mengolah, dan menulis data file dengan Python.

## Format File Input

File `data/nilai.txt` berisi satu record per baris dengan format `NIM,nilai`:

```text
A001,85
A002,78
```

Baris kosong dilewati. Baris dengan format salah atau nilai yang tidak dapat dikonversi ke `float` dilaporkan dan dilewati.

## Cara Menjalankan

Jalankan dari folder utama proyek:

```bash
python3 tugas/rekap_nilai_file.py
```

Program menampilkan ringkasan di terminal dan menulisnya ke `data/hasil_rekap.txt`. Nilai minimal 60 termasuk lulus.

## Error yang Ditangani

- `FileNotFoundError`: menampilkan pesan bahwa file input tidak ditemukan dan tidak membuat file rekap.
- `ValueError`: melaporkan nilai yang bukan angka, melewati baris tersebut, dan melanjutkan pemrosesan record lain.

## Test Case

| Kondisi | Hasil yang diharapkan | Hasil aktual | Status |
| --- | --- | --- | --- |
| Data contoh: lima nilai numerik dan `A004,abc` | Lima record valid diproses; rata-rata 83.40, minimum 74, maksimum 92, lulus 5 | Ringkasan sesuai; `A004,abc` dilaporkan dan dilewati | LULUS |
| File `nilai.txt` tidak tersedia | Pesan file tidak ditemukan; program tidak crash | Pesan ditampilkan, program selesai tanpa traceback dan tanpa membuat rekap | LULUS |
| Nilai invalid `A011,abc` | Baris invalid dilewati; record lain diproses | Baris dilaporkan; dua record valid tetap direkap | LULUS |
| Terdapat baris kosong | Baris kosong dilewati | Baris kosong dilewati; jumlah record valid tetap 2 | LULUS |
| Nilai tepat 60 | Dihitung lulus | Dari nilai 60 dan 40, jumlah lulus adalah 1 | LULUS |

## Refleksi

Error `ValueError` ditemukan saat teks nilai `abc` dikonversi menjadi `float`. Program menangkap error tersebut untuk baris terkait, menampilkan pesan, lalu melewati baris invalid agar record lain tetap diproses.
