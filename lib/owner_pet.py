class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        self.name = name 
        self.pet_type = pet_type
        self.owner = owner 
        Pet.all.append(self)
    
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, type):
        if type in Pet.PET_TYPES:
            self._pet_type = type
        else:
            raise Exception("Pet type must be specified in PET_TYPES")
        
    def __repr__(self):
        return self.name
            

class Owner:
    
    def __init__(self, name):
        self.name = name 

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else: 
            raise Exception("pet is not of type Pet.")
    
    def get_sorted_pets(self):
        sortedPets = Pet.all
        # Sorts by the first char in each pet name
        sortedPets.sort(key=lambda x: x.name)
        return sortedPets


if __name__ == "__main__":
    owner = Owner("John")
    pet1 = Pet("Fido", "dog", owner)
    pet2 = Pet("Clifford", "dog", owner)
    pet3 = Pet("Whiskers", "cat", owner)
    pet4 = Pet("Jerry", "reptile", owner)
    print(Pet.all)
    print(owner.get_sorted_pets())