class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

# Creating instances of Singleton
s1 = Singleton()
s2 = Singleton()

# Both instances refer to the same object
print(s1 is s2)  # Output: True