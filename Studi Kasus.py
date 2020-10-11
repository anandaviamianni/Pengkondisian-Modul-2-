# Kiki dan Titis adalah seorang programmer di PT Daspro, kemudian mereka diminta oleh atasannya 
# untuk membuat sebuah program untuk menentukkan kategori umur, dengan ketentuan umur seperti di bawah.

print("==== KATEGORI UMUR ====")

umur = int(input("Masukkan umur anda = "))
print("\nAnda Berada pada : ")
print("===============================")

if umur > 0 and umur <= 5:
    print("Masa Balita")
elif umur > 5 and umur <= 12:
    print("Masa Kanak-kanak")
elif umur > 12 and umur <= 25:
    print("Masa Remaja")
elif umur > 25 and umur <= 45:
    print("Masa Remaja")
elif umur > 45 and umur <= 65:
    print("Masa Lansia")
else:
    print("Masa Manula")

print("==============================")