class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.data = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data


single1 = Singleton()
single2 = Singleton()
single1.set_data("Hello India!")

print(single2 is single1)
print(single2.get_data())


class UpperTuple(tuple):

    def __new__(cls, iterable):
        upper_itr = (s.upper() for s in iterable)
        return super().__new__(cls, upper_itr)


def inher_immutable_upper_tuple():
    print("tuple in uppercase")
    print(UpperTuple(["hi", "there"]))

inher_immutable_upper_tuple()

# tup = (1, 3, 5)
# print(type(tup))




