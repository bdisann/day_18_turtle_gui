class Hallo:


    def __init__(self, name, address):
        self.name = name
        self.address = address


    def berjalan_maju(self):
        return "Sedang berjalan manju"


person_1 = Hallo('budi', 'jakarta')


print(f"Halo, {person_1.name} dari {person_1.address}\n{person_1.name} {person_1.berjalan_maju()}")