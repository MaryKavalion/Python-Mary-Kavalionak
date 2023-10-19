import matplotlib.pyplot as plt

import matplotlib.patches as patches
import time

import random

from math import pi, sqrt

class NotImplementedError(Exception):
    def __init__(self, message="This method or property is not implemented in the subclass"):
        self.message = message

class PositiveNumberError(Exception):
    def __init__(self, message="Should be a positive number"):
        self.message = message
        
class DivisionByZeroError(Exception):
    def __init__(self, message="Division by zero is not allowed"):
        self.message = message

class Figure:
    """
    Base class for geometric figures.
    :param name: Name of the figure.
    :param mid_x: X-coordinate of the figure's center.
    :param mid_y: Y-coordinate of the figure's center.
    :param colors: List of colors for drawing.
    :param left_x: Leftmost x-value when projecting the figure onto the x-axis.
    :param right_x: Rightmost x-value when projecting the figure onto the x-axis.
    :param up_y: Upmost y-value when projecting the figure onto the y-axis.
    :param down_y: Downmost y-value when projecting the figure onto the y-axis.
    """

    def __init__(self, name, mid_x, mid_y):
        self.name = name
        self.mid_x = mid_x
        self.mid_y = mid_y

    @property
    def mid_x(self):
        return self._mid_x
    
    @mid_x.setter
    def mid_x(self, mid_x):
        if type (mid_x) != int:
            raise TypeError("Must be numeric")
        else:
            self._mid_x = mid_x

    @property
    def mid_y(self):
        return self._mid_y
    
    @mid_y.setter
    def mid_y(self, mid_y):
        if type (mid_y) != int:
            raise TypeError("Must be numeric")
        else:
            self._mid_y = mid_y

    @property
    def colors(self):
        return ['b', '#2A33D5', '#9871E0', '#835EA0', '#1775C8', '#017294', '#5305A8',
                'g', '#4DE44E', '#9AC972', '#5DE027', '#7AE0CB', '#63E928', '#0A8D35',
                'r', '#C996C3', '#FE3920', '#C94671', '#E72EA8', '#E50A2F', '#BB489F',
                'c', '#C0728C', '#7C5467', '#DE7B37', '#452A2E', '#C5A652', '#AE5837',
                'm', '#AA4495', '#743E62', '#7A356C', '#DD17F7', '#A56797', '#6E0EB0',
                'y', '#D6B907', '#F6E619', '#6856D6', '#D7FA22', '#F6B567', '#D1CF4E',
                'k', '#CCC4CF', '#D2BCD6', '#BFB1AB', '#31081E', '#3B2949', '#2D2E0E']
    
    def __str__(self):
        return f"{self.name} is a geometric figure"
    
    def __repr__(self):
        return f"A geometric figure, centre = {({self.mid_x}, {self.mid_y})}"
    
    def get_area(self):
        raise NotImplementedError()
    
    def get_perimeter(self):
        raise NotImplementedError()

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
    
    def _get_settings(self, field, facecolor, indentation):
        """
        Setting plt's figure and axis for drawing function.
        :param field: If want to add the figure to already existing picture, else - None
        :type field: list [figure, axis]
        :param indentation: Sets the indentation from the figure to the field's edge.
        :type indentation: float, int
        
        :return: The field with the picture in it.
        :rtype: list [figure, axis]
        """
        if field is None:
            f, ax = plt.subplots()
            f.set_size_inches(6,6)
            if facecolor is not None:
                f.set_facecolor(facecolor)
            else:
                f.set_facecolor(random.choice(self.colors))

            ax.grid()

            self._plot_axis(indentation)

        else:
            f, ax = field
            self._plot_axis(indentation)

        return f, ax
    
    @property
    def left_x(self):
        raise NotImplementedError()
    
    @property
    def right_x(self):
        raise NotImplementedError()
    
    @property
    def down_y(self):
        raise NotImplementedError()
    
    @property
    def up_y(self):
        raise NotImplementedError()
    
    # A set of auxiliary functions used for automatically setting the displayed axis on the figure (using matplotlib)
    def _find_left_lim(self, indentation):
        return (self.left_x - indentation) if self.left_x <= indentation else 0
    
    def _find_right_lim(self, indentation):
        return (self.right_x + indentation) if self.right_x >= indentation else 0
    
    def _find_up_lim (self, indentation):
        return (self.up_y + indentation) if self.up_y >= indentation else 0
    
    def _find_down_lim (self, indentation):
        return (self.down_y - indentation) if self.down_y <= indentation else 0
    
    def _plot_axis(self, indentation):
        # the function which draws 2 lines which set the area of the axis shown 
        # according to our figures sizes and coordinates
        # else would have to set xlim, ylim manually each time, 
        # because patches package shows area with xlim (0, 1), ylim (0, 1) as default
        x_abscissa = [self._find_left_lim(indentation), self._find_right_lim(indentation)]
        y_abscissa = [0, 0]
        x_ordinates = [0, 0]
        y_ordinates = [self._find_down_lim(indentation), self._find_up_lim(indentation)]

        return plt.plot(x_abscissa, y_abscissa, x_ordinates, y_ordinates, color = 'k', alpha = 0.1)
    
    def transfer(self, new_mid_x, new_mid_y):
        """
        Setting new coordinates for the figure's centre.
        :param new_mid_x: New x-coordinate of the centre
        :type new_mid_x: int, float
        :param new_mid_y: New y-coordinate of the centre
        :type new_mid_y: int, float
        
        :return: Old parameters for using them in the transfer visualizing.
        :rtype: Dictionary 
        """
        if not (isinstance(new_mid_x, (int, float)) and (isinstance(new_mid_y, (int, float)))): 
            raise TypeError(f"{new_mid_x =} and {new_mid_y=} should both be a number")
        old_mid_x = self.mid_x
        old_mid_y = self.mid_y
        old_edge_x = self.left_x
        old_edge_y = self.down_y
        self.mid_x = new_mid_x
        self.mid_y = new_mid_y
        return {"old_mid": (old_mid_x, old_mid_y),
                "old_edge": (old_edge_x, old_edge_y)}
    
    def _calculate_step(self, old_coordinate, new_coordinate, num_steps):
        # function for setting small moves (steps) for visualizing the transfer
        if num_steps == 0:
            raise DivisionByZeroError()
        elif num_steps < 0:
            raise PositiveNumberError()
        elif not isinstance(num_steps, (int, float)) : 
            raise TypeError(f"{num_steps =} should be a number")
        return -(old_coordinate - new_coordinate) / num_steps
    
    def _calculate_coordinates(self, start_coordinate, step, num_steps):
        # finding new coordinates of the figure on each of the transfer's steps
         return [start_coordinate + x*step for x in range (num_steps)]
    
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

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if type (width) != int or width < 0:
            raise PositiveNumberError()
        else:
            self._width = width

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        if type (height) != int or height < 0:
            raise PositiveNumberError()
        else:
            self._height = height

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
        """
        Checks whether the point is or not inside the rectangle.
        """
        if not (isinstance(points_x, (int, float)) and isinstance(points_y, (int, float))):
            raise TypeError("points_x and points_y should be numeric values")
        if self.left_x < points_x < self.right_x and self.down_y < points_y < self.up_y:
           return True
        return False

    def draw(self, field=None, facecolor = None, lw=2, color = None, alpha = 0.75, indentation = 2): 
     
        f, ax = self._get_settings(field, facecolor, indentation)
            
        picture = patches.Rectangle ((self.left_x, self.down_y), self.width, self.height, lw = lw, 
                                     color = color if color is not None else random.choice(self.colors), alpha = alpha)
        
        
        ax.add_patch(picture)
        plt.show()
        return f, ax
    
    def transfer_and_show(self, new_mid_x, new_mid_y, field = None, facecolor = 'm', indentation = 2, num_steps=4, lw=2, color='k'):
        if not (isinstance(new_mid_x, (int, float)) and (isinstance(new_mid_y, (int, float)))): 
            raise TypeError(f"{new_mid_x =} and {new_mid_y=} should both be a number")
        old_position = self.transfer(new_mid_x, new_mid_y) #{"old_mid": (old_mid_x, old_mid_y),
                                                            # "old_edge": (old_edge_x, old_edge_y)}

        plt.ion()
        f, ax = self._get_settings(field, facecolor, indentation)
        f.set_size_inches(6,6)
        step_x_rectangle = self._calculate_step(old_position["old_edge"][0], self.left_x, num_steps)
        step_y_rectangle = self._calculate_step(old_position["old_edge"][1], self.down_y, num_steps)
        x_edges = self._calculate_coordinates(old_position["old_edge"][0], step_x_rectangle, num_steps)
        y_edges = self._calculate_coordinates(old_position["old_edge"][1], step_y_rectangle, num_steps)
        for ind in range (num_steps):
            
            picture = patches.Rectangle ((x_edges[ind], y_edges[ind]), self.width, self.height, lw = lw, 
                                     color = color, alpha = 0.5)
            ax.add_patch(picture)
            self._plot_axis
            time.sleep(0.5)
        final_picture = patches.Rectangle ((self.left_x, self.down_y), self.width, self.height, lw = lw, 
                                     color = random.choice(self.colors), alpha = 0.8)
        ax.add_patch(final_picture)
        plt.ioff()
        plt.show()

