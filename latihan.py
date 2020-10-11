print("\t>>>* ANGKA GANJIL *<<<")
print("\t\t--------")

angka = int(input("Inputkan angka anda = "))

if angka % 2 <=1:
    print("Angka", angka, "adalah angka ganjil")

print("\n") 
print("\t>>>* ANGKA GENAP *<<<")
print("\t\t--------")

angka = int(input("Inputkan angka anda = "))

if angka % 2 <=0:
    print("Angka", angka, "adalah angka genap")
else:
    print("Anda memasukkan angka ganjil")