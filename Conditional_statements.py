def check_area(area):
    print(f"Area is {area}")
    if area >= 10:
        print("Area is bigger than 10")
    elif area < 10 and area > 0:
        print("Area is smaller than 10")
    else:
        print("Invalid")
    pass


def triangle_area(base:float, height:float):
    area = 0.5 * base * height
    check_area(area)

def circle_area(radius:float):
    area = 3.14 * (radius ** 2)
    check_area(area)

def rectangle_area(length:float, width:float):
    area = length * width
    check_area(area)

triangle_area(5,10)
circle_area(1)
rectangle_area(-3,4)
