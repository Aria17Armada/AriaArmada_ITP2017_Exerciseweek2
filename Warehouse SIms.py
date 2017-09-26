warehouse = {}
warehouse = warehouse()
print(warehouse)
def add(x):
    warehouse.append(x)
def remove(x):
    warehouse.pop(x)

answer=str(input("Insert Command: "))
if answer=="add":
    print("What To Add?")
    item=input("Insert Item: ")
    howmany = input("Insert How Much: ")
    warehouse[item]:howmany
    print(warehouse)
elif answer==





