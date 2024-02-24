def make_pizza(*toppings):
    print(toppings)
    for topping in toppings:
        print(topping)


prachitosh = make_pizza("Mushroom", "onion", "Tomato")
Linkon = make_pizza("Mushroom","pineapple","Panneer","Tomato")
Liku = make_pizza("Mushroom","Pineapple","paneer","seetcorn")

def make_pizza_base(*topings,base):
    print(topings,base)
    for toping in topings:
        print(toping, end=" ")
Prachitosh= make_pizza_base("Mushroom","Onion","Tomato",base="Thin")
