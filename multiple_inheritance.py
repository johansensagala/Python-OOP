class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bergerak(self):
        print(f"{self.nama} bergerak.")

class HewanAir:
    def __init__(self, nama):
        self.nama = nama

    def bergerak(self):
        print(f"{self.nama} bergerak di air.")

class Ikan(Hewan, HewanAir):
    def __init__(self, nama):
        super().__init__(nama)

    def bergerak(self):
        super().bergerak()
        print(f"{self.nama} berenang.")

ikan = Ikan("Paus")
ikan.bergerak()
