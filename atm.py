atm = ''

def confirmPin(self,condition):
    pin = str(input('Confirm your pin:'))
    if pin != self.pin:
        print('The pin you have entered is correct')
        condition
    else:
        print('The pin you have entered is incorrect')

class ATM(object):
    def __init__(self,cardNumber,pin):
        self.pin = pin
        self.cardNumber = cardNumber
        self.balance = 1000000

    def checkBalance(self):
        print(self.balance)
        exitOrOptions()

    def depositMoney(self):
        depositAmount = int(input('How much money do you want to deposit:'))
        depconfirmation = input('Do you want to deposit this amount of money:')
        if depconfirmation == 'Yes' or depconfirmation == 'yes':
            self.balance = self.balance + depositAmount
            print(depositAmount,' has been deposited to your balance')
        exitOrOptions()

    def withdrawCash(self):
        withdrawalAmount = int(input('How much money do you want to withdraw:'))
        if self.balance >= withdrawalAmount:            
            confirmation = input('Do you want to withdraw this amount of money:')
            if confirmation == 'Yes' or confirmation == 'yes':
                    self.balance = self.balance - withdrawalAmount
                    print(withdrawalAmount,' has been withdrawed from your balance')
            exitOrOptions()
        else:
            print('You dont have enough balance to withdraw ',withdrawalAmount,' amount!')

def exitOrOptions():
    print('Do you want to exit or continue with options\nEnter exit to exit!\nEnter options to continue with other options!')
    exit1 = input('What do you want to do:')
    if exit1 == 'Exit' or exit1 == 'exit':
        exit()
    elif exit1 == 'Options' or exit1 == 'options':
        print('The other options are to check balance, withdraw money or deposit money!')
        options = input('What do you want to do:')
        if 'deposit' in options:
            print(options)
            atm.depositMoney()
        elif 'balance' in options:
            atm.checkBalance()
        elif 'withdraw' in options:
            atm.withdrawCash()
        else:
            print('Invalid function!')
            exitOrOptions()

print('Please enter your card Number and PIN')
print('Your PIN and card Number have to be less than 6 digits')
cardNo = int(input('Set your card number:'))
pin = int(input('Set your PIN number:'))

if cardNo in range(100000) and pin in range(100000):
    if cardNo == pin:
        print('Your pin cannot be the same as your cardNo.')
    else:
        atm = ATM(cardNo,pin)
        exitOrOptions()
elif cardNo > 100000 or pin > 100000:
    print('Your card and pin have to be less than 6 digits!')
else:
    print('Your card and pin have to be numbers!')