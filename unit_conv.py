#Unit Convertor
#Created By Shreyas
#Created On 11th July 2025

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return km / 0.621371

def kg_to_pound(kg):
    return kg * 2.20462

def pound_to_kg(pound):
    return kg / 2.20462

def celsius_to_farenheit(celsius):
    return (9/5 * celsius)+ 32

def farenheit_to_celsius(farenheit):
    return (farenheit - 32) *5/9

def main():
    print("Select conversation")
    print("1 - km to miles")
    print("2 - miles to km")
    print("3 - kg to pound")
    print("4 - pound to kg")
    print("5 - celsius to farenheit")
    print("6 - farenheit to celsius")
    print("7 - Exit")

choice = input("Enter number (1–7): ")
value = 0
if choice != '7':
    value = float(input("Enter value: "))
    
funcs = [
    km_to_miles,
    miles_to_km,
    kg_to_pound,
    pound_to_kg,
    celsius_to_farenheit,
    farenheit_to_celsius,
    lambda x: print("Goodbye!!!")
]

try:
    result = funcs[int(choice)-1](value)
    if choice!="7":
        print("Result",result)
except:
    print("Invalid Input.")
     


