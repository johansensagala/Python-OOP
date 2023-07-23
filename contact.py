class Person:

    data_person = {}

    def __init__(self, nama=None, no_telp=None, email=None, jk=None):
        self.nama = nama
        self.__no_telp = no_telp
        self.__email = email
        self.__jk = jk
        self.data_person[self.nama] = {
            "Nomor Telepon": self.no_telp,
            "E-mail": self.email,
            "Jenis Kelamin": self.jk
        }

    @classmethod
    def lihat_person(cls):
        return cls.data_person

    @property
    def no_telp(self):
        return self.__no_telp
    
    @property
    def email(self):
        return self.__email
    
    @property
    def jk(self):
        return self.__jk
    
    @no_telp.setter
    def no_telp(self, no_telp):
        self.__no_telp = no_telp
        self.data_person[self.nama]["Nomor Telepon"] = no_telp

    @email.setter
    def email(self, email):
        self.__email = email
        self.data_person[self.nama]["E-mail"] = email

    @jk.setter
    def jk(self, jk):
        self.__jk = jk
        self.data_person[self.nama]["Jenis Kelamin"] = jk

class Contact(Person):

    data_contact = {}

    def tambah_kontak(self, nama):
        self.nama = nama
        self.data_contact[nama] = super().data_person[nama]["Nomor Telepon"]
        
    @classmethod
    def lihat_contact(cls):
        return cls.data_contact
    
class Group(Person):

    grup = {}

    # method untuk menambah grup (maksimal ada 5 anggota untuk satu grup dan minimal 2)
    def tambah_grup(self, nama_grup, *args):

        self.grup[nama_grup] = {}

        if len(args) > 5:
            print("Jumlah anggota maksimum adalah 5!")

        elif len(args) < 2:
            print("Jumlah anggota minimum adalah 2!")
            
        else:  
            for arg in args:
                self.grup[nama_grup][arg] = super().data_person[arg]["Nomor Telepon"]

    @classmethod
    def tampilkan_grup(cls):
        return cls.grup


# menambahkan person ke kelas Person (anggap buku telepon)
jonatan = Person("Jonatan Situmorang", "+6282267926760", "jonatan@gmail.com", "L")
irpan = Person("Irpan Buri Siburian", "+6282370714442", "irpan@gmail.com", "L")
josua = Person("Eli Feri Josua", "+6281276005818", "josua@gmail.com", "L")
iman = Person("Iman Saputra", "+6281262329634", "iman@gmail.com", "L")

# menambah person yang kita mau untuk dimasukkan ke kontak
Contact().tambah_kontak("Jonatan Situmorang")
Contact().tambah_kontak("Irpan Buri Siburian")
Contact().tambah_kontak("Eli Feri Josua")
Contact().tambah_kontak("Iman Saputra")

print(Person.lihat_person())
print("\n")
print(Contact.lihat_contact())
print("\n")
print(jonatan.no_telp)
print("\n")
print(Person.lihat_person())
print("\n")
Group().tambah_grup("Grup Kelas", "Jonatan Situmorang", "Irpan Buri Siburian", "Iman Saputra")
Group().tambah_grup("Geng Cupu", "Jonatan Situmorang", "Irpan Buri Siburian", "Eli Feri Josua")
print("\n")
print(Group.tampilkan_grup())