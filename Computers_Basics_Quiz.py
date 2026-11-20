#Computers_Basic_Quiz.py
#Varibles #Do not mess with this line
Name = input("Enter your name: ").strip()
Score = 0
InvalidInputs = 0 
#Welcome Message
print(f"Welcome to the Computers Basics Quiz {Name}")
#ActualTest
#Test1
print(f"{Name}, what is the command to show the windows version in Run?")
print("A) ShowWindowsVersion")
print('B) print(f"Your windows version is: {WindowsVersion}")')
print("C) Winver")
print("D) SHOW ME MY WINDOWS VERSION NOW")
Answer1 = input("Enter your answer (A|B|C|D): ").strip().upper()
if Answer1 == "C":
    print(f"{Name}, you are correct 🥳")
    Score += 1
elif Answer1 in ["A","B"]:
    print(f"{Name}, unfortanatly, you are incorrect 😒")
    print("The correct answer is C")
    Score -= 1
elif Answer1 == "D":
    print("You dont need to demand your windows version lol")
    print("You are incorrect 👎🏻")
    print("The correct answer is C")
    Score -= 1
else:
    print("Invallid input!")
    InvalidInputs += 1
    print(f"{Name}, you now have {InvalidInputs} invalid inputs.")
#Test2
print(f"{Name}, what is the command to show text in PowerShell?")
print('A) print("Hello, world")')
print('B) echo "Hello, world"')
print('C) show "Hello, world!"')
print('D) display "Hello, world"')
Answer2 = input("Enter your answer (A | B | C | D): ").strip().upper()
if Answer2 == "B" and Score == 1:
    print(f"{Name}, once again, you are correct 😊!")
    Score += 1
elif Answer2 == "B":
    print(f"{Name}, you are correct 😀!")
    Score += 1
elif Answer2 in ["C", "D"]:
    print(f"Oh no! You are incorrect {Name}")
    print("The correct answer was B")
elif Answer2 == "A":
    print(f";-; {Name}, PowerShell is not Python.")
    print("The correct answer is C")
    Score -= 1
else:
    print("Invallid input!")
    InvalidInputs += 1
#Test3
print("Guys im going crazy")
print("How do you restart your router?")
print("A) Unplug & Replug (or reset if you have the button)")
print("B) Wait 999 years for it to load")
print("C) Yell at the router until it loads")
print("D) Put a satalite and a cell tower next to your house")
Answer3 = input("Enter your answer (A|B|C|D): ").strip().upper()
if Answer3 == "A":
    print(f"{Name}, after all that crazyness, you are correct! ")
    Score += 1
elif Answer3 == "B":
    print("Uhh, see you in 999 years I guess.")
    print("(Oh yeah I didn't tell you, this still removes a point)") 
    print("The correct answer is B")
    Score -= 1
elif Answer3 == "C":
    print(f"{Name}, we've all tried that before,")
    print("it doesn't work.")
    print("(Oh yeah I didn't tell you, this still removes a point)")
    print("The correct answer is B")
    Score -= 1
elif Answer3 == "D":
    print("I'm preety sure you cant do that..")
    print("(Oh yeah I didn't tell you, this still removes a point)")
    print("The correct answer is B")
    Score -= 1
else:
    print("Why did you give a invallid input on the crazyist question so far 😭")
    InvalidInputs += 1
#Test4
print("Whats the run command to open the applocations folder?")
print("A) OPEN MY APPS FOLDER NOW!")
print("B) appsfolder")
print("C) applocationsfolder")
print("D) shell:appsfolder")
Answer4 = input("Enter your answer (A | B | C | D): ").strip().upper()
if Answer4 == "D":
    print(f"{Name}, you are correct, thank you for not choosing the crazyist answer on the list.")
    Score += 1
elif Answer4 == "A":
    print("OK OK CALM DOWN! You got 1 score removed.")
    print("The correct answer is D")
    Score -= 1
elif Answer4 == "B":
    print(f"Sorry {Name}, you forgot the shell in that command.")
    print("The correct answer is D")
elif Answer4 == "C":
    print(f"{Name}, you are incorrect, ")
    print("you forgot the shell: and you need to shorten it.")
    print("The correct answer is D")
    Score -= 1
else:
    print("Why do you need to put an invalid input?")
    InvalidInputs += 1
#Final score
if Score == 4:
    print(f"Congrats {Name}, you got a perfect 100%!")
elif Score == 3:
    print(f'{Name}, you got a 75%!')
elif Score == 2:
    print(f"{Name}, you got a 50%")
elif Score == 1:
    print(f"{Name}, nooo, you got a 25%")
elif Score == 0:
    print(f"{Name}, unfortanatly, you got a 0%")
else:
    print(f"... {Name}, im sorry to say, you got a negitive score.")
#Invallid inputs
print(f"{Name}, you made {InvalidInputs} invallid inputs.")
