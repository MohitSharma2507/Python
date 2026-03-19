# Expression execution

# 1.String & Numeric values can operate together with *
A,B=2,3
Txt = "@"
print(A*Txt*B)  #@@@@@@

# 2.String & String can operate together with +

A,B="2",3
Txt = "@"
print((A+Txt)*B)  #2@2@2@

# 3.Numeric values can operate with all arithmetic operators

A,B =2,3
C=4
print(A+B*C)  #14

# 4.Arithmetic expression with integer and float will result in float

A,B =2,3.5
C=A*B
print(C)     #50.0

# 5.Result of division operator with two integer will be float

A,B=1,2
C=A/B
print(C)   #0.5


# 6.Integer division with float and int will give int displayed as float

"""
(floor gives closest integer, which is lesser than or equal to the float value)
#Result of (A//B) is same as floor(A/B)
"""
A,B=1.5,3   
C=A/B
print(C,A/B)   #0.0


# 7.Remainder is negative when denominator is negative

A,B=-5,2
C=A%B
print(C)   #1

A,B=5,2
C=A%B
print(C)   #1

A,B= 5,-2
C=A%B
print(C)   #-1