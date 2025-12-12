class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("whoof whoof")

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number

owner1 = Owner("benny", "alfonso", "9863726371")
dog1 = Dog("bruce", "xyz", owner1)
print(dog1.owner.name)

owner2 = Owner("belly", "talker", "8828196371")
dog2 = Dog("freya", "abc", owner2)
print(dog2.owner.name)
