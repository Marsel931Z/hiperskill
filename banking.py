import random
import sqlite3

conn = sqlite3.connect('./card.s3db')
cur = conn.cursor()
cur.execute('drop table card')
cur.execute("""CREATE TABLE IF NOT EXISTS card (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number TEXT,
        pin TEXT,
        balance INTEGER DEFAULT 0);""")
conn.commit()



class Menu():

    def __init__(self):
        print('1. Create an account')
        print('2. Log into account')
        print('0. Exit')
        self.choise = int(input())
        if self.choise == 1:
            CreateAcc()
        elif self.choise == 2:
            LogIn()
        elif self.choise == 0:
            print('Bye!')
            exit(1)


class CreateAcc():

    def __init__(self):
        self.IIN = '400000'
        self.num = str(random.randint(0, 999999999))
        while len(self.num) < 9:
            self.num = "0" + self.num
        self.cardnum = self.IIN + self.num
        self.cardnumlist = []
        for i in self.cardnum:
            self.cardnumlist.append(int(i))
        self.suma = 0
        for q in range(0, len(self.cardnumlist), 2):
            self.cardnumlist[q] = self.cardnumlist[q] * 2
            if self.cardnumlist[q] > 9:
                self.cardnumlist[q] -= 9
        for j in self.cardnumlist:
            self.suma += j
        if self.suma % 10 != 0:
            self.checksum = 10 - (self.suma % 10)
        else:
            self.checksum = 0
        self.cardnum = self.cardnum + str(self.checksum)
        self.pin = str(random.randint(0, 9999))
        while len(self.pin) < 4:
            self.pin = "0" + self.pin
        CreateAcc.check(self.cardnum, self.pin)
        print('Your card has been created')
        print('Your card number:')
        print(self.cardnum)
        print('Your card PIN:')
        print(self.pin)
        print()
        cur.execute(f'INSERT INTO card(number, pin) VALUES({self.cardnum}, {self.pin});')
        conn.commit()
        Menu()

    def check(cardnum, pin):
        if cardnum not in numbers:
            numbers.append(cardnum)
            base[cardnum] = int(pin)
        else:
            CreateAcc()


class LogIn():

    def __init__(self):
        print('Enter your card number:')
        self.cardnum = str(input())
        print('Enter your PIN:')
        self.pin = int(input())
        cur.execute(f"SELECT * FROM card WHERE number={self.cardnum} AND pin={self.pin}")
        if self.cardnum not in numbers or self.pin != base[self.cardnum]:
            print('Wrong card number or PIN!')
            Menu()
        elif bool(cur.fetchone()) is not False:
            print('You have successfully logged in!')
            LogIn.menu(self.cardnum, self.pin)

    def menu(card, pin):
        card1 = card
        pin1 = pin
        print('1. Balance')
        print('2. Add income')
        print('3. Do transfer')
        print('4. Close account')
        print('5. Log out')
        print('0. Exit')
        choise = int(input())
        if choise == 1:
            Balance.__init__(card1, pin1)
        elif choise == 2:
            Balance.income(card1, pin1)
        elif choise == 3:
            Balance.transfer(card1, pin1)
        elif choise == 4:
            LogIn.closeacc(card1, pin1)
        elif choise == 5:
            print('You have successfully logged out!')
            Menu()
        elif choise == 0:
            exit(1)

    def closeacc(card, pin):
        cur.execute(f"DELETE FROM card WHERE number={card} AND pin={pin}")
        conn.commit()
        print('The account has been closed')
        Menu()




class Balance():

    def __init__(self, card, pin):
        card1 = card
        pin1 = pin
        cur.execute(f"SELECT * FROM card WHERE number={card} AND pin={pin}")
        print("Balance: {}\n".format(cur.fetchone()[3]))
        LogIn.menu(card1, pin1)

    def income(card, pin):
        card1 = card
        pin1 = pin
        income = int(input('''Enter income:
        '''))
        cur.execute(f'UPDATE card SET balance = balance + {income} WHERE number={card} AND pin={pin}')
        conn.commit()
        print('Income was added!')
        LogIn.menu(card1, pin1)

    def transfer(card, pin):
        card1 = card
        pin1 = pin
        transfer_num = int(input('''Enter card number:
                '''))
        if Balance.lun(transfer_num) is True:
            if str(transfer_num) in numbers:
                suma = int(input('''Enter how much money you want to transfer:'
                                 '''))
                cur.execute(f"SELECT * FROM card WHERE number={card} AND pin={pin}")
                balance = cur.fetchone()[3]
                if balance >= suma:
                    cur.execute(f'UPDATE card SET balance = balance - {suma} WHERE number={card} AND pin={pin}')
                    cur.execute(f'UPDATE card SET balance = balance + {suma} WHERE number={str(transfer_num)}')
                    conn.commit()
                    print('Success!')
                else:
                    print('Not enough money!')
            else:
                print('Such a card does not exist.')
        else:
            print('Probably you made a mistake in the card number. Please try again!')
        LogIn.menu(card1, pin1)

    def lun(number):
        n = 0
        num = []
        for k in str(number):
            num.append(k)
        for j in range(0, len(num), 2):
            num[j] = int(num[j]) * 2
            if int(num[j]) > 9:
                num[j] = int(num[j]) - 9
        for i in range(len(num)):
            n += int(num[i])
        if n % 10 == 0:
            return True
        else:
            return False


numbers = []
base = {}
Menu()
