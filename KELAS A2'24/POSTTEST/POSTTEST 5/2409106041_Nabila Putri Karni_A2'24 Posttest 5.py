users = [["bilaw", "bilaw123", "bilaw"]]  

datahewan = []

logged_in = False
current_user = None

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

        users.append([newusername, newpassword, "pengguna baru"])
        print("Registrasi berhasil untuk pengguna baru!")

    elif pilihan_utama == 2: 
        while not logged_in:
            print("Login")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")

            found = False
            for user in users:
                if user[0] == username and user[1] == password:
                    current_user = user
                    logged_in = True
                    found = True
                    print(f"Berhasil masuk sebagai {username}!")
                    break
            
            if not found:
                print("Username atau password salah. Coba lagi.")

        while True:
            if current_user[2] == "bilaw":  
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
                    petid = input("Masukkan ID hewan: ")
                    petname = input("Masukkan nama hewan: ")
                    pettype = input("Masukkan jenis hewan: ")
                    try:
                        petname = int(input("Masukkan umur hewan (tahun): "))
                    except ValueError:
                        print("Umur harus berupa angka.")
                        continue
                    datahewan.append([petid, petname, pettype, petname])
                    print("Data hewan berhasil ditambahkan.")

                elif pilihan == 2:  
                    if len(datahewan) == 0:
                        print("Data hewan tidak ada.")
                    else:
                        print("\nData Hewan:")
                        for i, pet in enumerate(datahewan, 1):
                            print(f"{i}. ID: {pet[0]}, Nama: {pet[1]}, Jenis: {pet[2]}, Umur: {pet[3]} tahun")

                elif pilihan == 3:  # Ubah Hewan
                    if len(datahewan) == 0:
                        print("Tidak ada data hewan untuk diubah.")
                    else:
                        try:
                            indeks = int(input("Masukkan nomor hewan yang ingin diubah: ")) - 1
                            if 0 <= indeks < len(datahewan):
                                petname = input("Masukkan nama  baru: ")
                                pettype = input("Masukkan jenis baru: ")
                                try:
                                    petname = int(input("Masukkan umur baru: "))
                                except ValueError:
                                    print("Umur harus berupa angka.")
                                    continue
                                datahewan[indeks] = [datahewan[indeks][0], petname, pettype, petname]
                                print("Data hewan berhasil diupdate.")
                            else:
                                print("Nomor hewan tidak valid.")
                        except ValueError:
                            print("Input harus berupa angka.")

                elif pilihan == 4:  
                    if len(datahewan) == 0:
                        print("Tidak ada data hewan untuk dihapus.")
                    else:
                        try:
                            indeks = int(input("Masukkan nomor hewan yang ingin dihapus: ")) - 1
                            if 0 <= indeks < len(datahewan):
                                datahewan.pop(indeks)
                                print("Data hewan berhasil dihapus.")
                            else:
                                print("Nomor hewan tidak valid.")
                        except ValueError:
                            print("Input harus berupa angka.")

                elif pilihan == 5:  
                    logged_in = False
                    current_user = None
                    break  
            elif current_user[2] == "user":  
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
                    pilihan = int(input("Pilih menu: "))
                except ValueError:
                    print("Input harus berupa angka.")
                    continue

                if pilihan == 1:  
                    if len(datahewan) == 0:
                        print("Data hewan kosong.")
                    else:
                        print("\nData Hewan:")
                        for i, pet in enumerate(datahewan, 1):
                            print(f"{i}. ID: {pet[0]}, Nama: {pet[1]}, Jenis: {pet[2]}, Usia: {pet[3]} tahun")

                elif pilihan == 2:  
                    logged_in = False
                    current_user = None
                    break 

    elif pilihan_utama == 3:  
        print("Terima kasih telah menggunakan program petshop ini.")
        break

    else:
        print("Pilihan tidak valid.")
