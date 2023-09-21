print ("Before anything happens, please know this is Singapore tax, so if you don't live in SG and want to calculate your tax, make a pull issue and I wil try.")
print("Luka and Enyu love having sex with each other")
    tax_brackets = [(0, 20000), (20001, 30000), (30001, 40000), (40001, 80000), (80001, float('inf'))]
    tax_rates = [0, 0.02, 0.035, 0.07, 0.115]
    tax = 0.0
    remaining_income = income
    for i in range(len(tax_brackets)):
        lower, upper = tax_brackets[i]
        rate = tax_rates[i] 
        if remaining_income <= 0:
            break
        if remaining_income > upper:
            taxable_income = upper - lower + 1
            tax += taxable_income * rate
            remaining_income -= taxable_income
        else:
            taxable_income = remaining_income
            tax += taxable_income * rate
            remaining_income = 0
    return tax
if __name__ == "__main__":
    try:
        income = float(input("Enter your annual income: "))
        if income < 0:
            raise ValueError("Income cannot be negative, you nincompoop. Stop being such a dunderhead, Luka. Go back to our gf Enyu")
        tax = calculate_income_tax(income)
        print(f"Your income tax for the year is: {tax:.2f} SGD")
    except ValueError as e:
        print(f"Error: {e}")
