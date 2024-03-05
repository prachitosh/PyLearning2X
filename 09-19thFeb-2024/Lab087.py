# Class & Objects in Python
# Class -  Attributes and Behaviour

# Person -> Object Vani, Pramod, Shreeram
class person:
    # Attribute -> data member
    name = None
    age = None
    id = None
    Phone_no = None

    # Behaviour -> Methods (not the functions)
    def talk(self):
        print("i can talk")

    def another(self):
        print("I am a method")

    def sleep(self, name):
        print("i am a Method")
        print("Sleep", name)

    def walk(self):
        return "i am walking"


def anotherf():
    print("i am f(n)")


shreeram = person()
shreeram.name = "shreeram"
print(shreeram.name)

shreeram.talk()  # this belongs Shreeram

pramod = person()

Prachitosh = person()

# NOTHIGN IS THERE, SO CLEAN THE MEMORY
# exit the program
