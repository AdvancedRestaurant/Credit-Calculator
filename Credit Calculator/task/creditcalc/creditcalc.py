initial = 0
pay = 0
month = 0


def text():
    credit_principal = 'Credit principal: 1000'
    final_output = 'The credit has been repaid!'
    first_month = 'Month 1: paid out 250'
    second_month = 'Month 2: paid out 250'
    third_month = 'Month 3: paid out 500'

    print(credit_principal)
    print(first_month)
    print(second_month)
    print(third_month)
    print(final_output)


# write your code here
def principal():
    print("Enter the credit principal: ")
    global initial
    initial = int(input())


def months():
    global month
    global initial
    global pay
    print("Enter monthly payment:")
    pay = int(input())

    month = round(initial / pay)

    if month == 1:
        print('It takes ' + str(month) + ' month to repay the credit')
    else:
        print('It takes ' + str(month) + ' months to repay the credit')


def payment():
    global month
    global initial
    global pay
    print("Enter count of months ")
    month = int(input())
    even = initial % month
    pay = round(initial / month)

    last_payment = initial - ((month - 1) * (pay + 1))

    if even == 0:
        print('Your monthly payment = ' + str(pay))
    elif even == 1:
        print("Your monthly payment = " + str(pay + 1) + " with the last payment = " + str(last_payment))


principal()
print('''
What do you want to calculate?
type \"m\" - for counts of months,
type \"p\" - for monthly payments
''')
select = input()
if select == "m":
    months()
elif select == "p":
    payment()



