class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("cpu:", self.cpu, "ram:", self.ram)


comp1 = Computer("i5", 8)
comp2 = Computer("i7", 16)
comp1.config()
comp2.config()
