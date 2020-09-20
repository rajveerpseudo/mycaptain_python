import random
import time
comp_input=['stone','paper','scissor']
c=0
u=0
print("Enter stone, paper or scissor")
time.sleep(2)
rounds=int(input("Enter no. of rounds you want to play? "))
time.sleep(1)
for i in range(rounds):
    comp_choice=random.choice(comp_input)
    user_choice=input("Enter your Choice: ")
    if (comp_choice== 'stone' and user_choice== 'scissor'):
        print("Comp chose: {}".format(comp_choice))
        print("Comp scores")
        c = c + 1
        print("Computer: {} You: {}".format(c,u))
        time.sleep(2)
    elif (comp_choice=='paper' and user_choice=='stone'):
        print("Comp chose: {}".format(comp_choice))
        print("Comp scores")
        c = c + 1
        print("Computer: {} You: {}".format(c, u))
        time.sleep(2)
    elif (comp_choice=='scissor' and user_choice=='paper'):
        print("Comp chose: {}".format(comp_choice))
        print("Comp scores")
        c = c + 1
        print("Computer: {} You: {}".format(c, u))
        time.sleep(2)
    elif(comp_choice==user_choice):
        print("Comp chose: {}".format(comp_choice))
        print("Draw")
        print("Computer: {} You: {}".format(c, u))
        time.sleep(2)
    else:
        print("Comp chose: {}".format(comp_choice))
        print("You score")
        u=u+1
        print("Computer: {} You: {}".format(c, u))
        time.sleep(2)
