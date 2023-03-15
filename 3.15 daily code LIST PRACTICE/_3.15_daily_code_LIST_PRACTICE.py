
#Create a list named "colors" and initialize it with five of your favorite colors, like "blue", "teal", and "magenta". Print out the first slot, the middle slot, and the last slot. Then add a sixth color to the list. Finally, print out the whole list. 
colors = ["orange", "green", "teal", "purple", "pastel pink"]
print(colors[0])
print(colors[2])
print(colors[4])
colors.append("Jazzberry Jam")
print(colors)
#Create a list named "paychecks" and initalize it with your four last paycheck amounts (or what you wish your four last paychecks were). Using a for loop and an extra variable you create, find the sum of all the values in the list. 
paychecks = [15,15,15,15]
sum=0
for i in range(4):
    sum += paychecks[i]
    print(sum)
print("total", sum)
#Create an empty list named "foods". Then ask a user for the number of types of foods they want to pack on their trip to Mars. Then, use a for loop to ask a user for a food, and append it to the list. If the user asks for 8 types of food, the for loop should run 8 times. Finally, print the whole list out. 
foods = []
j = int(input("How many types of food do you want to pack for you trip to Mars?"))
for i in range(j):
    print("what is the ", i+1,"th food you want to pack")
    food = input()
    foods.append(food)
print("your list:",foods)