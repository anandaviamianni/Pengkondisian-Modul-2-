print("\t>>>>* Cek Kelulusan Mata Kuliah Kalkulus *<<<<")
nilai = int(input("Masukkan nilai akhir : "))
if nilai > 40:
    kehadiran = int(input("Masukkan presentase kehadiran: "))
    if kehadiran >= 75:
        print("Selamat anda lulus")
        if nilai <= 50 and nilai >= 41:
            print("Dengan index E")
        elif nilai <= 60 and nilai >= 51:
            print("Dengan index D")
        elif nilai <= 70 and nilai >= 61:
            print("Dengan index C")
        elif nilai <= 80 and nilai >= 71:
            print("Dengan index B")
        elif nilai <= 100 and nilai >= 81:
            print("Dengan index A")
    else:
        print("Maaf anda harus mengulang")
else:
    print("Maaf anda harus mengulang")