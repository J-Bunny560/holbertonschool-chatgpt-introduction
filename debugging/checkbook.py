class Checkbook:
    def __init__(self):
        """
        Function Description:
        Initializes a new Checkbook object with a balance of 0.0.

        Parameters:
        self: The Checkbook object itself.

        Returns:
        None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function Description:
        Deposits the specified amount into the checkbook balance.

        Parameters:
        self: The Checkbook object itself.
        amount (float): The amount to be deposited.

        Returns:
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function Description:
        Withdraws the specified amount from the checkbook balance if sufficient funds are available.

        Parameters:
        self: The Checkbook object itself.
        amount (float): The amount to be withdrawn.

        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function Description:
        Prints the current balance of the checkbook.

        Parameters:
        self: The Checkbook object itself.

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Function Description:
    The main function of the program, allowing users to interact with the Checkbook class.

    Parameters:
    None

    Returns:
    None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
