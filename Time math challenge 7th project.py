import random
import time

OPERATORS = ["+","-","*"]
MIN_OPERAND = 4
MAX_OPERAND = 15
TOTAL_PROBLEM = 5

def generate_pro():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operators = random.choice(OPERATORS)

    expr = str(left) + " " + operators + " " + str(right)
    answer = eval(expr)
    #print(expr)
    return expr, answer

#expr, answer = generate_pro()
#print(expr, answer)
wrong = 0
input("Click enter to begin🐱‍🏍")
print("------------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEM):
    expr, answer = generate_pro()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
            wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("------------------------------")
print("Nice One! You finished your calculation in  ", total_time, "seconds⌛")