#Net Imposable = 0.77*Brut
def get_income():
    while True:
        try:

            income = int(input("Please enter your taxable income: "))
        except ValueError:
            print("Sorry, I didn't understand that please enter taxable income as a number")

            continue
        else:
            break

    return income


def compute_tax(income):
    if income <= 10225:
        tax = 0
    elif income <= 26070: 
        tax = (income - 10225) * 0.11 
    elif income <= 74545:
        tax = (income - 26070) * 0.3 + 1742,84
    elif income <= 169336:
        tax = (income - 74546) * 0.41 + 1742,84 + 14542,5 
    else:
        tax = (income - 160336) * 0.45 + 1742,84 + 14542,5 

    return tax


if __name__ == "__main__":
    income = get_income()
    tax = compute_tax(income)
    print("Votre IR est de" + str(tax) + "€")