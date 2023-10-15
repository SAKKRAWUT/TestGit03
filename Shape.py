import math

# Base class: Shape
class Shape:
    # Class-level variable to keep track of Shape IDs
    shape_count = 0
    
    def __init__(self, color):
        self.color = color
        Shape.shape_count += 1
        self.shape_id = Shape.shape_count

    def area(self):
        pass

    def perimeter(self):
        pass

    def display_info(self):
        print(f"Shape ID: {self.shape_id}") 
        print(f"Shape: {self.__class__.__name__}")
        print(f"Color: {self.color}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

# Subclass: Rectangle
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Subclass: Circle
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Create instances of the shapes
rectangle1 = Rectangle("Blue", 4, 5)
rectangle2 = Rectangle("Green", 2, 5)
rectangle3 = Rectangle("Purple", 3, 2)
circle1 = Circle("Yellow", 3)
circle2 = Circle("Pink", 5)
circle3 = Circle("Violet", 7)

# Display information about the shapes
print("\n")
rectangle1.display_info()
print("\n")
rectangle2.display_info()
print("\n")
rectangle3.display_info()
print("\n")
circle1.display_info()
print("\n")
circle2.display_info()
print("\n")
circle3.display_info()
print("\n")

