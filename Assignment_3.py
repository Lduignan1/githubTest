NAME = input("Hi, what is your name? ")

cm = int(input("\nWhat is your height in centimetres? "))
F = cm * 0.0328084
I = (F - int(F)) * 12
Q = (I - int(I)) * 4

if (F < 5):
    print("You're still a wee lad")

print("\nDear",NAME.upper(),"you are approximately",F,"feet",I, str(Q) + "/4 inches tall")

input("\nPress the enter key to exit")
