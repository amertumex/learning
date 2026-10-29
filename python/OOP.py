class Cat:
    name =  None
    age = None
    isHappy = None

    def __init__(self, name, age, isHappy):
        self.set_data(name, age, isHappy)
        self.get_data()

    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print("Name:", self.name, "age:", self.age, "Happy:", self.isHappy)

cat1 = Cat("Barsik", 3, True)
cat2 = Cat("Max", 2, False)