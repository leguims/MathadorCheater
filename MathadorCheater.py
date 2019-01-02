from itertools import permutations, product, combinations#, combinations_with_replacement
from operator import add, truediv, sub, mul # truediv = float div

#Enonce
##numbers=[2, 5, 8, 11, 15]
##result=44

##numbers=[2, 3, 7, 8, 15]
##result=60

numbers=[3, 6, 8, 9, 14]
result=50

##numbers=[3, 4, 5, 7, 9, ]
##result=42

# Score:
#   18 points : All operations are used
#   OR
#   1 point for x or + operations
#   2 points for - operation
#   3 points for / operation


#teatments
operations=[add, truediv, sub, mul]
operationsSigns={k.__name__:v for (k,v) in zip(operations, ['+',':','-','x'])}
operationsScore={k.__name__:v for (k,v) in zip(operations, [ 1 , 3 , 2 , 1 ])}
loop_numbers=[list(p) for p in permutations(numbers)]
loop_operations=[list(p) for p in product(operations, repeat=4)]
solutions={"{}".format(k):list() for k in ['Mathador {}'.format(m) for m in range(1,4)]+['Other {}'.format(o) for o in range(1,8)]}

for (n1, n2, n3, n4, n5) in loop_numbers:
    for (op1, op2, op3, op4) in loop_operations:
        # Make it easier to print
        (ops1, ops2, ops3, ops4) = [operationsSigns[op.__name__] for op in (op1, op2, op3, op4)]
        (op1_score, op2_score, op3_score, op4_score) = [operationsScore[op.__name__] for op in (op1, op2, op3, op4)]
        # Todo : Define if mathador or not ! if op1, op2, op3, op4)
        if True in [a==b for (a,b) in combinations((op1, op2, op3, op4),2)]:
            mathador = False
        else:
            mathador = True
            
        if mathador:
            solution_key = "Mathador "
            score = 18
        else:
            solution_key = "Other "
            score = sum([op1_score, op2_score, op3_score, op4_score])

        # Mathador !
        if op4( op3( op2( op1(n1, n2), n3), n4), n5) == result:
            solutionString = "{op1}{op2}{op3}{op4} : [ ( [ ({n1}{op1}{n2}) {op2}{n3} ] {op3}{n4}) {op4}{n5}] = {result} => {score} pts".format(
                op1 = ops1, n1 = n1, n2 = n2,
                op2 = ops2, n3 = n3,
                op3 = ops3, n4 = n4,
                op4 = ops4, n5 = n5,
                result = int(result),
                score = score)
            #print(solutionString)
            solutions[solution_key+"1"].append(solutionString)
        if op4( op3(op1(n1, n2), op2(n3,n4)), n5) == result:
            solutionString = "{op1}{op3}{op2}{op4} : [ ({n1}{op1}{n2}) {op3} ({n3}{op2}{n4}) ] {op4}{n5} = {result} => {score} pts".format(
                op1 = ops1, n1 = n1, n2 = n2,
                op2 = ops2, n3 = n3, n4 = n4,
                op3 = ops3, 
                op4 = ops4, n5 = n5,
                result = int(result),
                score = score)
            #print(solutionString)
            solutions[solution_key+"2"].append(solutionString)
        if op4( op2( op1(n1, n2), n3), op3(n4, n5)) == result:
            solutionString = "{op1}{op2}{op4}{op3} : [ ({n1}{op1}{n2}) {op2}{n3} ] {op4} ({n4}{op3}{n5}) = {result} => {score} pts".format(
                op1 = ops1, n1 = n1, n2 = n2,
                op2 = ops2, n3 = n3,
                op3 = ops3, n4 = n4, n5 = n5,
                op4 = ops4,
                result = int(result),
                score = score)
            #print(solutionString)
            solutions[solution_key+"3"].append(solutionString)

        # Others
        if op3( op2( op1(n1, n2), n3), n4) == result:
            score = sum([op1_score, op2_score, op3_score])
            solutionString = "{op1}{op2}{op3} : [ ({n1}{op1}{n2}) {op2}{n3} ] {op3}{n4} = {result} => {score} pts".format(
                op1 = ops1, n1 = n1, n2 = n2,
                op2 = ops2, n3 = n3,
                op3 = ops3, n4 = n4,
                result = int(result),
                score = score)
            #print(solutionString)
            if solutionString not in solutions["Other 4"]:
                solutions["Other 4"].append(solutionString)
        if op3( op1(n1, n2), op2(n3, n4) ) == result:
            score = sum([op1_score, op2_score, op3_score])
            solutionString = "{op1}{op3}{op2} : ({n1}{op1}{n2}) {op3} ({n3}{op2}{n4}) = {result} => {score} pts".format(
                op1 = ops1, n1 = n1, n2 = n2,
                op2 = ops2, n3 = n3,
                op3 = ops3, n4 = n4,
                result = int(result),
                score = score)
            #print(solutionString)
            if solutionString not in solutions["Other 5"]:
                solutions["Other 5"].append(solutionString)
        if op2( op1(n1, n2), n3) == result:
            score = sum([op1_score, op2_score])
            solutionString = "{op1}{op2} : ({n1}{op1}{n2}) {op2}{n3} = {result} => {score} pts".format(
                op1 = ops1, n1 = n1, n2 = n2,
                op2 = ops2, n3 = n3,
                result = int(result),
                score = score)
            #print(solutionString)
            if solutionString not in solutions["Other 6"]:
                solutions["Other 6"].append(solutionString)
        if op1(n1, n2) == result:
            score = sum([op1_score])
            solutionString = "{op1} : ({n1}{op1}{n2}) = {result} => {score} pts".format(
                op1 = ops1, n1 = n1, n2 = n2,
                result = int(result),
                score = score)
            #print(solutionString)
            if solutionString not in solutions["Other 7"]:
                solutions["Other 7"].append(solutionString)

print("Find {} with these numbers : {} and operations {}".format(int(result), [int(n) for n in numbers], operationsSigns.values()))
print("{} possibilies to sort operations and numbers.".format(len(loop_numbers)*len(loop_operations)))
print("Found {} solutions below.".format( sum([len(i) for i in solutions.values()]) ))
print(15*4*"=")
for (k,v) in solutions.items() :
    print("Found {} solution{} with {}{}".format(len(v),
                                                 "s" if len(v)>1 else "",
                                                 k,
                                                 ":" if len(v)>0 else "."))
    for s in v:
        print("{}{}".format(4*" ", s))
    print(15*"-=-.")
print("End of searching")
#raw_input("Press RETURN key to close window.")