class Circle(Figure):
    def __init__(self, name, mid_x, mid_y, radius):
        super().__init__(name, mid_x, mid_y)
        self.radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        if type (radius) != int or radius < 0:
            raise PositiveNumberError()
        else:
            self._radius = radius

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
    
    @property
    def left_x(self):
        return self.mid_x - self.radius
    
    @property
    def right_x(self):
        return self.mid_x + self.radius
    
    @property
    def down_y(self):
        return self.mid_y - self.radius
    
    @property
    def up_y(self):
        return self.mid_y + self.radius
    
    def draw(self, field=None, facecolor = None, lw=2, color = None, alpha = 0.75, indentation = 2):

        f, ax = self._get_settings (field, facecolor, indentation)
        
        picture = patches.Circle ((self.mid_x, self.mid_y), self.radius, lw = lw, 
                                     color = color if color is not None else random.choice(self.colors), alpha = alpha)
        
        ax.add_patch(picture)
        plt.show()
        return f, ax 

    def transfer_and_show(self, new_mid_x, new_mid_y, field = None, facecolor = 'm', indentation = 2, num_steps=4, lw=2, color='k'):
        if not (isinstance(new_mid_x, (int, float)) and (isinstance(new_mid_y, (int, float)))): 
            raise TypeError(f"{new_mid_x =} and {new_mid_y=} should both be a number")
        old_position = self.transfer(new_mid_x, new_mid_y) #{"old_mid": (old_mid_x, old_mid_y),
                                                            # "old_edge": (old_edge_x, old_edge_y)}

        plt.ion()
        f, ax = self._get_settings(field, facecolor, indentation)
        f.set_size_inches(6,6)
        step_x_circle = self._calculate_step(old_position["old_mid"][0], self.mid_x, num_steps)
        step_y_circle = self._calculate_step(old_position["old_mid"][1], self.mid_y, num_steps)
        x_centres = self._calculate_coordinates(old_position["old_mid"][0], step_x_circle, num_steps)
        y_centres = self._calculate_coordinates(old_position["old_mid"][1], step_y_circle, num_steps)
        for ind in range (num_steps):
            
            picture = patches.Circle ((x_centres[ind], y_centres[ind]), self.radius, lw = lw, 
                                     color = color, alpha = 0.5)
            ax.add_patch(picture)
            self._plot_axis
            time.sleep(0.5)
        final_picture = patches.Circle ((self.mid_x, self.mid_y), self.radius, lw = lw, 
                                     color = random.choice(self.colors), alpha = 0.8)
        ax.add_patch(final_picture)
        plt.ioff()
        plt.show()

