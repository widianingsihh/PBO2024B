# ~             CF2                         ~ 
# 1. Class And Object in The_init_("Function")

class PBOB:
    def __init__(deklarasi, nama, jenis_kelamin):
        deklarasi.nama = nama
        deklarasi.jenis_kelamin = jenis_kelamin

BG = PBOB("Ardiansyah Mulia", "Laki-Laki")

print (CF.nama)
print (CF.jenis_kelamin)

print("*OR*")

print ("Nama " + CF.nama)
print ("Jenis Kelamin " + CF.jenis_kelamin)

# 2.Alternate
class mahasiswa :
    def __init__(deklarasi, nama, jenis_kelamin, mahasiswa):
        deklarasi.nama = nama
        deklarasi.jenis_kelamin = jenis_kelamin
        deklarasi.mahasiswa = mahasiswa

    def info(deklarasi):
        return f"Nama saya adalah {deklarasi.nama} dan Jenis Kelamin saya {deklarasi.jenis_kelamin} status Mahasiswa {deklarasi.mahasiswa}"

mahasiswa1 = mahasiswa("Ardiansyah Mulia", "Laki-Laki", "PBO Kelas B")
mahasiswa2 = mahasiswa("Putri Salsabila", "Perempuan", "PBO Kelas A")

print (mahasiswa1.info())
print (mahasiswa2.info())