#"Taylor is a UH student and makes $1,000 per month from working at Starbucks. Taylor has been offered a salary raise, which can be chosen from the following two options: Plan 1: $50 salary increase every three months Plan 2: A salary increase of 1.5% every month" 
# Write a program to help Taylor make a decision.


s = 1000
m = int(input("Enter total number of month Taylor going to work in UH:"))

p1 = s

for i in range(1, m+1):
    if i % 3 == 0:
        p1 = p1 + 50

p2 = s

for i in range(1, m+1):
    inc = p2 * 0.015
    p2 = p2 + inc


print("Plan 1 final:", round(p1,2))
print("Plan 2 final:", round(p2,2))

if p1 > p2:
    print("Plan 1 is better")
elif p2 > p1:
    print("Plan 2 is better")
else:
    print("Both are same")
