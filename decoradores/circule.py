class Circle:

    def __init__(self, radius:float):
        self._radius = radius
        

    @property
    def area(self) -> float:
        return 3.141592 * (self._radius) ** 2
    
    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, value: float) -> None:
        if value <= 0:
            raise ValueError("El radio debe ser mayor que 0")
        self._radius = value

circle = Circle(5)
print(circle.area)
circle.radius = -10
print(circle.area)