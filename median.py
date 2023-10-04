"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def median(numlist):
    numlist.sort()
    if len(numlist) % 2 == 0:
            median = ((numlist[len(numlist)//2])+(numlist[len(numlist)//2-1]))/2
    else:
        odd_average = len(numlist)//2
        median = numlist[odd_average]

    return median

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
        
print(median(numbers))
