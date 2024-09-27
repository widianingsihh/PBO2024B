


def hitung_koordinat(banyak_perintah):
   
    x, y = 0, 0

    
    for _ in range(banyak_perintah):
        perintah = input("Masukkan perintah : ")
        
       
        if perintah == "U":
            y += 1  
        elif perintah == "S":
            y -= 1  
        elif perintah == "T":
            x += 1  
        elif perintah == "B":
            x -= 1  
        elif perintah == "HOME":
            x, y = 0, 0  
        else:
            continue  

    
    return x, y


def main():
    
    banyak_perintah = int(input("Banyak perintah : "))

   
    if banyak_perintah == 0:
        print("Karakter Meong Brosss berada di koordinat (0,0)")
    else:
        
        x_akhir, y_akhir = hitung_koordinat(banyak_perintah)
        
        
        print(f"Karakter Meong Brosss berada di koordinat ({x_akhir},{y_akhir})")


if __name__ == "__main__":
    main()
