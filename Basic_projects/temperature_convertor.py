# this program is a simple file used to convert temperature from Celsius ↔ Fahrenheit

def main():
    unit = input("which temperature do you want to input? 'Celsius (C)' or 'Fahrenheit (F)':  ").strip().lower()
    while True:
      if unit == 'f':
        Fahrenheit_to_Celsius()
        break
      elif unit == 'c': 
        Celsius_to_Fahrenheit()
        break
      else:
        unit = input("Please enter 'Celsius (C)' or 'Fahrenheit (F)':  ").strip().lower()


# Converting from Celsius to Fahrenheit
def Celsius_to_Fahrenheit():
    X = int(input("What is the temperature?: "))
    f = (9/5) * X + 32
    print(f"{f} is the temperature in Fahrenheit")
    
    

# Converting from Fahrenheit to Celsius
def Fahrenheit_to_Celsius():
    X = int(input("What is the temperature?: "))
    c = (X - 32)*(5/9)
    print(f"{c} is the temperature in Celsius")
    

main()