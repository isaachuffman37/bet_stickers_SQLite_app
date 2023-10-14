import sqlite3
import sales

three_inches = 3
two_inches = 2



stickers = [
    ("lungs_sm", two_inches, 25),
    ("succulent_stamp", two_inches, 25),
    ("leaf_stamp", two_inches, 15),
    ("another_sticker", two_inches, 30),
    ("fu_ghost_sm", two_inches, 14),
    ("chamomile_stamp",two_inches,15),
    ("carabiner_sm",two_inches,15),
    ("fall_starbies_sm",two_inches,20),
    ("Jesus_sm",two_inches,25),
    ("flower_ghost_sm",two_inches,20),
    ("mary_poppins_sm",two_inches,15),
    ("wizard_of_oz_sm",two_inches,12),
    ("Jesus_lg",three_inches,20),
    ("cow_ghost_lg",three_inches,15),
    ("utah_sm",two_inches,20),
    ("alice_wond_sm",two_inches,14),
    ("pride_pred_sm",two_inches,16),
    ("cowboy_ghost_lg",three_inches,20),
    ("cowboy_ghost_sm",two_inches,30)
]

def display_menu():
    print("1. Add sticker")
    print("2. Remove sticker")
    print("3. See which stickers make the most money")
    print("4. Adjust quantity")
    print("5. Add sale")
    print("6. View sales table")
    print("7. View sticker table")
    print("8. Quit")


def main():
    print()
    print("WELCOME! This is a simple database for Bet Stickers. It is limited in its performance, but with this program, you can more easily track inventory and see which stickers are making you the most money (or the least haha). Please enjoy! ")
    print()
    response = ""
    while response != "8":
        display_menu()
        response = input("What would you like to do? ")
        if response == "1":
            amount = int(input("How many stickers do you want to add? "))
            for i in range(0,amount):
                sales.add_one_sticker()
            sales.view_stickers_table()
        elif response == "2":
            name = input("what is the name of the sticker you want to remove? ")
            sales.delete_sticker(name)

        elif response == "3":
            option = input("Do you want to view every sticker?(y/n) ")
            if option == "y":
                print()
                sales.get_all_revenue_info()
                print()
            else:
                limit = int(input("How many stickers would you like to view? "))
                print()
                sales.get_limited_revenue_info(limit)
                print()
        elif response == "4":
            name = input("What is the name of the sticker? ")
            amount = int(input("What is the amount you want to adjust it by? (positive or negative)"))
            sales.update_stock_amount(name, amount)
        elif response == "5":
            sales.add_one_sale()
        elif response == "6":
            print()
            sales.view_sales_table()
            print()
        elif response == "7":
            print()
            sales.view_stickers_table()
            print()

if __name__ == "__main__":
    main()

