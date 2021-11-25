import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str, required=False, choices=["annuity", "diff"], help="")
parser.add_argument("--principal", type=int, required=False, help="")
parser.add_argument("--periods", type=int, required=False, help="")
parser.add_argument("--interest", type=float, required=False, help="")
parser.add_argument("--payment", type=int, required=False, help="")

args = vars(parser.parse_args())
"""
Assigning args to variables
"""
type_lc = args["type"]
prin_lc = args["principal"]
inter_lc = args["interest"]
month = args["periods"]
pay_lc = args["payment"]
"""
Check whether:
Required parameters are entered
"""
if (type_lc is None) or (type_lc == "diff" and pay_lc is not None) or (inter_lc is None) or (month is not None and month < 0):
    print("Incorrect parameters")
else:
    i = inter_lc / (12 * 100)
    if type_lc == "diff":
        # Assigning prin_lc to overpayment
        overpayment_d = prin_lc
        # Looping for number of months
        for x in range(1, month + 1):
            d_mon = math.ceil((prin_lc/month) + (i * (prin_lc - ((prin_lc * (x - 1))/month))))
            overpayment_d -= d_mon
            print(f'Month {x}: payment is {d_mon}')
        print(f'\nOverpayment = {abs(overpayment_d)}')
    elif type_lc == "annuity":
        # To find principle
        if prin_lc is None:
            prin_a = pay_lc / ((i * math.pow((1 + i), month)) / (math.pow((1 + i), month) - 1))
            overpayment_ap = abs(prin_a - (pay_lc * month))
            print(f'Your loan principal = {prin_a}')
            print(f'Overpayment = {overpayment_ap}')
        # To find no. of months
        elif month is None:
            month_am = math.ceil(math.log(pay_lc / (pay_lc - i * prin_lc), 1 + i))
            years = month_am // 12
            months_am = month_am % 12
            if months_am == 0:
                print(f"It will take {years} to repay this loan!")
            else:
                print(f"It will take {years} years and {months_am} to repay this loan!")
            overpayment_am = (prin_lc - (month_am * pay_lc))
            print(f'Overpayment {overpayment_am}')
        # To find annuity payment
        else:
            pay_mon = math.ceil((prin_lc * ((i * math.pow((1 + i), month)) / (math.pow((1 + i), month) - 1))))
            overpayment_aa = (prin_lc - (pay_mon * month))
            print(f'Your annunity payment = {pay_mon}')
            print(f'Overpayment = {overpayment_aa}')

