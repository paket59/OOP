'''тестовый_пуш'''


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


artur = User('Артур', 24)
# artur = User()
artur.food = 'chicken'
# print(artur.name)
# print(artur.age)
print(artur.food)