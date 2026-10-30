def baca_data(nama_file):
	data = []

	try:
		with open(nama_file, "r", encoding="utf-8") as file:
			for nomor_baris, baris in enumerate(file, start=1):
				baris = baris.strip()
				if not baris:
					continue

				bagian = baris.split(",")
				if len(bagian) != 2:
					print(f"Baris {nomor_baris} dilewati: format harus NIM,nilai.")
					continue

				nim, teks_nilai = (kolom.strip() for kolom in bagian)
				if not nim:
					print(f"Baris {nomor_baris} dilewati: NIM tidak boleh kosong.")
					continue

				try:
					nilai = float(teks_nilai)
				except ValueError:
					print(f"Baris {nomor_baris} dilewati: nilai '{teks_nilai}' bukan angka.")
					continue

				data.append((nim, nilai))
	except FileNotFoundError:
		print(f"File input tidak ditemukan: {nama_file}")
		return None

	return data


def tulis_rekap(nama_file, data):
	jumlah_data = len(data)
	jumlah_lulus = sum(nilai >= 60 for _, nilai in data)

	if data:
		rata_rata = sum(nilai for _, nilai in data) / jumlah_data
		nilai_minimum = min(nilai for _, nilai in data)
		nilai_maksimum = max(nilai for _, nilai in data)
		teks_rata_rata = f"{rata_rata:.2f}"
		teks_minimum = f"{nilai_minimum:g}"
		teks_maksimum = f"{nilai_maksimum:g}"
	else:
		teks_rata_rata = "Tidak tersedia"
		teks_minimum = "Tidak tersedia"
		teks_maksimum = "Tidak tersedia"

	with open(nama_file, "w", encoding="utf-8") as file:
		file.write("REKAP NILAI\n")
		file.write(f"Jumlah data valid: {jumlah_data}\n")
		file.write(f"Rata-rata: {teks_rata_rata}\n")
		file.write(f"Nilai minimum: {teks_minimum}\n")
		file.write(f"Nilai maksimum: {teks_maksimum}\n")
		file.write(f"Jumlah lulus (nilai >= 60): {jumlah_lulus}\n")

	return jumlah_data, teks_rata_rata, teks_minimum, teks_maksimum, jumlah_lulus


input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

data_nilai = baca_data(input_file)
if data_nilai is not None:
	ringkasan = tulis_rekap(output_file, data_nilai)
	jumlah_data, rata_rata, nilai_minimum, nilai_maksimum, jumlah_lulus = ringkasan
	print(f"Rekap berhasil ditulis ke {output_file}")
	print(f"Jumlah data valid: {jumlah_data}")
	print(f"Rata-rata: {rata_rata}")
	print(f"Nilai minimum: {nilai_minimum}")
	print(f"Nilai maksimum: {nilai_maksimum}")
	print(f"Jumlah lulus (nilai >= 60): {jumlah_lulus}")
