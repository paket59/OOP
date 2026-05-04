class User:
    def __init__(self, name, age, email):
        if not User.is_email(email):
            raise ValueError(f'Неверная почта {email}')
        self.name = name
        self.age = age
        self.email = email

    @staticmethod
    def is_email(value):
        return '@' in value

artur = User('Artur', 41, 'artur@mail.ru')

