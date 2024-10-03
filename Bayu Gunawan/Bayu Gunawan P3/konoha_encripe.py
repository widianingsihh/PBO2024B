#               CF2                 #

print ("The Eligma Code")

# input1 = input("Masukkan Input :")
def geser_karakter(karakter, jumlah_geser):
    # Menggeser karakter berdasarkan jumlah geseran dengan memutar kembali ke 'a' jika melebihi 'z'
    if 'a' <= karakter <= 'z':
        return chr((ord(karakter) - ord('a') + jumlah_geser) % 26 + ord('a'))
    elif 'A' <= karakter <= 'Z':
        return chr((ord(karakter) - ord('A') + jumlah_geser) % 26 + ord('A'))
    else:
        return karakter

def proses_string(input_string):
    angka_total = 0
    huruf_saja = []

    # Memisahkan huruf dan angka, serta menjumlahkan angka
    for karakter in input_string:
        if karakter.isdigit():
            angka_total += int(karakter)
        elif karakter.isalpha():
            huruf_saja.append(karakter)
    
    # Geser huruf sesuai jumlah penjumlahan angka
    hasil_geser = [geser_karakter(huruf, angka_total) for huruf in huruf_saja]
    
    # Gabungkan hasil
    return ''.join(hasil_geser)

# Contoh penggunaan
input_string = "CF2 W4HY8M89A"
output_string = proses_string(input_string)
print(output_string)
