annual_salary=float(input("enter the annual salary"))
housecost=float(input("enter the cost of house"))
portion=float(input("enter the percentage per month to save"))
monthsal=annual_salary/12
downpay=housecost*0.25
monthsav=monthsal*portion
rdownpay=0
months=0
annualrise=0
while(rdownpay<downpay):
    annualrise=rdownpay*(0.04/12)
    rdownpay+=annualrise+monthsav
    months+=1
print(months)