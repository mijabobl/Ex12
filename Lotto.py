import random

Machine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
Result = set()
name = {"GUINEVERE", "LANCELOT", "SpongeBob", "PENELOPE", "DAVE"}
select = name.pop()
print("Today we are using Machine", select)

print("Let's place the balls in", select, ".....")
print(Machine)
print()
print("Time to draw those big money balls")

play = int(1)
while play < 7:
    Ball = int(Machine.pop(random.randrange(len(Machine))))
    print("Ball", play, "is: ", Ball)
    play = play+1
    Result.add(Ball)
print()
print("Your winning balls are", sorted(Result))
print()
print("Wow, the balls have actually gone!")
print(sorted(Machine))
print()
print("Are you the Rollover Jackpot winner of 1 Billion Pounds?")
print()
print("Goodbye")

