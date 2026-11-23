
print("Welcome to the Fantasy Item Shop!")

# Player
player_name = input("What is your name? ")
player_gold = 100
inventory = []

print(f"\nHello {player_name}! You have {player_gold} gold.")

# Shop items
items = ["Sword", "Shield", "Potion", "Bow"]

print("\nItems available:")
for item in items:
    print(item)

# Prices
sword_price = 50
shield_price = 40
potion_price = 20
bow_price = 60

# Shop menu
shop_open = True

while shop_open:
    print("\n=== Fantasy Item Shop ===")
    print("1. Buy Sword (50 gold)")
    print("2. Buy Shield (40 gold)")
    print("3. Buy Potion (20 gold)")
    print("4. Buy Bow (60 gold)")
    print("5. View Inventory")
    print("6. Exit Shop")

    choice = input("\nWhat would you like to do? ")

    match choice:
        case "1":
            if player_gold >= sword_price:
                player_gold -= sword_price
                inventory.append("Sword")
                print("You bought a Sword!")
                print(f"Remaining gold: {player_gold}")
            else:
                print("You don't have enough gold!")

        case "2":
            if player_gold >= shield_price:
                player_gold -= shield_price
                inventory.append("Shield")
                print("You bought a Shield!")
                print(f"Remaining gold: {player_gold}")
            else:
                print("You don't have enough gold!")

        case "3":
            if player_gold >= potion_price:
                player_gold -= potion_price
                inventory.append("Potion")
                print("You bought a Potion!")
                print(f"Remaining gold: {player_gold}")
            else:
                print("You don't have enough gold!")

        case "4":
            if player_gold >= bow_price:
                player_gold -= bow_price
                inventory.append("Bow")
                print("You bought a Bow!")
                print(f"Remaining gold: {player_gold}")
            else:
                print("You don't have enough gold!")

        case "5":
            if len(inventory) == 0:
                print("Your inventory is empty!")
            else:
                print("Your inventory:")
                for item in inventory:
                    print("-", item)

        case "6":
            print(f"Thanks for visiting, {player_name}!")
            print(f"You have {player_gold} gold left.")
            shop_open = False

        case _:
            print("Invalid option! Please choose 1-6.")

