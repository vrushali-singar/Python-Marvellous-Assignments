#Area and Perimeter of Rectangle
#Accept the length and width of a rectangle. Calculate and display the area and perimeter.
def areaRectangle(value1,value2):
    a = value1 * value2
    return a
def perimeterRectangle(value1,value2):
    p = 2 * (value1 + value2)
    return p
def main():
    length = float(input("Enter Length :"))
    width = float(input("Enter width :"))
    area = areaRectangle(length,width)
    print("Area of Rectangle is :",area)
    perimeter = perimeterRectangle(length,width)
    print("Perimeter of Rectangle is :",perimeter)

if __name__ == "__main__":
    main()
