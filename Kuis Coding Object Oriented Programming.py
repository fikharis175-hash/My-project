"""
TODO:
1. Buatlah class bernama Animal dengan ketentuan:
    - Memiliki properti:
      - name: string
      - age: int
      - species: string
    - Memiliki constructor untuk menginisialisasi properti:
      - name
      - age
      - species
2. Buatlah class bernama Cat dengan ketentuan:
    - Merupakan turunan dari class Animal
    - Memiliki method:
      - bernama "deskripsi" yang mengembalikan nilai string berikut ini.
        "{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
      - bernama "suara" yang akan mengembalikan nilai string "meow!"
 3. Buatlah instance dari kelas Cat bernama "myCat" dengan ketentuan:
    - Atribut name bernilai: "Neko"
    - Atribut age bernilai: 3
    - Atribut species bernilai: "Persian".
"""

#TODO: Silakan buat kode Anda di bawah ini.


class Animal:
    def __init__(self, name, age, species):
        self.name = name 
        self.age = age
        self.species = species 
       
class Cat(Animal):
    def myCat(self):
        self.name = "Neko"
        self.age = 3
        self.species = "Persian"
    
    def deskripsi(self):
        print (f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun")
        return (f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun")
    
    def suara(self):
        print('meow!')
        return "meow!"

myCat = Cat('Neko', 3, 'Persian')
print(myCat.name)
myCat.deskripsi()