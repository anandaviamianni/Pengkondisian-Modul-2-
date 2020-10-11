# Adi adalah pemilik dari T-mart, Adi menginginkan supermarket miliknya memberikan discount 5% kepada 
# pembeli nya dengan minimum pembelian sebesar Rp. 50.000 dan menentukan kembalian pembeli secara otomatis. 
# Tapi apabila pembeli tidak mencapai minimum pembelian. Maka, pembeli tidak berhak mendapatkan discount 5%. 
# Bantu adi membuat program tersebut 

print("=====* T-Mart *=====")
total_belanja = int(input("Total belanja anda = Rp. "))

if total_belanja >= 50000:
    discount = int(total_belanja * (5/100))
    hasil = total_belanja - discount
    print("\nAnda mendapatkan potongan harga sebesar 5%")
    print("Total yang harus anda bayar\t = Rp.",hasil)
    bayar = int(input("Masukkan Uang anda = Rp. "))
    if bayar >= hasil:
        kembalian = bayar - hasil
        print("Kembalian anda \t\t\t= Rp.", kembalian)
        print("\n\tTerimakasih sudah berbelanja")
    else:
        print("\t==== Uang anda kurang ===")
        print("\t\tTerima Kasih")
else:
    print("\nTotal yang harus dibayar\t= Rp.", total_belanja)
    bayar = int(input("Masukkan Uang anda \t\t= Rp. "))
if bayar >= total_belanja:
    kembalian = bayar - total_belanja
    print("Kembalian anda \t\t\t= Rp.", kembalian)
    print("\n\tTerimakasih sudah berbelanja")
else:
    print("\t==== Uang anda kurang ====")
    print("\t\tTerimakasih")