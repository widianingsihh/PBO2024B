def meong_bross():
    # Posisi awal Meongbross
    x, y = 0, 0
    
    # Input jumlah perintah
    try :
        jumlah_perintah = int(input(" jumlah perintah: "))
        
        # Identifikasi input jumlah perintah
        if jumlah_perintah < 0:
            print("Jumlah perintah adalah bilangan non negatif.")
            
    except ValueError:
        print("bilangan tidak valid. Coba masukkan bilangan bulat!")
        

    # Proses setiap perintah
    for _ in range(jumlah_perintah):
        w = input("jumlah perintah: ").strip()
        
        if w == 'U':
            y += 1  # Bergerak ke Utara
        elif w == 'S':
            y -= 1  # Bergerak ke Selatan
        elif w == 'T':
            x += 1  # Bergerak ke Timur
        elif w == 'B':
            x -= 1  # Bergerak ke Barat
        elif w == 'HOME':
            break  # Menghentikan eksekusi
        else:
            print("Berhasil, Meong Bross bergerak.")
    
    # Output posisi akhir Meong Bross dengan format yang diminta
    print(f"Karakter Meong Brosss berada di koordinat ({x},{y})")

# Menjalankan program
meong_bross()