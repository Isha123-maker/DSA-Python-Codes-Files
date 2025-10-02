class Category:
    def __init__(self, name):
        # Each category has a name and a ledger (list of deposits/withdrawals)
        self.name = name
        self.ledger = []

    def get_balance(self):
        # Current balance = sum of all amounts in the ledger
        return sum(item['amount'] for item in self.ledger)
    
    def check_funds(self, amount):
        # Return True if enough balance is available, otherwise False
        if amount > self.get_balance():
            return False
        return True

    def deposit(self, amount, description=""):
        # Add a deposit to the ledger
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        # Withdraw money if sufficient funds exist
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def transfer(self, amount, other_category):
        # Transfer money from this category to another
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        # Nicely format the category ledger when printed
        title = self.name.center(30, "*") + "\n"
        items = ""
        for entry in self.ledger:
            # Description (cut off at 23 chars) + amount (right aligned)
            description = entry['description'][:23]
            amount = f"{entry['amount']:.2f}"
            items += f"{description:23}{amount:>7}\n"
        # Total balance at the bottom
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total
    

def create_spend_chart(categories):
    """
    Create a bar chart showing the percentage spent in each category.
    - Only withdrawals count as 'spent'.
    - Percentages are rounded down to the nearest 10.
    - Chart is drawn with 'o' markers.
    """

    # 1) Calculate total spent per category
    spent = []
    for cat in categories:
        total_spent_cat = 0
        for entry in cat.ledger:
            amt = entry.get("amount", 0)
            if amt < 0:  # withdrawals are negative
                total_spent_cat += -amt
        spent.append(total_spent_cat)

    total_spent_all = sum(spent)

    # 2) Calculate spend percentages (rounded down to nearest 10)
    percents = []
    for s in spent:
        if total_spent_all == 0:
            p = 0
        else:
            raw = int((s / total_spent_all) * 100)
            p = raw - (raw % 10)    # round down
        percents.append(p)

    # 3) Build chart lines
    lines = []
    lines.append("Percentage spent by category")

    # Y-axis labels from 100 down to 0
    for level in range(100, -1, -10):
        row = str(level).rjust(3) + "|"  # align numbers
        for p in percents:
            if p >= level:
                row += " o "
            else:
                row += "   "
        row += " "  # trailing space after last column
        lines.append(row)

    # Horizontal line under bars
    dash_len = 3 * len(categories) + 1
    lines.append("    " + "-" * dash_len)

    # Category names printed vertically
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        row = "     "  # spacing before names
        for cat in categories:
            if i < len(cat.name):
                row += cat.name[i] + "  "
            else:
                row += "   "
        lines.append(row)

    # Return full chart as string (no extra newline at end)
    return "\n".join(lines)


# ---------------- Example Usage ----------------
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

# Add deposits and withdrawals
food.deposit(1000, "initial deposit")
food.withdraw(150.25, "groceries")
food.withdraw(50.75, "restaurant and more food")

entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(200, "movies and games")

business.deposit(1000, "initial deposit")
business.withdraw(10, "paper")

# Show ledgers
print(food)
print(entertainment)
print(business)

# Show the spend chart
print(create_spend_chart([food, entertainment, business]))
# ---------------- Example Usage ----------------