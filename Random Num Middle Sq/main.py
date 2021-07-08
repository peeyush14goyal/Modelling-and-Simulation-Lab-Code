#-----------------------------------------Code starts from here-----------------------------------------------------------------------
value=input("Enter the seed: ")

x=[1, 10, 100, 1000, 10000, 100000]
middle_value = 0
i=1

while len(x)==len(set(x)):
    value=int(value)
    r=value
    value=value*value
    print("x%s = %s*%s = %s"%(i,r,r,value))
    value=str(value)
    if len(value)==3:
        middle_value=value[0:-1]
    elif len(value)==2:
        middle_value=value[0:-1]
    elif len(value)==1:
        middle_value=0
    elif len(value)==4:
        middle_value=value[1:-1]
    value=middle_value
    x.append(value)

    print("Next seed = %s"%middle_value)
    i=i+1

if len(x)!=len(set(x)):
    print("Repeating random numbers. Process halted.")
