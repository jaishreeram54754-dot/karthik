annual_salary=int(input("enter the annual salary"))
portion_saved=float(input("enter the save percentage amount of salary for house in (decimals)"))
housecost=float(input("enter the house cost"))
annualincrease=float(input("enter the semi annual increase 6months increase"))
monthlysalary=annual_salary/12
monthsave=monthlysalary*portion_saved
downpayment=housecost*0.25
rdownpayment=0
months=0
annualrise=0
semiris=0
flag=0
while(rdownpayment<downpayment):
    annualrise=rdownpayment*0.04/12
    rdownpayment+=annualrise+monthsave
    months+=1
    if(months%6==0):
        semiris=annual_salary*annualincrease
        annual_salary=semiris+annual_salary
        monthlysalary=annual_salary/12
        monthsave=monthlysalary*portion_saved
print(months)

