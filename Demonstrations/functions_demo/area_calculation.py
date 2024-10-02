import numpy as np

def area_rect(length, width):
    """Determine the area of a rectangle with length and width"""
    area = length * width
    return area

def area_triangle(base, height):
    """Determine the area of a triangle with base and height"""
    area = 0.5 * base * height
    return area

def area_circle(radius):
    """Determine the area of a rectangle with length and width"""
    area = np.pi * radius ** 2
    return area

def find_area(length, width = None, shape = None):
    """Find the area of a geometric shape"""
    
    if shape == "rectangle":
        area = length * width

    elif shape == "triangle":
        area = 0.5 * length * width

    elif shape == "circle":
        area = np.pi * length ** 2

    else:
        raise ValueError(f'"{shape}" is not a valid parameter for "shape"')
    
    return area