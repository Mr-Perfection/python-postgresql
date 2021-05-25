class Book:
    TYPES = ("hard", "soft")
    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __str__(self):
        return f'{self.name} {self.book_type} {self.weight}'
    @classmethod
    def hardcover(cls, name, weight) -> "Book":
        return cls(name, cls.TYPES[0], weight+100)

    @staticmethod
    def helper_method(name, weight) -> str:
        return f'{name} {weight}'

print(Book.hardcover('yeezzyy', 100))