import datetime

def main():
    # Untuk mengetahui tahun saat ini
    tahun_saat_ini = datetime.datetime.now().year

    # Untuk mengetahui jumlah hari dalam tahun ini
    jumlah_hari_tahun_ini = 366 if (tahun_saat_ini % 4 == 0 and tahun_saat_ini % 100 != 0) or (tahun_saat_ini % 400 == 0) else 365

    # Memasukkan sebuah bilangan bulat
    bilangan_bulat = int(input("Masukkan sebuah bilangan bulat: "))

    # Menghitung hasil pembagian bilangan bulat dengan jumlah hari pada tahun ini
    hasil = bilangan_bulat / jumlah_hari_tahun_ini

    # Menampilkan hasil dengan sebelas angka desimal jika ada (dibulatkan ke atas)
    format_hasil = "{:.11f}".format(hasil)

    print("Hasil:", format_hasil)

if __name__ == "__main__":
    main()
