player1=int(input("Enter the run scored by 1st player on 60 balls"))
player2=int(input("Enter the run scored by 2nd player on 60 balls"))
player3=int(input("Enter the run scored by 3rd player on 60 balls"))
strike_rate1=player1*100/60
strike_rate2=player1*100/60
strike_rate3=player1*100/60
print("strike rate of player1",strike_rate1)
print("strike rate of player2",strike_rate2)
print("strike rate of player3",strike_rate3)

print("Runs score if player1 played 60 more balls",player1*2)
print("Runs score if player2 played 60 more balls",player2*2)
print("Runs score if player3 played 60 more balls",player3*2)

print("Maximum number of sixes player1 could have hit",player1//6)
print("Maximum number of sixes player2 could have hit",player2//6)
print("Maximum number of sixes player3 could have hit",player3//6)
