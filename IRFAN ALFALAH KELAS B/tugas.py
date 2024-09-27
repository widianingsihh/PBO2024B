class Person:
    def __init__(self, nama, jenis_kelamin, ipk):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.ipk = ipk

    def myfunc(self):
        print("Mahasiswa PBO kelas B " + self.nama + " mempunyai jenis_kelamin " + self.jenis_kelamin)
        print("dengan IPK " + str(self.ipk))
    
p1 = Person("irfan alfalah", "pria", 9.0)
p1.myfunc()
