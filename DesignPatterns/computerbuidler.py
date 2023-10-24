class Computer:
    def __init__(self, cpu, ram, storage, grap_card = "NA"):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.grap_card = grap_card

    def __str__(self):
        return f"Computer: CPU={self.cpu}, RAM={self.ram}, Storage={self.storage}, Graphics Card={self.grap_card}"


class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.grap_card = "NA"

    def set_cpu(self, cpu):
        self.cpu = cpu
        return self

    def set_ram(self, ram):
        self.ram = ram
        return self

    def set_storage(self, storage):
        self.storage = storage
        return self

    def set_grap_card(self, grap_card):
        self.grap_card = grap_card
        return self

    def build(self):
        return Computer(self.cpu, self.ram, self.storage, self.grap_card)


builder = ComputerBuilder()
computer = builder.set_cpu("intel").set_ram("8GB").set_storage("1TB").set_grap_card("Nvidia").build()

print(computer)


class Mobile:
    def __init__(self, ram, size, cost, camera = "NA"):
        self.ram = ram
        self.size = size
        self.cost = cost
        self.camera = camera

    def __str__(self):
        return f"phone: ram-{self.ram}, size- {self.size}, cost- {self.cost}, camera- {self.camera}"


class MobileBuilder:
    def __init__(self):
        self.ram = None
        self.size = None
        self.cost = None
        self.camera = "NA"

    def set_ram(self, ram):
        self.ram = ram
        return self

    def set_size(self, size):
        self.size = size
        return self

    def set_cost(self, cost):
        self.cost = cost
        return self

    def set_camera(self, camera):
        self.camera = camera
        return self

    def build(self):
        return Mobile(self.ram, self.size, self.cost, self.camera)


builder = MobileBuilder()
mobile = builder.set_ram("512GB").set_cost("1000$").set_size("100MM").set_camera("12MP").build()

print(mobile)

