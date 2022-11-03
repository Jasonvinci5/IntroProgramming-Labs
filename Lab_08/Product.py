class Products:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity 
        self.id = id

    def num_stock(self, count):
        if count <= self.quantity:
            return True 
        else:
            return False

    def total_cost(self, count):
        total = self.price * count 
        return total

    def remove_stock(self, count):
        self.quantity = self.quantity - count
        return self.quantity


products = [Products("Ultrasonic Range finder", 2.50, 4), Products("Servo Motor", 14.99, 10), Products("Servo Controller", 44.95, 5), Products("Microcontroller", 34.95, 7), Products("Laser range finder", 149.99, 2), Products("Lithium polymer battery", 8.99, 8)]
print(products[0].num_stock(3))
print(products[0].name)
print(products[1].total_cost(2))
print(products[2].remove_stock(1))
