class car:
    color = None
    model = None

    def car_details(self):
        print("Your car details is", self.color, self.model)


car_color = input("Enter your car color is\n")
car_model = input("Enter yuor car model is \n")

car_obj_ref = car()
car_obj_ref.color = car_color
car_obj_ref.model = car_model
car_obj_ref.car_details()