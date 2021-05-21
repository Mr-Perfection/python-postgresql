class Book:
    TYPES = ("hard", "soft")
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    @classmethod
    def hardcover(cls, name, weight):
        return cls(name, TYPES[0], weight+100)

    @staticmethod
    def helper_method(name, weight):
        return f'{name} {weight}'
