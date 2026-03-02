print(not True)
print(not False)

a, b = 23, 38
print(not(a < b))   # a < b = True , not True = False
c = print(a < b)    # a < b = True
print(c)            # nothing store is store in variable so None


val1 = True
val2 = False
print("And operator ", val1 and val2) # True when both value true

print("Or operator: ", val1 or val2)  # True when atleast 1 val True

"""Three logical operator:-
Not > And > Or
arithmatic precedence order """


a, b = 25, 38
print((a == b) or (a < 38))  # a == b False or a < b True --> True