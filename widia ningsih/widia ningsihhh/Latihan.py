class Person:
    def _init_(self, name, gender, ipk):
        self.name = name
        self.gender = gender
        self.ipk = ipk

    def myfunc(self):
        print("Mahasiswa PBO kelas B adalah " + self.name + " jenis kelamin " + self.gender)
        print("dengan IPK " + str(self.ipk))
    
p1 = Person("Widia Ningsih", "cewe", 3.9)
p1.myfunc()