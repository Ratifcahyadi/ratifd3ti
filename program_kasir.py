menu = "y" or "Y"
while menu == "y" or "Y":
    print(" ========================================")
    print(" Selamat Datang di Pussy Library Store")
    print(" Daftar Judul Buku:")
    print(" ========================================")
    print(" 1. Sains dan Teknologi Pangan : Rp 23.000")
    print(" 2. Elektonika dan Instrumental : Rp 27.000")
    print(" 3. Manajemen dan Ekonomi Industri : Rp 30.000")
    print(" 4. Multi Literature Languange's : Rp 26.000")
    print(" 5. Games dan Manifest Public : Rp. 27.000")
    print(" ========================================")
    listJudul=str(input(" Masukkan angka sesuai dengan judul buku yang tersedia = "))
    jumlahPesanan=int(input(" Jumlah dibeli = "))
    if listJudul == "1":
        namaJudul= " Sains dan Teknologi Pangan"
        harga=(23000*jumlahPesanan)
        pajak= int(harga * 0.1)
        if jumlahPesanan >= 5:
            totalHarga=int(harga+pajak)
        else:
            totalHarga=int(harga+pajak)
    elif listJudul == "2":
        namaJudul= " Elektonika dan Instrumental"
        harga = (27000*jumlahPesanan)
        pajak = int(harga * 0.1)
        if jumlahPesanan >= 5:
            totalHarga =int(harga+pajak)
        else:
            totalHarga =int(harga+pajak)
    elif listJudul == "3":
        namaJudul= " Manajemen dan Ekonomi Industri"
        harga=int(30000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga=int(harga+pajak)
    elif listJudul == "4":
        namaJudul= " Multi Literature Languange's + Pena"
        harga=int(26000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga = int(harga+pajak)
    elif listJudul == "5":
        namaJudul= " Games dan Manifest Public + Pena"
        harga=int(27000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga = int(harga+pajak)
    else:
        menu=input(" Maaf, Judul  yang dipilih tidak tersedia di Pussy Store")
        break

    print(" ------------------------------")
    print(" Judul :",namaJudul)
    print(" Jumlah Pesanan :", jumlahPesanan)
    print(" Harga :", harga)
    print(" Pajak :", pajak)
    print(" ------------------------------")
    print(" Total Pembayaran :", totalHarga)
    print(" ------------------------------")

    menu=input(" Mau pesan lagi? pilih Y jika Ya, pilih N jika Tidak (Y/N) = ")