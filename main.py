balance = 0.0


def deposit():
  global balance
  amount_deposited = float(input("Enter the amount to be deposited: "))
  balance += amount_deposited
  print(f"{amount_deposited} deposited successfully.")


def withdraw():
    global balance

    withdrawal_amount = float(input("Enter the amount to be withdrawn: "))

    if withdrawal_amount <= balance:
        balance -= withdrawal_amount
        print(f"{withdrawal_amount} withdrawn successfully.")
    else:
        print("Insufficient balance!")


def check_balance():
    print(f"Current Balance: {balance}")


def main():
  status =True
  account_holder_name = input("Enter the name: ")
  account_num = input("Enter your a/c number: ")

  while status:
    print("------Menu-----")
    print("1. Deposit")
    print("2. Withdrawal ")
    print("3. Check Balance")
    print("4. Exit")
    user_choice = input("Enter your choice:")
    if(user_choice == '1'):
      deposit()
    elif(user_choice == '2'):
      withdraw()
    elif(user_choice == '3'):
      print(f"Account Holder: {account_holder_name}")
      print(f"Account Number: {account_num}")
      check_balance()
      
    elif(user_choice == '4'):
      print("Thank you")
      status = False
      break
    else:
      print("Select a valid choice")

if __name__ =='__main__':
    main()
