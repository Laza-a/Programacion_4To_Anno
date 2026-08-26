# Clase padre: SavingsAccount
class SavingsAccount:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.__balance = balance

    # Getter
    def get_balance(self):
        return self.__balance


# Clase hija: PremiumSavings
class PremiumSavings(SavingsAccount):
    def show_details(self):
        print("\n--- Premium Savings Account ---")
        print("Holder:", self.holder_name)
        print("Balance:", self.get_balance())


# Clase padre: CheckingAccount
class CheckingAccount:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.__balance = balance

    # Getter
    def get_balance(self):
        return self.__balance


# Clase hija: BusinessChecking
class BusinessChecking(CheckingAccount):
    def show_details(self):
        print("\n--- Business Checking Account ---")
        print("Holder:", self.holder_name)
        print("Balance:", self.get_balance())


# Input for Savings Account
print("Enter information for the Savings Account")
savings_name = input("Holder name: ")
savings_balance = float(input("Initial balance: "))

# Input for Checking Account
print("\nEnter information for the Checking Account")
checking_name = input("Holder name: ")
checking_balance = float(input("Initial balance: "))


# Create objects
savings_account = PremiumSavings(savings_name, savings_balance)
checking_account = BusinessChecking(checking_name, checking_balance)


# Display details
savings_account.show_details()
checking_account.show_details()