def process(list):
    if len(list)==1:
        return list[0]
    elif len(list)==2:
        return max(list[0],list[1])
    elif len(list)==3:
        return max(list[1],list[0]+list[2])
    else:
        return max(list[0]+process(list[2:]),list[1]+process(list[3:]))
list=[int(x) for x in input("The  value present in each houses =").split(",")]
print("The maximum stolen value by the theif =",process(list))
