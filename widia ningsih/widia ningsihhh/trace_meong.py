def meong_bross():
    
    x, y = 0, 0
    jalur = [(x, y)]
    
    
    try :
        jumlah_perintah = int(input("Jumlah perintah: "))
        
        
        if jumlah_perintah < 0:
            print("Jumlah perintah tidak boleh negatif.")
            
    except ValueError:
        print("Bilangan tidak valid. Harap masukkan bilangan bulat.")
        

    
    for _ in range(jumlah_perintah):
        perintah = input("Masukkan perintah: ").strip()
        
        if perintah == 'U':
            y += 1  # Bergerak ke Utara
        elif perintah == 'S':
            y -= 1  # Bergerak ke Selatan
        elif perintah == 'T':
            x += 1  # Bergerak ke Timur
        elif perintah == 'B':
            x -= 1  # Bergerak ke Barat
        elif perintah == 'HOME':
            break  # Menghentikan eksekusi
        else:
            print("Tidak valid, Meong Bross tetap di tempat.")
            
        
        jalur.append((x, y))
    
    
    jalur_output = "-".join(f"({x},{y})" for x, y in jalur)
    print(f"Jalur yang dilalui meong bross  {jalur_output}")


meong_bross()