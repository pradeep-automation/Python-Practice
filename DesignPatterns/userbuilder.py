class UserProfile:
    def __init__(self, username, email, age, address, phone):
        self.username = username
        self.email = email
        self.age = age
        self.address = address
        self.phone = phone

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}, Age: {self.age}, Address: {self.address}, Phone: {self.phone}"

class UserProfileBuilder:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age
        self.address = None
        self.phone = None

    def set_address(self, address):
        self.address = address
        return self

    def set_phone(self, phone):
        self.phone = phone
        return self

    def build(self):
        return UserProfile(self.username, self.email, self.age, self.address, self.phone)

# Test data generation
user1 = UserProfileBuilder("user1", "user1@example.com", 25).set_address("123 Main St").set_phone("555-1234").build()
user2 = UserProfileBuilder("user2", "user2@example.com", 30).build()

print(user1)
print(user2)
