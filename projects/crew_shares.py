#ER 2nd Crew Shares

#The captain didn't have time to divvy up money before releasing everyone to port. He gave each member of the crew 500 dollars for the evening but needs to divide it properly. The captain of the crew gets 7 shares (equal portions of the treasure) The first mate gets 3 shares, each member of the crew then gets 1 share but the crew members have all already received $500.

total = float(input("How much was earned in total? "))
crew = int(input("How many crew members are there (not including captain and first mate)? "))

shares = crew + 10 #extra 10 are for captain and first mate

money_per_share = total/shares 

captain = money_per_share*7 #Captain gets 7 shares

first_mate = money_per_share*3 #First mate gets 3 shares

crew_shares = money_per_share-500 #You already gave each crew member $500 so you need to subtract that so you know the rest of what they need

print(f"The captain gets: ${captain:.2f}")
print(f"The first mate gets: ${first_mate:.2f}")
print(f"The crew still needs: ${crew_shares:.2f}")