
menu = ['Steak','sandwiches','ribs','pork_chops']

#create a dictionary

stock= {'Steak':11,
        'sandwiches': 15,
        'ribs': 13,
        'pork_chops': 45
        }

#create a dictionary for price
price= {'Steak': 20,
        'sandwiches': 60,
        'ribs': 22,
        'pork_chops': 50
        }

total_stock = 0

for item in menu:
    # current item quantity and cost
    quantity = stock[item]
    cost = price[item]
    # updating total stock 
    total_stock = total_stock + quantity * cost
#print the total 
print("R",total_stock)
