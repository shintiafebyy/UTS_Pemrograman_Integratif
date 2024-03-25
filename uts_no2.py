def main():
    angka = int(input("Masukkan sebuah angka (tanggal tes hari ini): "))

    hasil_perkalian = 1

    # Menghitung hasil perkalian dari 1 hingga angka yang dimasukkan
    for i in range(1, angka + 1):
        hasil_perkalian *= i

    # Mencetak hasil perkalian dari 1 hingga angka yang dimasukkan
    print("Hasil perkalian dari 1 hingga", angka, "adalah:", hasil_perkalian)

if __name__ == "__main__":
    main()
