import matplotlib.pyplot as plt

import matplotlib.patches as patches

class Figure:
    def __init__(self, name, mid_x, mid_y):
        self.name = name
        self.mid_x = mid_x
        self.mid_y = mid_y

    def __str__(self):
        return f"{self.name} is a geometric figure"
    
    def __repr__(self):
        return f"A geometric figure, centre = {({self.mid_x}, {self.mid_y})}"
    
    def get_area(self):
        return 0
    
    def get_perimeter(self):
        return 0

    def __eq__ (self, other):
        print (f"{self.name} and {other.name} have {'' if self.get_area() == other.get_area() else 'not'} the same area") 
        return self.get_area() == other.get_area()
    
    def __lt__ (self, other):
         return self.get_area() < other.get_area()
    
    def __gt__ (self, other):
        return self.get_area() > other.get_area()
    
    def __le__ (self, other):
        return self.get_area() <= other.get_area()
    
    def __ge__ (self, other):
        return self.get_area() >= other.get_area()
    
    def transfer(self, new_mid_x, new_mid_y):
        self.mid_x = new_mid_x
        self.mid_y = new_mid_y

class Rectangle(Figure):
# The rectangle's angles A, B, C, D have coordinates:
    # A (left_x, up_y)
    # B (right_x, up_y)
    # C (right_x, down_y)
    # D (left_x, down_y)

    def __init__(self, name, mid_x, mid_y, width, height):
        super().__init__(name, mid_x, mid_y)
        self.width = width
        self.height = height

    def __repr__(self):
        return f"A rectangle, centre = {({self.mid_x}, {self.mid_y})}, width = {self.width}, height = {self.height}"
    
    def __str__(self):
        return f"{self.name} is a rectangle."
    
    def get_perimeter (self):
        return 2*(self.width + self.height)
    
    def get_area (self):
        return self.width*self.height
    
    def is_square (self):
        return self.width == self.height
    
    @property
    def left_x(self):
        return self.mid_x - 0.5*self.width
    
    @property
    def right_x(self):
        return self.mid_x + 0.5*self.width
    
    @property
    def down_y(self):
        return self.mid_y - 0.5*self.height
    
    @property
    def up_y(self):
        return self.mid_y + 0.5*self.height
    
    def is_in (self, points_x, points_y):
        if self.left_x < points_x < self.right_x and self.down_y < points_y < self.up_y:
            return True
        return False
    
    def set_x_y_area(self):
        pass
    
    def draw(self, field=None, facecolor = 'b', lw=2, color = 'y', alpha = 0.5): 
        
        if field == None:
            f, ax = plt.subplots()
            f.set_facecolor(facecolor)
            ax.grid()
            ax.set (xlim=(-10, 10), ylim=(-10, 10)) 
        else:
            f, ax = field
        
        picture = patches.Rectangle ((self.left_x, self.down_y), self.width, self.height, 
                                                lw = lw, color = color, alpha = alpha)
        ax.add_patch(picture)
        #plt.show()
        return f, ax

    def draw_in_other_field(self,other):
        pass

    def show_transfer(self):
        pass

from math import pi, sqrt

class Circle(Figure):
    def __init__(self, name, mid_x, mid_y, radius):
        super().__init__(name, mid_x, mid_y)
        self.radius = radius

    def __repr__(self):
        return f"A circle, centre = {({self.mid_x}, {self.mid_y})}"
    
    def __str__(self):
        return f"{self.name} is a circle."
    
    def get_perimeter (self):
        return 2*pi*self.radius
    
    def get_area (self):
        return pi*(self.radius**2)
    
    def is_unit_circle (self):
        return self.radius == 1 and self.mid_x == 0 and self.mid_y == 0
    
    def is_in (self, points_x, points_y):
        return self.radius >= sqrt((points_x - self.mid_x)**2 + (points_y - self.mid_y)**2)
    
    def draw(self):
        pass

    def draw_in_other_field(self,other):
        pass

    def show_transfer(self):
        pass

