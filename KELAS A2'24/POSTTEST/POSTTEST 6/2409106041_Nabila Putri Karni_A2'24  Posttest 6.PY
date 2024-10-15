
users = {
    "bilaw": {"password": "bilaw123", "role": "admin"}
}

datahewan = {}

logged_in = False
pengguna = None

while True:
    print(
    """
    ===========================
    |   MANAJEMEN PET SHOP    |
    ===========================
    |    1. REGISTRASI        |
    |    2. LOGIN             |
    |    3. KELUAR            |
    ===========================
    """
    )
    try:
        pilihan_utama = int(input("Pilih (1/2/3): "))
    except ValueError:
        print("Input harus berupa angka.")
        continue

    if pilihan_utama == 1: 
        newusername = input("Masukkan username baru: ")
        newpassword = input("Masukkan password baru: ")
        if newusername in users:
            print("Username sudah ada. Coba lagi.")
        else:
            users[newusername] = {"password": newpassword, "role": "pengguna"}
            print("Registrasi berhasil untuk pengguna baru!")

    elif pilihan_utama == 2:  
        while not logged_in:
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            if username in users and users[username]["password"] == password:
                pengguna = users[username]
                logged_in = True
                print(f"Berhasil masuk sebagai {username}!")
            else:
                print("Username atau password salah. Coba lagi.")

        while logged_in:
            if pengguna["role"] == "admin":  
                print(
                """
                ===========================
                |    MENU ADMIN PET SHOP   |
                ===========================
                |    1. TAMBAH HEWAN       |
                |    2. TAMPILKAN HEWAN    |
                |    3. UBAH HEWAN         |
                |    4. HAPUS HEWAN        |
                |    5. LOGOUT             |
                ===========================
                """
                )
                try:
                    pilihan = int(input("Pilih (1/2/3/4/5): "))
                except ValueError:
                    print("Input harus berupa angka.")
                    continue

                if pilihan == 1: 
                    id_hewan = input("Masukkan ID hewan: ")
                    nama_hewan = input("Masukkan nama hewan: ")
                    jenis_hewan = input("Masukkan jenis hewan: ")
                    try:
                        petage = int(input("Masukkan umur hewan (tahun): "))
                    except ValueError:
                        print("Umur harus berupa angka.")
                        continue
                    datahewan[id_hewan] = {"nama": nama_hewan, "jenis": jenis_hewan, "umur": petage}
                    print("Data hewan berhasil ditambahkan.")

                elif pilihan == 2:  
                    if not datahewan:
                        print("Data hewan tidak ada.")
                    else:
                        print("\nData Hewan:")
                        for id_hewan, details in datahewan.items():
                            print(f"ID: {id_hewan}, Nama: {details['nama']}, Jenis: {details['jenis']}, Umur: {details['umur']} tahun")

                elif pilihan == 3: 
                    id_hewan = input("Masukkan ID hewan yang ingin diubah: ")
                    if id_hewan in datahewan:
                        nama_hewan = input("Masukkan nama baru: ")
                        jenis_hewan = input("Masukkan jenis baru: ")
                        try:
                            petage = int(input("Masukkan umur baru: "))
                        except ValueError:
                            print("Umur harus berupa angka.")
                            continue
                    
                        datahewan[id_hewan].update({"nama": nama_hewan, "jenis": jenis_hewan, "umur": petage})
                        print("Data hewan berhasil diupdate.")
                    else:
                        print("Hewan dengan ID tersebut tidak ditemukan.")

                elif pilihan == 4:  
                    id_hewan = input("Masukkan ID hewan yang ingin dihapus: ")
                    if id_hewan in datahewan:
                        del datahewan[id_hewan]
                        print(f"Data hewan dengan ID {id_hewan} berhasil dihapus.")
                    else:
                        print("Hewan dengan ID tersebut tidak ditemukan.")

                elif pilihan == 5:  
                    logged_in = False
                    pengguna = None
                    break

            elif pengguna["role"] == "pengguna": 
                print(
                """
                ===========================
                |    MENU USER PET SHOP    |
                ===========================
                |    1. TAMPILKAN HEWAN    |
                |    2. LOGOUT             |
                ===========================
                """
                )
                try:
                    pilihan = int(input("Pilih (1/2): "))
                except ValueError:
                    print("Input harus berupa angka.")
                    continue

                if pilihan == 1: 
                    if not datahewan:
                        print("Data hewan tidak ada.")
                    else:
                        print("\nData Hewan:")
                        for id_hewan, details in datahewan.items():
                            print(f"ID: {id_hewan}, Nama: {details['nama']}, Jenis: {details['jenis']}, Umur: {details['umur']} tahun")

                elif pilihan == 2:  
                    logged_in = False
                    pengguna = None
                    break

    elif pilihan_utama == 3: 
        print("Terima kasih telah menggunakan program petshop ini.")
        break

    else:
        print("Pilihan tidak valid.")
