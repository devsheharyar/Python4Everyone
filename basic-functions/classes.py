class vehical:
    def __init__(self,n,a):
        self.company = n
        self.model = a
    def get_model(self):
        return self.model

car = vehical('toyota','corolla')
if __name__ == "__main__":
    print(car.company)