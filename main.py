length = float(input("Enter the length of a zander in centimeters: "))
how_much_below_size_limit = 42-length
if length >= 42:
    print("Yey you can keep the fish!")
else:
    print(f"You should release the fish back into the lake because it's {how_much_below_size_limit:.1f} centimeters below the size limit.")