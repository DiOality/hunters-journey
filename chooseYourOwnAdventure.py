name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = ""
q2 = ""
q3 = ""

while True:
    answer = input(
        "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? Type left to go left or right to go right: "
    ).lower()
    if answer == "left":
        break
    if answer == "right":
        break
    continue

# QUESTION 2
while True:
    if answer == "left":
        q2 = input(
            "You come to a river, you can walk around it or swim across? Type walk to walk or swim to swim across: "
        )
    if answer == "right":
        q2 = input(
            "You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back) "
        )

    if q2 == "swim" or q2 == "walk" or q2 == "cross" or q2 == "back":
        break
    continue
# QUESTION 2 OUTCOMES
if q2 == "swim":
    print("You swam across and were eaten by an alligator.")
    exit()
if q2 == "walk":
    print("You walked for many miles, ran out of water and you lost the game.")
    exit()
if q2 == "back":
    print("You go back to the tavern. and die ")
    exit()
    # Cross removed because I want the code to continue to the next line

# QUESTION 3
while True:
    if q2 == "cross":
        q3 = input(
            "You cross the bridge and meet a stranger. Do you talk to them? (yes/no) "
        )
    if q3 == "yes":
        print("You talk to the stranger and they give you gold. YOU WIN!")
        break

    if q3 == "no":
        print("You ignore the stranger and they are offended and they kill you dead")
        break

    continue

print(f"Thank you for playing {name}")
