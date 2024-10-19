menu = {
    "Daal Makhani": 130,
    "Butter Paneer": 220,
    "Shahi Paneer": 140,
    "Daal tadka": 100,
    "Mix veg": 110,
    "Chana masala": 90,
    "Malai kofta": 110,
    "Paneer lawabdaar": 140,
    "Butter Chicken": 180,
    "Chicken Changezi": 200,
    "kabab": 120,
    "Barbique Chicken": 200,
    "Tandoori Roti": 10,
    "Butter Tandoori Roti": 15,
    "Sada Naan": 12,
    "Butter Naan": 20,
    "Salad": 30,
    "Dry Fruit Ice Cream": 80,
    "Vanilla Ice cream": 50,
    "Choco Lava cake": 60
}

def welcome():
    print("Welcome to our Dhaba!")
    print("Here is our menu:")
    print("Dish Name\t\tPrice")
    print("---------------------------------")
    for dish, price in menu.items():
        print(f"{dish:<20}\t{price:.2f}")
    print("---------------------------------")

def order():
    total_bill = 0.0
    order_items = []
    while True:
        choice = input("kya khana chahenge aap? (enter 'done' agar khana peena ho gya ho toh): ").strip()
        
        if choice.lower() == 'done':
            break
        
        if choice in menu:
            price = menu[choice]
            order_items.append(choice)
            total_bill += price
            print(f"{choice} add kar diya.")
        else:
            print("sir yeh ni banta humare dhabe mein")
    
    return total_bill, order_items

def main():
    welcome()
    total_bill, order_items = order()
    
    print("\ndhanyawaad! yeh raha aapka bill")
    for item in order_items:
        print(f"- {item}")
    print(f"Total: ${total_bill:.2f}")

if __name__ == "__main__":
    main()
