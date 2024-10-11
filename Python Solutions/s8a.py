tuple = (4,14,20,8,9,5,4)
newtuple = ()

for n in tuple:
    if n in newtuple:
        print(f"Repeated Item: {n}")
    else:
        newtuple += (n,)
    
if len(newtuple) == 0:
    print("No Repeated Items")