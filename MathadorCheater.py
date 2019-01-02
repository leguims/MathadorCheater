from itertools import permutations, product, combinations#, combinations_with_replacement
from operator import add, truediv, sub, mul # truediv = float div

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
#.  5 points for result
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
loop_operations=[list(p) for p in product(operations, repeat=4)]
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

for (n1, n2, n3, n4, n5) in loop_numbers:
    for (op1, op2, op3, op4) in loop_operations:
        # Make it easier to print
        (ops1, ops2, ops3, ops4) = [operationsSigns[op.__name__] for op in (op1, op2, op3, op4)]

        # Mathador or 4 operators !
        try:
            if op4( op3( op2( op1(n1, n2), n3), n4), n5) == result:
                solutionString = "{op1}{op2}{op3}{op4} : [ ( [ ({n1}{op1}{n2}) {op2}{n3} ] {op3}{n4}) {op4}{n5}] = {result}".format(
                    op1 = ops1, n1 = n1, n2 = n2,
                    op2 = ops2, n3 = n3,
                    op3 = ops3, n4 = n4,
                    op4 = ops4, n5 = n5,
                    result = result)
                #print(solutionString)
                save_solution(solutions, solutionString, op1, op2, op3, op4)
        except ZeroDivisionError:
            pass
        try:
            if op4( op3(op1(n1, n2), op2(n3,n4)), n5) == result:
                solutionString = "{op1}{op3}{op2}{op4} : [ ({n1}{op1}{n2}) {op3} ({n3}{op2}{n4}) ] {op4}{n5} = {result}".format(
                    op1 = ops1, n1 = n1, n2 = n2,
                    op2 = ops2, n3 = n3, n4 = n4,
                    op3 = ops3, 
                    op4 = ops4, n5 = n5,
                    result = result)
                #print(solutionString)
                save_solution(solutions, solutionString, op1, op2, op3, op4)
        except ZeroDivisionError:
            pass
        try:
            if op4( op2( op1(n1, n2), n3), op3(n4, n5)) == result:
                solutionString = "{op1}{op2}{op4}{op3} : [ ({n1}{op1}{n2}) {op2}{n3} ] {op4} ({n4}{op3}{n5}) = {result}".format(
                    op1 = ops1, n1 = n1, n2 = n2,
                    op2 = ops2, n3 = n3,
                    op3 = ops3, n4 = n4, n5 = n5,
                    op4 = ops4,
                    result = result)
                #print(solutionString)
                save_solution(solutions, solutionString, op1, op2, op3, op4)
        except ZeroDivisionError:
            pass

        # Less than 4 operators
        try:
            if op3( op2( op1(n1, n2), n3), n4) == result:
                solutionString = "{op1}{op2}{op3} : [ ({n1}{op1}{n2}) {op2}{n3} ] {op3}{n4} = {result}".format(
                    op1 = ops1, n1 = n1, n2 = n2,
                    op2 = ops2, n3 = n3,
                    op3 = ops3, n4 = n4,
                    result = result)
                #print(solutionString)
                save_solution(solutions, solutionString, op1, op2, op3)
        except ZeroDivisionError:
            pass
        try:
            if op3( op1(n1, n2), op2(n3, n4) ) == result:
                solutionString = "{op1}{op3}{op2} : ({n1}{op1}{n2}) {op3} ({n3}{op2}{n4}) = {result}".format(
                    op1 = ops1, n1 = n1, n2 = n2,
                    op2 = ops2, n3 = n3,
                    op3 = ops3, n4 = n4,
                    result = result)
                #print(solutionString)
                save_solution(solutions, solutionString, op1, op2, op3)
        except ZeroDivisionError:
            pass
        try:
            if op2( op1(n1, n2), n3) == result:
                solutionString = "{op1}{op2} : ({n1}{op1}{n2}) {op2}{n3} = {result}".format(
                    op1 = ops1, n1 = n1, n2 = n2,
                    op2 = ops2, n3 = n3,
                    result = result)
                #print(solutionString)
                save_solution(solutions, solutionString, op1, op2)
        except ZeroDivisionError:
            pass
        try:
            if op1(n1, n2) == result:
                solutionString = "{op1} : ({n1}{op1}{n2}) = {result}".format(
                    op1 = ops1, n1 = n1, n2 = n2,
                    result = result)
                #print(solutionString)
                save_solution(solutions, solutionString, op1)
        except ZeroDivisionError:
            pass

print("Find {} with these numbers : {} and operations {}".format(int(result), [int(n) for n in numbers], operationsSigns.values()))
print("{} possibilies to sort operations and numbers.".format(len(loop_numbers)*len(loop_operations)))
print("Found {} solutions below.".format( sum([len(i) for i in solutions.values()]) ))
print(15*4*"=")
for (k,v) in solutions.items() :
    print("Found {} solution{} with {} point{}:{}".format(len(v),
                                                 "s" if len(v)>1 else "",
                                                 k,
                                                 "s" if k>1 else "",
                                                 " ==> Mathador <==" if k==18 else ""))
    for s in v:
        print("{}{}".format(4*" ", s))
    print(15*"-=-.")
print("End of searching")
raw_input("Press RETURN key to close window.")
