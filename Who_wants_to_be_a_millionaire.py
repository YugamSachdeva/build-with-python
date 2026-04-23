questions = [
["Who is Warren Buffett?", "Plumber", "Engineer", "Investor", "Carpenter", 3],
["What does CPU stand for?", "Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Control Processing Unit", 2],
["Which language is used for web development?", "Python", "HTML", "C++", "Java", 2],
["What is 2 + 2?", "3", "4", "5", "6", 2],
["Which company created Windows?", "Apple", "Google", "Microsoft", "Amazon", 3],
["Which planet is known as Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
["What is the capital of India?", "Mumbai", "Delhi", "Kolkata", "Chennai", 2],
["Which data structure uses FIFO?", "Stack", "Queue", "Tree", "Graph", 2],
["Which symbol is used for comments in Python?", "//", "#", "/* */", "--", 2],
["Who is the CEO of Tesla (2025)?", "Jeff Bezos", "Elon Musk", "Bill Gates", "Mark Zuckerberg", 2]
]

price=[10,50,100,1000,10000,50000,100000,350000,500000,1000000]
won=0


print("--------------------------------")
print("You Can Be the Next Millionaire!")
print("--------------------------------")
for i in range(len(questions)):
    q=questions[i]
    print("This question is for $",price[i])
    print(q[0])
    print(f"1.{q[1]}")
    print(f"2.{q[2]}")
    print(f"3.{q[3]}")
    print(f"4.{q[4]}")

    a=int(input("Enter the correct option:"))   
    if(a!=q[5]):
        print("This is wrong answer.\nYou Lost!")
        print("You won:$",won)
        break
    else:
        won=price[i]
        print("Your ans is correct.")
        print("Total Won Balance:",won)
        print(" ")
        print("--Next question is--")    

        
    