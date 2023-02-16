#import module
from tabulate import tabulate
 
#assign data
mydata=[
    ["Gloria","manager"],
    ["Lidya","secretary"],
    ["Samuel","treasurer"],
    ["Esther","supervisor"],
]

#create header
head=["Name","Ranks"]
#display table
print(tabulate(mydata,headers=head,tablefmt="grid"))
