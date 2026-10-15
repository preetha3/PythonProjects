import sys
from datetime import datetime


# ANSI color codes
class Colors:
    MAGENTA = None
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


menu_items = {
    'pizza': 390,
    'pasta': 400,
    'burgers': 129,
    'apple': 210,
    'banana': 190,
    'apple juice': 180,
    'tea': 30,
    'coffee': 40,
    'milk': 45,
    'boost': 30,
    'bingo': 35,
    'mango': 40,
}

# ASCII Art for Cafe
cafe_banner = f"""
{Colors.BOLD}{Colors.CYAN}
    ╔═══════════════════════════════════════════════════════╗
    ║                                                       ║
    ║          ☕  PREETHAM'S PREMIUM CAFE  ☕             ║
    ║                                                       ║
    ║          🍕  Fresh • Delicious • Affordable  🍔      ║
    ║                                                       ║
    ╚═══════════════════════════════════════════════════════╝
{Colors.RESET}
"""

menu_display = f"""
{Colors.BOLD}{Colors.YELLOW}┌─── 📋 TODAY'S SPECIAL MENU ───┐{Colors.RESET}

{Colors.GREEN}🍕 FOOD ITEMS:{Colors.RESET}
  🍕 Pizza         : Rs. 390
  🍝 Pasta         : Rs. 400
  🍔 Burgers       : Rs. 129

{Colors.YELLOW}🍎 FRUITS:{Colors.RESET}
  🍎 Apple         : Rs. 210
  🍌 Banana        : Rs. 190
  🥭 Mango         : Rs. 40

{Colors.CYAN}🥤 BEVERAGES:{Colors.RESET}
  🧃 Apple Juice   : Rs. 180
  ☕ Coffee        : Rs. 40
  🍵 Tea           : Rs. 30
  🥛 Milk          : Rs. 45

{Colors.MAGENTA}🍪 SNACKS:{Colors.RESET}
  🍪 Bingo         : Rs. 35
  ⚡ Boost         : Rs. 30

{Colors.BOLD}{Colors.YELLOW}└────────────────────────────────┘{Colors.RESET}
"""


def print_header():
    """Print decorated header"""
    print(cafe_banner)
    print(f"{Colors.BOLD}{Colors.BLUE}{'=' * 60}{Colors.RESET}")
    print(f"{Colors.GREEN}📅 Date & Time: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}{Colors.RESET}")
    print(f"{Colors.BLUE}{'=' * 60}{Colors.RESET}\n")


def print_menu():
    """Display the menu"""
    print(menu_display)


def get_order_input(order_number):
    """Get order input from user"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}Order #{order_number}:{Colors.RESET}")
    while True:
        item = input(f"{Colors.YELLOW}👉 Please enter item name: {Colors.RESET}").strip().lower()
        if not item:
            print(f"{Colors.RED}❌ Input cannot be empty! Please try again.{Colors.RESET}")
            continue
        return item


def validate_and_add_item(item, order_total):
    """Validate item and add to order"""
    if item in menu_items:
        price = menu_items[item]
        order_total += price
        print(f"{Colors.GREEN}✅ '{item.title()}' (Rs. {price}) added to your order!{Colors.RESET}")
        return order_total, True
    else:
        print(f"{Colors.RED}❌ '{item}' is not available in our menu. Please choose from available items.{Colors.RESET}")
        return order_total, False


def ask_continue():
    """Ask if customer wants to add more items"""
    while True:
        choice = input(f"\n{Colors.CYAN}Would you like to add another item? (yes/no): {Colors.RESET}").strip().lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print(f"{Colors.RED}❌ Invalid input! Please enter 'yes' or 'no'.{Colors.RESET}")


def print_bill(order_total, items_list):
    """Print final bill"""
    print(f"\n{Colors.BOLD}{Colors.GREEN}")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 15 + "🧾 FINAL BILL - PREETHAM'S CAFE 🧾" + " " * 10 + "║")
    print("╠" + "═" * 58 + "╣")

    for i, (item, price) in enumerate(items_list, 1):
        print(f"║ {i}. {item.title():<35} Rs. {price:>6} ║")

    print("╠" + "═" * 58 + "╣")
    total_line = f"  TOTAL AMOUNT: Rs. {order_total}"
    print(f"║{total_line:^58}║")
    print("╠" + "═" * 58 + "╣")
    print(f"║ {'Thank you for your order! Visit Again 😊':^58} ║")
    print("╚" + "═" * 58 + "╝")
    print(f"{Colors.RESET}")


def main():
    """Main function"""
    print_header()
    print_menu()

    order_total = 0
    items_list = []
    order_count = 0

    while True:
        order_count += 1
        item = get_order_input(order_count)
        new_total, success = validate_and_add_item(item, order_total)

        if success:
            order_total = new_total
            items_list.append((item, menu_items[item]))

            if not ask_continue():
                break
        else:
            # Ask if they want to retry or continue
            retry = input(
                f"{Colors.YELLOW}Would you like to try another item? (yes/no): {Colors.RESET}").strip().lower()
            if retry not in ['yes', 'y']:
                if order_total > 0:
                    break
                else:
                    print(f"{Colors.RED}❌ You haven't ordered anything yet!{Colors.RESET}")

    if order_total > 0:
        print_bill(order_total, items_list)
    else:
        print(f"\n{Colors.RED}{Colors.BOLD}❌ No valid orders placed. Thank you for visiting!{Colors.RESET}")

    print(f"\n{Colors.CYAN}See you next time at Preetham's Cafe! 👋{Colors.RESET}\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Program interrupted by user. Thank you!{Colors.RESET}\n")
        sys.exit(0)
