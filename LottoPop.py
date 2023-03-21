print("Welcome to the Lotto!")
name = {"GUINEVERE", "LANCELOT", "PENELOPE", "DAVE"}
select = name.pop()
print("Today we are using Machine", select)
print("Let's place the balls in", select, ".....")

machine = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
           "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
           "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
           "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
           "41", "42", "43", "44", "45", "46", "47", "48", "49", "50"}

#print(machine)
result = set()
play = int(1)

print()
print("Time to draw those big money balls")
#loop 6 times through the machine and 'pop' a random ball from the machine
while play < 7:
    x = int(machine.pop())
    result.add(x)
    print("Ball", play, "Is: ", x)
    play = play + 1
print()
print("Tonight's BIG Money Balls ARE!!!>>>", sorted(result))
print()

print("Lets check these balls have been removed from the machine")
#convert set from string to integer
machine2 = set(map(int, machine))
print(sorted(machine2))
print()
print("Thanks for playing my game")




