'''
polymorphism => many forms

many forms នៅក្នុង programming មានន័យថា method និង function ទាំងឡាយដែលមានឈ្មោះដូចគ្នាវាអាចធ្វើការ excute ជាមួយ object ជាច្រើនផ្សេងៗគ្នា។
'''

class Instrument:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def play(self):
        print("play the instrument.")

class Guitar(Instrument):
    def play(self):
        print("strum the guitar.")

class Piano(Instrument):
    def play(self):
        print("play the piano keys.")

class Drum(Instrument):
    def play(self):
        print("Hit the drum.")

guitar = Guitar(brand="Fender", model="AcousticX1")
piano = Piano(brand="Yamaha", model="YX1")
drum = Drum(brand="Yamaha", model="YX1")

Instrument = guitar
Instrument.play()
print(Instrument.brand)
print(Instrument.model)

Instrument = piano
Instrument.play()
print(Instrument.brand)
print(Instrument.model)

Instrument = drum
Instrument.play()
print(Instrument.brand)
print(Instrument.model)