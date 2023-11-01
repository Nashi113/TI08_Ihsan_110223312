print ("Tugas 1")
m = ["B 3122 PZ", "Supra", "125cc", "Hitam"]
print(m)

print("Tugas 2")
m.append("Rp.5.000.000")
m.append("Kendaraan Roda 2")
m.insert(1,"Honda")
m.insert(3, "Motor")
print(m)

print("Tugas 3")
ket = '''Silahkan Masukkan Nomor
         1. Untuk Menghitung Luas Persegi
         2. Untuk Menghitung Luas Lingkaran
         3. Untuk Menghitung Luas Segitiga....'''

pilihan = input (ket) 

match pilihan:
    case "1":
        print ("Anda Memilih 1 untuk menghitung Luas Persegi")
        sisi = int(input("Masukkan sisi ="))
        luasP = sisi * sisi
        print ("Luas Persegi yang sisinya", sisi, "adalah", luasP)
    case "2":
        print ("Anda Memilih 2 untuk menghitung Luas Lingkaran")
        jari2 = float(input("Masukkan Jari2 ="))
        luasL = 3.14 * jari2 * jari2
        print = ("Luas Lingkaran yang Jari2nya", jari2, "adalah",int(luasL))
    case "3":
        print ("Anda Memilih 3 untuk menghitung Luas Segitiga")
        a = int(input("Masukkan alas ="))
        t = int(input("Masukkan tinggi ="))
        luasS = 0.5 * a * t
        print ("Luas Segitiga yang alas", a,"tinggi", t, "adalah", luasS)
    case _:
        print("Nomor yang anda masukkan salah")

