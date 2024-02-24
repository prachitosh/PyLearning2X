def makepizza(*toppings, base="Wheat"):
    print(toppings, base)
    for topping in toppings:
        print(topping)
    return toppings,base


Prachitosh_t, Prachitosh_b = makepizza("Onion", "Tomato", "Sweetcorn")
#Linkon = makepizza("Onion", "Tomato", "Sweetcorn", base="Thin crust")
print(Prachitosh_t)
print(Prachitosh_b)

