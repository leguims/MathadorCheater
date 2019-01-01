from itertools import permutations#, combinations, combinations_with_replacement
from operator import add, truediv, sub, mul # truediv = float div

#Enonce
numbers=[2, 5, 8, 11, 15]
result=44

#teatments
operations=[add, truediv, sub, mul]
operationsSigns={k.__name__:v for (k,v) in zip(operations, ['+','/','-','x'])}
permutations_numbers=[list(p) for p in permutations(numbers)]
permutations_operations=[list(p) for p in permutations(operations)]
solutions={"Formula {}".format(k):list() for k in range(1,4)}

for (n1, n2, n3, n4, n5) in permutations_numbers:
    for (op1, op2, op3, op4) in permutations_operations:
        # Make it easier to print
        (ops1, ops2, ops3, ops4) = [operationsSigns[op.__name__] for op in (op1, op2, op3, op4)]
        if op4( op3( op2( op1(n1, n2), n3), n4), n5) == result:
            solutionString = "{op1}{op2}{op3}{op4} : [ ( [ ({n1}{op1}{n2}) {op2}{n3} ] {op3}{n4}) {op4}{n5}] = {result}".format(
                op1 = ops1, n1 = n1, n2 = n2,
                op2 = ops2, n3 = n3,
                op3 = ops3, n4 = n4,
                op4 = ops4, n5 = n5,
                result = int(result))
            #print(solutionString)
            solutions["Formula 1"].append(solutionString)
        if op4( op3(op1(n1, n2), op2(n3,n4)), n5) == result:
            solutionString = "{op1}{op3}{op2}{op4} : [ ({n1}{op1}{n2}) {op3} ({n3}{op2}{n4}) ] {op4}{n5} = {result}".format(
                op1 = ops1, n1 = n1, n2 = n2,
                op2 = ops2, n3 = n3, n4 = n4,
                op3 = ops3, 
                op4 = ops4, n5 = n5,
                result = int(result))
            #print(solutionString)
            solutions["Formula 2"].append(solutionString)
        if op4( op2( op1(n1, n2), n3), op3(n4, n5)) == result:
            solutionString = "{op1}{op2}{op4}{op3} : [ ({n1}{op1}{n2}) {op2}{n3} ] {op4} ({n4}{op3}{n5}) = {result}".format(
                op1 = ops1, n1 = n1, n2 = n2,
                op2 = ops2, n3 = n3,
                op3 = ops3, n4 = n4, n5 = n5,
                op4 = ops4,
                result = int(result))
            #print(solutionString)
            solutions["Formula 3"].append(solutionString)

print("Find {} with these numbers : {} and operations {}".format(int(result), [int(n) for n in numbers], operationsSigns.values()))
print("{} possibilies to sort operations and numbers.".format(len(permutations_numbers)*len(permutations_operations)))
print(60*"=")
for (k,v) in solutions.items() :
    print("Found {} solution{} with {}{}".format(len(v),
                                                 "s" if len(v)>1 else "",
                                                 k,
                                                 ":" if len(v)>0 else "."))
    for s in v:
        print("{}{}".format(4*" ", s))
    print(15*"-=-.")
print("End of searching")
raw_input("Press RETURN key to close window.")
