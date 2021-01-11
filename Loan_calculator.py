import math
import argparse

def convert(x):
    if x != None:
        x = float(x)
    else:
        x = 0
    return x


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")

args = parser.parse_args()
listt = [args.payment, args.principal, args.periods, args.interest]
principal = convert(args.principal)
periods = convert(args.periods)
payment = convert(args.payment)
interest = convert(args.interest)

if len(listt) != 4:
    print("Incorrect parameters")
elif (args.type != "diff" and args.type != "annuity") or args.type == None:
    print("Incorrect parameters")
elif args.type == "diff" and payment != 0:
    print("Incorrect parameters")
elif interest == 0:
    print("Incorrect parameters")
elif interest < 0 or periods < 0 or principal < 0 or payment < 0:
    print("Incorrect parameters")
else:
    i = interest / 12 / 100
    if args.type == "annuity":
        if periods == 0:
            periods = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
            years = periods // 12
            rest = periods % 12
            if years == 0:
                if periods == 1:
                    print(f"It will take {rest} month to repay this loan!")
                else:
                    print(f"It will take {rest} months to repay this loan!")
            else:
                print(f"It will take {years} years and {rest} months to repay this loan!")
        elif payment == 0:
            payment = math.ceil(principal * (i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
            print(f"Your monthly payment = {payment}!")
        elif principal == 0:
            principal = math.ceil(payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)))
            print(f"Your loan principal = {principal}!")
        over = math.ceil(payment * periods - principal)
        print(f"Overpayment = {over}")
    else:
        over = 0
        for m in range (1, int(periods) + 1):
            payment = math.ceil(principal / periods + i * (principal - principal * (m - 1) / periods))
            print(f"Month {m}: payment is {payment}")
            over += payment
        over = math.ceil(over) - principal
        print(f"\nOverpayment = {over}")


    
    
