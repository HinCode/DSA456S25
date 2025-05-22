
# Write the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: Wang Hin Chan
# Student Number: 149900227
#


def wins_rock_scissors_paper(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()

    if p1 == p2:
        return False
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "paper" and p2 == "rock") or \
         (p1 == "scissors" and p2 == "paper"):
        return True
    else:
        return False


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result



def fibonacci(n):

    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)



def sum_to_goal(nums, goal):
    seen = set()
    for num in nums:
        diff = goal - num
        if diff in seen:
            return num * diff
        seen.add(num)
    return 0

    

class UpCounter:
    def __init__(self, step=1):
        self.value = 0
        self.step = step

    def count(self):
        return self.value

    def update(self):
        self.value += self.step



class DownCounter(UpCounter):
    def update(self):
        self.value -= self.step
