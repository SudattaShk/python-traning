class vehicle:
    def __init__(self,color,brand,vehicle_type,price,number_of_wheels=4):
        self.color=color
        self.brand=brand
        self.vehicle_type=vehicle_type
        self.number_of_wheels=number_of_wheels
        self.price=price


    def get(self):
        print("color=",self.color,", brand=",self.brand,", price=",self.price)

v1=vehicle("white","tesla","car",9000000)
print(v1.get())
