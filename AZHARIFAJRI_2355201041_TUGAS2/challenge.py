# Fungsi untuk menghitung jalur Meong Bross berdasarkan perintah
def trace_meong():
    # Inisialisasi koordinat awal
    x, y = 0, 0
    # Simpan jejak koordinat
    path = [(x, y)]

    # Meminta jumlah perintah
    n = int(input("Banyak perintah: "))

    # Loop untuk meminta setiap perintah
    for _ in range(n):
        command = input("Masukkan perintah: ").upper()

        # Sesuaikan pergerakan berdasarkan perintah
        if command == 'U':  # Up
            y += 1
        elif command == 'T':  # Right (Timur)
            x += 1
        elif command == 'B':  # Down (Bawah)
            y -= 1
        elif command == 'S':  # Left (Selatan)
            x -= 1
        else:
            print(f"Perintah {command} tidak dikenali, lewati.")

        # Tambahkan koordinat baru ke dalam jejak
        path.append((x, y))

    # Format dan cetak hasil jalur yang ditempuh
    result = "Jalur yang ditempuh meong bross adalah " + '-'.join([f"({x},{y})" for x, y in path])
    print(result)

# Memanggil fungsi
trace_meong()