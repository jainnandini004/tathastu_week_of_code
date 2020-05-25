from numpy import*
def sort1(vote,maxvalue):
    list=[key for (key,values) in vote.items() if values==maxvalue]
    z=sorted(list)
    for key in z:
        print(key)
n=[i for i in input("Enter the candidates name").split(",")]
vote={}
for i in n:
    vote.update({i:n.count(i)})

maxvalue=max(vote.values())
sort1(vote,maxvalue)
