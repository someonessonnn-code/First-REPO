class person(object):
    population = 50
    def __init__(self,name,age,location,school):
        self.name= name
        self.age = age
        self.location = location
        self.school = school

    
    @classmethod
    def getPopulation(cls):
        return cls.population
    
    @staticmethod
    def isAdult(age):
        return age >= 18
    
    def display(self):
        print(self.name, 'is' ,self.age, 'years old' , 'he lives in ' , self.location , 'and goes to' , self.school)


newPerson = person('Nsemwa', 21 , 'Kitwe',"UNILUS")
print(newPerson.display())