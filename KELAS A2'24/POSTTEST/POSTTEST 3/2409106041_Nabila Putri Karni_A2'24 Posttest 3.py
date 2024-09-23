import os


if os.name == 'nt':
    os.system('cls')





nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
jumlah_pinjaman = float(input("Masukkan jumlah pinjaman (Rp): "))
lama_cicilan = int(input("Masukkan lama cicilan (1/2/3 tahun): "))

if lama_cicilan == 1:
    bunga_tahunan = 0.07
    jumlah_bulan = 12
elif lama_cicilan == 2:
    bunga_tahunan = 0.13
    jumlah_bulan = 24
elif lama_cicilan == 3:
    bunga_tahunan = 0.19
    jumlah_bulan = 36
else:
    print("tidak validdd!!!!!") 
    exit()
    
Bunga_per_bulan = (bunga_tahunan  / 12 )* jumlah_pinjaman
cicilan_per_bulan = (jumlah_pinjaman + Bunga_per_bulan )/ jumlah_bulan

print(f"nama: {nama}")
print(f"NIM: {nim}")
print(f"jumlah bulan: {jumlah_bulan}")
print(f"jumlah pinjaman: Rp {jumlah_pinjaman:,.0f}")
print(f"bunga per bulan: Rp {Bunga_per_bulan:,.0f}")
print(f"cicilan per bulan: Rp {cicilan_per_bulan:,.0f}")   


