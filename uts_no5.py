# Membaca angka-angka dari file teks bernama input.txt
with open("input.txt", "r") as file:
    numbers = [int(line.strip()) for line in file if line.strip().isdigit()]

# Menghitung jumlah dari angka-angka yang ada di dalam file input.txt
total = sum(numbers)

# Mencetak hasil dengan pemisah koma dan tiga digit di belakang koma
print("{:,.3f}".format(total))
