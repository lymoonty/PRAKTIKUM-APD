nama = input("masukkan nama lengkap:")
nim = input("Masukkan NIM:")
harga = input("Masukkan harga beras (Rp):")

harga = float(harga)

diskon_mawar = 11 / 100
diskon_sania = 14 / 100
diskon_maknyus = 17 / 100

diskon_mawar_hitung = harga * diskon_mawar
diskon_sania_hitung = harga * diskon_sania
diskon_maknyus_hitung = harga * diskon_maknyus

harga_setelah_diskon_mawar = harga  - diskon_mawar_hitung
harga_setelah_diskon_sania = harga - diskon_sania_hitung
harga_setelah_diskon_maknyus = harga - diskon_maknyus_hitung

print("harga setelah diskon beras mawar adalah", harga_setelah_diskon_mawar)
print("harga setelah diskon beras sania adalah", harga_setelah_diskon_sania)
print("harga setelah diskon beras maknyus adalah", harga_setelah_diskon_maknyus)
