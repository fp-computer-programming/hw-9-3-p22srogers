# Author: SMR (AMDG) 01/18/22
def temp_convert():
    while True:
        try: 
            temp = float(input("Enter the temperature: "))
            type = input("Convert to(f/c)? ").upper()
            if type == "C":
                result = (temp * (9/5))+32
                print("The temperature in celsius is {0}.".format(result))
            elif type == "F":
                result = (temp-32)*(5/9)
                print("The temperature in Fahrenheit is {0}.".format(result))
            else:
                print("Invalid input. Enter 'f' for fahrenheit and 'c' for celsius.")
        except ValueError:
            print("Invalid input. Use only numerical values for temperature.")
temp_convert()