# Impor modul math untuk menggunakan konstanta pi
import math

# Fungsi untuk menghitung luas permukaan bola
def luas_permukaan_bola(r):
    # Rumus luas permukaan bola = 4 * pi * r**2
    return 4 * math.pi * r**2

# Fungsi untuk menghitung volume bola
def volume_bola(r):
    # Rumus volume bola = 4/3 * pi * r**3
    return 4/3 * math.pi * r**3

# Contoh penggunaan fungsi
# Masukkan jari-jari bola
r = float(input("Masukkan jari-jari bola: "))
# Panggil fungsi luas_permukaan_bola dan volume_bola
# Cetak hasilnya dengan pembulatan dua angka di belakang koma
print(f"Luas permukaan bola = {round(luas_permukaan_bola(r), 2)}")
print(f"Volume bola = {round(volume_bola(r), 2)}")
