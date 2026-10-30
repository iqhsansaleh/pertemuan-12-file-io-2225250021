with open("data/nilai.txt", "r", encoding="utf-8") as file:
	for nomor_baris, baris in enumerate(file, start=1):
		baris = baris.strip()
		if not baris:
			continue

		bagian = baris.split(",")
		if len(bagian) != 2 or not bagian[0].strip() or not bagian[1].strip():
			print(f"Format baris {nomor_baris} tidak valid.")
			continue

		nim, teks_nilai = bagian
		try:
			nilai = float(teks_nilai)
		except ValueError:
			print(f"Nilai pada baris {nomor_baris} bukan angka.")
			continue

		print(nim.strip(), nilai)
