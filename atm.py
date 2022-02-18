data =[["Tejo","1234",100000],
         ["Vidya mam","12345",100000000],
           ["Aaru","1111",10000000]]
def cashWithdrawl(id):
    amount = int(input("Enter the amount for withdrawl"))
    for i in data:
        if i[1] == id:
            currentbalance = i[2] - amount
            print(i[0]+" your balance is: " + str(amount))

def cashDeposit(id):
    amount2 = input("Enter your amount")
    for i in data:
        if i[1] == id:
            currentbalance2 = i[2] + amount2
            print(i[0]+" your balance is: " + str(amount2))
            
def balanceEnquiry(id):
    print("Balance Enquyiry")
    for i in data:
        if i[1] == id:
            print(i[0]+" your balance is: " + str(i[2]))

id = input("Enter your id")

print("Press 1 for cashwithdrawl")
print("Press 2 for cashDeposit")
print("Press 3 for balanceEnquiry")

input = int(input("Enter your choice"))
if input == 1:
    cashWithdrawl(id)
elif input == 2:
    cashDeposit(id)
else:
    balanceEnquiry(id)