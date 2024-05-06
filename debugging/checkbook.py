class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function Description:
        Deposits the specified amount into the checkbook balance.

        Parameters:
        - amount (float): The amount to be deposited.

        Returns:
        None
        """
        try:
            amount = float(amount)
            self.balance += amount
            print("Deposited ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid input. Please enter a numeric value for the amount.")

    def withdraw(self, amount):
        """
        Function Description:
        Withdraws the specified amount from the checkbook balance if sufficient funds are available.

        Parameters:
        - amount (float): The amount to be withdrawn.

        Returns:
        None
        """
        try:
            amount = float(amount)
            if amount > self.balance:
                print("Insufficient funds to complete the withdrawal.")
            else:
                self.balance -= amount
                print("Withdrew ${:.2f}".format(amount))
                print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid input. Please enter a numeric value for the amount.")

    def get_balance(self):
        """
        Function Description:
        Displays the current balance in the checkbook.

        Parameters:
        None

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = input("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = input("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
