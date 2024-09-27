def meong_bross():
    # Inisialisasi posisi awal Meong Bross
    x, y = 0, 0

    # Minta jumlah perintah dari pengguna
    while True:
        try:
            jumlah_perintah = int(input("Masukkan jumlah perintah: "))
            if jumlah_perintah < 0:
                raise ValueError("Jumlah perintah harus bilangan non negatif.")
            break  # Keluar dari loop jika input valid
        except ValueError as e:
            print(f"Input tidak valid: {e}. Silakan coba lagi.")

    # Proses setiap perintah yang diberikan
    for _ in range(jumlah_perintah):
        perintah = input("Masukkan perintah: ")

        # Memperbarui posisi berdasarkan perintah
        if perintah == "U":
            y += 1
        elif perintah == "S":
            y -= 1
        elif perintah == "T":
            x += 1
        elif perintah == "B":
            x -= 1
        elif perintah == "HOME":
            x, y = 0, 0  # Reset ke posisi awal
        else:
            print(f"Perintah '{perintah}' tidak dikenali. Meong Bross tetap di posisi ({x}, {y}).")

    # Menampilkan hasil akhir
    print(f"Karakter Meong Brosss berada di koordinat ({x}, {y})")

# Jalankan program
if __name__ == "__main__":
    meong_bross()
