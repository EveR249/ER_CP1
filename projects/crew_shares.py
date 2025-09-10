#ER 2nd Crew Shares

total = int(input("How much was earned in total? "))
crew = int(input("How many crew members are there (not including captain and first mate)? "))

shares = crew + 10 #extra ten are for captain and first mate

money_per_share = total/shares

captain = money_per_share*7

first_mate = money_per_share*3

crew_shares = money_per_share-500

print(f"The captain gets: ${captain:.2f}")
print(f"The First Mate gets: ${first_mate:.2f}")
print(f"The crew still needs: ${crew_shares:.2f}")