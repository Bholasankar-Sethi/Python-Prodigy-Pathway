a, b = 2, "5"   # int, string data type cannot add directly
c = int(b)      # manually converted string to integer
print(type(c))
sum = a + c
print(sum)    #integer out put



x, y = 6, 4.38   # integer to float
z = float(x)
print(z)
print(type(z))
print(y + z)



# name = " Sritam"     # String to float
# c = float(name)
# print(type(c))
# print(y + c)    # Not possible


p, q = "Sri", 5   # number to string
r = str(q)
sub = p + r
print(sub)
print(type(p))