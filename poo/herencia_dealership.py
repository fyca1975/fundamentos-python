class vehicle:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.is_available = True

    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Price: {self.price}")
    
    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"The vehicle {self.brand} {self.model} has been sold.")
        else:
            print(f"The vehicle {self.brand} {self.model} is not available.")
    
    def check_availability(self):
        return self.is_available    
    
    def get_price(self):
        return self.price   
    
    def start_engine(self):
        raise NotImplementedError("This method must be implemented in the child class.")
        
    def stop_engine(self):       
        raise NotImplementedError("This method must be implemented in the child class.")
    
# Crear una clase car que hereda de vehicle    
class Car(vehicle):
    # def __init__(self, brand, model, year, price, fuel_type):
    #     super().__init__(brand, model, year, price)
    #     self.fuel_type = fuel_type
        
    def start_engine(self):
        if not self.is_available:
            return f"The car engine cannot be started. {self.brand}"
        else:    
            return f"The car engine has been started. {self.brand}"
        
    def stop_engine(self):
        if not self.is_available:
            return f"The car engine cannot be stopped. {self.brand}"
        else:    
            return f"The car engine has been stopped. {self.brand}"
class Bike(vehicle):

    def start_engine(self):
        if not self.is_available:
            return f"The bike engine cannot be started. {self.brand}"
        else:    
            return f"The bike engine has been started. {self.brand}"
        
    def stop_engine(self):
        if not self.is_available:
            return f"The bike engine cannot be stopped. {self.brand}"
        else:    
            return f"The bike engine has been stopped. {self.brand}"    

class Truck(vehicle):
    
    def start_engine(self):
        if not self.is_available:
            return f"The truck engine cannot be started. {self.brand}"
        else:    
            return f"The truck engine has been started. {self.brand}"
        
    def stop_engine(self):
        if not self.is_available:
            return f"The truck engine cannot be stopped. {self.brand}"
        else:    
            return f"The truck engine has been stopped. {self.brand}"

class Customer:
    def __init__(self, name, age, budget):
        self.name = name
        self.age = age
        self.budget = budget
        self.vehicles = []
    
    def buy_vehicle(self, vehicle: vehicle):

        if vehicle.check_availability():
            vehicle.sell()
            self.vehicles.append(vehicle)   
            print(f"{self.name} has bought the vehicle {vehicle.brand} {vehicle.model}.")
        else:
            print(f"The vehicle {vehicle.brand} {vehicle.model} is not available.")        
    
    def inquire_vehicle(self, vehicle: vehicle):
        if vehicle.check_availability():
            print(f"The vehicle {vehicle.brand} {vehicle.model} is available. The price is {vehicle.get_price()}.")
        else:
            print(f"The vehicle {vehicle.brand} {vehicle.model} is not available.")

    
    def show_vehicles(self):
        print(f"{self.name} has the following vehicles:")
        for vehicle in self.vehicles:
            print(f"{vehicle.brand} {vehicle.model}")
    
    def show_budget(self):
        print(f"{self.name} has a budget of {self.budget}.")

class Dealership:
    def __init__(self):
        self.iventory = []
        self.customers = []
    
    def add_vehicle(self, vehicle: vehicle):
        self.iventory.append(vehicle)
        print(f"The vehicle {vehicle.brand} {vehicle.model} has been added to the iventory.")
    
    def add_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"The customer {customer.name} has been added to the dealership.")
    
    def show_vehicles(self):
        print("The dealership has the following vehicles:")
        for vehicle in self.iventory:
            print(f"{vehicle.brand} {vehicle.model}")   