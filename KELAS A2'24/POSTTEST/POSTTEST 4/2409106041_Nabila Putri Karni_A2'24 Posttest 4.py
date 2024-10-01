username_saya = ("nabilapk")
password_saya = ("41")

kesempatan_login = 3
while kesempatan_login > 0:
    username = input("Masukkan username: ")
    password = input("Masukkan 2 digit terakhir NIM: ")

    if username == username_saya and password == password_saya:
        print("\nbisa login bro!!!\n")
        break
    else:
        kesempatan_login -= 1
        if kesempatan_login == 0:
            print("Kesempatan habis kocak. programnya diberentiin nih!!!")
            exit()
        print(f"kaga bisa login. kesempatan login: {kesempatan_login}")    


while True:
    jumlah_pinjaman = float(input("masukkan jumlah pinjaman: "))

    lama_cicilan = int(input("masukkan lama cicilan (1/2/3 tahun): "))

    if lama_cicilan == 1:
        bunga_tahunan =0.07
        jumlah_bulan =12
    elif lama_cicilan == 2:
        bunga_tahunan =0.13
        jumlah_bulan =24
    elif lama_cicilan == 3:
        bunga_tahunan =0.19
        jumlah_bulan =36
    else:
        print("tidak valid!!!!!")
        continue

    bunga_per_bulan = (bunga_tahunan / 12)* jumlah_pinjaman

    cicilan_per_bulan = (jumlah_pinjaman + bunga_per_bulan)/ jumlah_bulan

    print(f"Jumlah pinjaman: Rp {jumlah_pinjaman:,.0f}")
    print(f"Bunga per Bulan: Rp {bunga_per_bulan:,.0f}")
    print(f"Cicilan per Bulan: Rp {cicilan_per_bulan:,.0f}")

    pilihan = input("Apakah Anda ingin menghitung lagi? (yay/nay): ").lower()
    if pilihan == 'nay':
        print("Program diberhentikan. Makasehhh")
        break