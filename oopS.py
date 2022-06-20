class Computer:

    def __init__(self):
        self.name="amit"
        self.age=19
    #
    # def update(self,):
    #     self.age=20

    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False


c1=Computer()
c2=Computer()
c1.age=30

if c1.compare(c2):
    print("same")
else:
    print("different")

# c1.name="Sanket"
# c1.age=12

# c1.update()

print(c1.name)
print(c2.name)
print(c1.age)