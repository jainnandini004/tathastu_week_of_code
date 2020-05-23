def duplicate(string):
    dupstring=""
    for x in string:
        if x not in dupstring:
            dupstring+=x
    print("Duplicate character are removed=",dupstring)

s=input("Enter a string from whivh you want to remove duplicate character")
duplicate(s)
