#Create a file called account and put 1000 coins in it. 
#Read account and use coins to buy goods which as follows
#Pens 4 packs, each pack of 20 pens costs 50coins/pack
#3 Books one for 10 coins and two for 15 coins each
#A bag for 100 coins
#Now add all these goods in to goods file and update the account with remaining balance.
#Show the initial, remaining balance and goods to the output.


account = open('./account','r')
coins = account.read()
account.close()

print('total available coins in account :',coins)

pens_cost = '4 * 50'
books_cost = '10 + 2*15'
bag_cost = '100'

buyed_total = eval(pens_cost) + eval(books_cost) + eval(bag_cost)
remaining = eval(coins) - buyed_total


account = open('./account','w')
account.write(str(remaining))
account.close()

print('total buyed coins of :',buyed_total)
print('remaining coins in account :',remaining)

goods = open('./goods.txt','w')
bill = f'''
Pens : {pens_cost} = {eval(pens_cost)}
Books : {books_cost} = {eval(books_cost)}
Bag : {bag_cost} = {eval(bag_cost)} 
'''
goods.write(bill)
print(bill)


