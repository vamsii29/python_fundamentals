# This is my first python Program

def main():
    hello()
    name =input(("what is your full name? "))
    name = name.strip() # removes spaces infront and back
    name = name.title() # capitalises properly
    first, middle, last = name.split(" ") # splits the name
    hello(last)

# This is the function call
def hello(to="world!!!"):
    if(to == "world!!!"):
        print(f"Hello, {to}")
    else:
        print(f"Hello, {to}, congratulations on your first step to learn python ") 

main()