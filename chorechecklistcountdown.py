total_chores=4
original_count=total_chores
print("Today you have been given these amount of chores: ",original_count,"\n Lets get started")

completed_chores=0
chore_num=1

while chore_num <= total_chores:
    if chore_num ==1 : next_chore= "make your bed"
    elif chore_num==2: next_chore="Wash the utensils"
    elif chore_num==3: next_chore="Sweep the compound"
    elif chore_num==4: next_chore="Wipe the table"

    answer=input(f"Have you finished: {next_chore}? (yes/no)")

    if answer=="yes":
        completed_chores+=1
        chore_num+=1
        print("Great job ") 
    else:
        print("Please finish your chores")

        print("Chores remaining",total_chores-completed_chores)
    