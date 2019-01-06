from itertools import permutations, product, combinations#, combinations_with_replacement
from operator import add, truediv, sub, mul # truediv = float div
from copy import deepcopy
from fractions import Fraction # Use fraction instead of float from truediv

#Enonce
level_unknown=[
    {'result': 44, 'numbers':(2, 5, 8, 11, 15)},
    {'result': 60, 'numbers':(2, 3, 7, 8, 15)},
    {'result': 50, 'numbers':(3, 6, 8, 9, 14)},
    {'result': 42, 'numbers':(3, 4, 5, 7, 9)},
    ]

level_1=[
    {'result': 6, 'numbers':(1, 12, 9, 2, 2)},
    {'result': 6, 'numbers':(4, 9, 3, 8, 2)},
    {'result': 4, 'numbers':(6, 2, 12, 4, 5)},
    {'result': 8, 'numbers':(8, 2, 2, 10, 8)},
    {'result': 6, 'numbers':(1, 2, 9, 12, 2)},
    {'result': 3, 'numbers':(1, 9, 2, 2, 12)},
    ]

level_2=[
    {'result': 18, 'numbers':(9, 1, 2, 11, 4)},
    {'result': 12, 'numbers':(9, 12, 2, 1, 2)},
    {'result': 11, 'numbers':(3, 5, 7, 4, 1)},
    {'result': 10, 'numbers':(7, 9, 6, 14, 1)},
    {'result': 5, 'numbers':(2, 3, 4, 8, 9)},
    {'result': 14, 'numbers':(9, 7, 9, 1, 2)},
    ]

to_solve=level_1[0]

# Score:
#   18 points : All operations are used
#   OR
#   5 points for result
#   1 point for x or + operations
#   2 points for - operation
#   3 points for / operation


#teatments
numbers=to_solve['numbers']
result=to_solve['result']
operations=[add, truediv, sub, mul]
operationsSigns={k.__name__:v for (k,v) in zip(operations, ['+',':','-','x'])}
operationsScore={k.__name__:v for (k,v) in zip(operations, [ 1 , 3 , 2 , 1 ])}
loop_numbers=[list(p) for p in permutations(numbers)]
loop_operations=[list(p) for r in range (1,5) for p in product(operations, repeat=r)]
solutions={}

def get_score(*ops):
    if len(ops) == 4:
        if True not in [a==b for (a,b) in combinations(ops, 2)]:
            return 18
    return sum([5]+[operationsScore[op.__name__] for op in ops])

def save_solution(save, description, *ops):
    # Use score as index in save
    score = get_score(*ops)
    if score not in save:
        save[score]=list()
    if description not in save[score]:
        save[score].append(description)

count=0
for numbers in loop_numbers:
    for operations in loop_operations:
        # Construct loop on priorities instead to code formulas with 'if' instructions
        for priorities in permutations(range(len(operations))): # [0..len()-1]
            count+=1
            # Copy numbers and drop unused numbers
            operations_copy = deepcopy(operations)
            current_result = deepcopy(numbers[0:len(operations)+1])

            # Modify priority to be relative values
            # [3, 2, 1, 0] becomes [3, 2, 1, 0]
            # [0, 3, 2, 1] becomes [0, 2, 1, 0]
            # [3, 0, 2, 1] becomes [3, 0, 1, 0]
            # [0, 1, 2, 3] becomes [0, 0, 0, 0]
            priorities_writable = list(deepcopy(priorities))
            for index in range(len(priorities_writable)):
                priorities_writable = priorities_writable[:index+1] + [p-1 if p>priorities_writable[index] else p for p in priorities_writable[index+1:]]
            
            try:
                solutionString = ""
                for next_operation in priorities_writable:
                    n1 = current_result[next_operation]
                    n2 = current_result[next_operation+1]
                    op = operationsSigns[operations_copy[next_operation].__name__]
                    # Pop 'index=next_operation' + 'index=next_operation+1'
                    r  = operations_copy.pop(next_operation)(current_result.pop(next_operation),current_result.pop(next_operation))
                    if op == operationsSigns['truediv']:
                        r = Fraction(r)
                    if len(solutionString) > 0:
                        solutionString += " ; "
                    solutionString += "{n1}{op}{n2} = {result}".format(
                        n1 = n1 if n1 >= 0 else "({})".format(n1),
                        op = op,
                        n2 = n2 if n2 >= 0 else "({})".format(n2),
                        result = r)
                    current_result.insert(next_operation, r)
                if current_result[0] == result:
                    save_solution(solutions, solutionString, *operations)
            except ZeroDivisionError:
                 pass

line_separator = 15*4*"="

solutions_resume = ""
for (k,v) in solutions.items() :
    if len(solutions_resume) > 0:
        solutions_resume += "\n"
    solutions_resume += """Found {} solution{} with {} point{}.{}""".format(len(v),
                                                 "s" if len(v)>1 else "",
                                                 k,
                                                 "s" if k>1 else "",
                                                 " ==> Mathador <==" if k==18 else "")
solutions_resume += "\n{}".format(line_separator)

resume = """{line_separator}
Find {result} with these numbers : {numbers} and operations {operations}
{count} possibilies to sort operations, numbers and priorities.
Found {solutions} solutions.
{line_separator}""".format(
    result = int(result), numbers = [int(n) for n in numbers], operations = operationsSigns.values(),
    count = count,
    solutions = sum([len(i) for i in solutions.values()]),
    line_separator = line_separator)

print(resume)
print(solutions_resume)
for (k,v) in solutions.items() :
    print("Found {} solution{} with {} point{}:{}".format(len(v),
                                                 "s" if len(v)>1 else "",
                                                 k,
                                                 "s" if k>1 else "",
                                                 " ==> Mathador <==" if k==18 else ""))
    for s in v:
        print("{}{}".format(4*" ", s))
    print(15*"-=-.")
print(resume)
print(solutions_resume)
print("End of searching")
raw_input("Press RETURN key to close window.")
