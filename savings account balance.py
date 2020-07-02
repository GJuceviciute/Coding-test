def balance(openingSum, interestRate, taxFreeLimit, taxRate, numMonths):
    # assumes non-negative openingSum
    cur_balance = openingSum
    for _ in range(numMonths):
        interest = cur_balance * (interestRate / 100)
        tax = 0
        if cur_balance > taxFreeLimit:
            tax = (cur_balance - taxFreeLimit) * (taxRate / 100)
        cur_balance = cur_balance + interest - tax
    return cur_balance
