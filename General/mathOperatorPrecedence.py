'''
Math Operator precedence is as follows:

**        Exponentiation (raise to the power)
~ + -     Ccomplement, unary plus and minus (method names for the last two are +@ and -@)
/ % //    Multiply, divide, modulo and floor division
+ or -    Addition and subtraction
<<        Right and left bitwise shift
&         Bitwise ‘AND’
^ |       Bitwise exclusive OR' and regularOR’
<= < > >= Comparison operators
<> == !=  Equality operators

= %= /= //= -= += = *= Assignment operators
is is not Identity operators
in not in Membership operators
not or and Logical operators

'''


a = 28//4 % 3
print(a)
