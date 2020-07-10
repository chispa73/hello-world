#Give correct change in canadian denominations as a cash register with the least number of coins
import decimal

#Value of Canadian denominations
LOONIE = 1
TOONIE = 2
QUARTER = 25
DIME = 10
NICKEL = 5
PENNY = 1

#Ask user to input value of shopping cart
goods_value = decimal.Decimal(input('Please enter the total cost in CAD of goods sold: ')) #used the decimal type
goods_value = goods_value.quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_UP) #specifying the number of decimal places to use

#Ask user to input cash
tendered_cust = decimal.Decimal(input('Please enter the cash given: '))
tendered_cust = tendered_cust.quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_UP)

#Break down between dollars and cents
change = str(tendered_cust - goods_value) #turned to a string
split_num = str(change).split('.') #splitting between the decimal
change_value_dollar = int(split_num[0]) #moving each value into it's own variable of dollars and cents
change_value_cents = int(split_num[1])

#Break down the dollars
toonie_total = int(change_value_dollar / TOONIE)
loonie_total = int(change_value_dollar - (toonie_total * TOONIE) / LOONIE)

#Break down coins starting with quarters
cents_needed = int(change_value_cents) 
quarters_needed = int(cents_needed / QUARTER) 

#dimes
dime_cents_needed = int(cents_needed - (quarters_needed * QUARTER))
dimes_needed = int(dime_cents_needed / DIME) 


#nickels
nickel_cents_needed = int(cents_needed - ((quarters_needed * QUARTER) + (dimes_needed * DIME))) 
nickels_needed = int(nickel_cents_needed / NICKEL)

#pennies
pennies_cents_needed = int(cents_needed - ((quarters_needed * QUARTER) + (dimes_needed * DIME) + (nickels_needed * NICKEL)))
pennies_needed = int(pennies_cents_needed / PENNY)

print(' Change is $%.2f' %(tendered_cust - goods_value))
print(' We need', toonie_total, 'toonies', loonie_total, 'loonies', quarters_needed, 'quarters,', dimes_needed, 'dimes', nickels_needed, 'nickels', pennies_needed, 'pennies!')


