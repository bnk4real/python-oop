class Person:
    def __init__(self, id, fullname, age, position):
      self.id = id
      self.name = fullname
      self.age = age
      self.position = position
    def __str__(self):
        return f'Id: {self.id}, Name: {self.name}, Age: {self.age}, Position: {self.position}'

person1 = Person("1", "Alice", 30, "Marketing Officer")
person2 = Person("2", "Marie", 30, "Documents Officer")
person3 = Person("3", "Shawn", 30, "Engineer")
person4 = Person("4", "Hills", 30, "Accountant")
person5 = Person("5", "Jacks", 30, "Finance Officer")

userList = [person1, person2, person3, person4, person5]