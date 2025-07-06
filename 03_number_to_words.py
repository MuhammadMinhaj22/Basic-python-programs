import inflect

p = inflect.engine()

while True:

    num = input("Enter a number: ")
    
    if num.isdigit():
        words = p.number_to_words(num)
        print(f"In words: {words}")
    
    else:
        print("Please enter digits only (0-9).")
        break