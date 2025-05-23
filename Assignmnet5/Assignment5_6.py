# Celsius to Fahrenheit Converter
#Accept temperature in Celsius and convert it to Fahrenheit using the formula:
#F= (C x 9/5) + 32
def celsiusToFahrenheit(celsius):
    F = (celsius * 9/5) + 32
    return F

def main():
    c = float(input("Enter temperature in Celsius: "))
    f = celsiusToFahrenheit(c)
    print("temprature in Fahrenheit",f)

if __name__ == "__main__":
    main()
