import csv
import os

os.system("cls" if os.name == "nt" else "clear")

while True:
    print("\n=== Pencatatan Nilai Mahasiswa ===")
    print("1. Lihat Nilai")
    print("2. Tambah Nilai")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("\n=== Data Nilai Mahasiswa ===")

        data = []

        with open("nilai.csv", mode='r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")

            for row in csv_reader:
                data.append(row)

        for row in data:
            print(row)

    elif pilihan == "2":
        print("\n=== Tambah Data Nilai ===")

        nim = input("NIM: ")
        nama = input("Nama: ")
        mata_kuliah = input("Mata Kuliah: ")
        nilai = input("Nilai: ")

        with open("nilai.csv", mode='a',newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            writer.writerow([nim, nama, mata_kuliah, nilai])

        print("Data nilai berhasil ditambah")

    elif pilihan == "3":
        print("Program selesai")
        break

    else:
        print("Menu tidak tersedia")