def mindel(string,l,h):
    if l>h:
        return 10
    if l==h:#same character
        return 0
    if l==h-1:#only two character present
        if string[l]==string[h]:
            return 0
        else:
            return 1
    if string[l]==string[h]:
        return mindel(string,l+1,h-1)
    else:
        return(min(mindel(string,l,h-1),mindel(string,l+1,h))+1)




string=input("Enter the string")
print("Number of character to delete  to make the string palindrome",mindel(string,0,len(string)-1))
