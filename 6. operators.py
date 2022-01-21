# OPERATORS

# Operators are used to perform operations on variables and values.

# Arithmetic operators
Operator 	Name 	            Example
+ 	        Addition 	        x + y
- 	        Subtraction 	    x - y
* 	        Multiplication 	    x * y
/ 	        Division 	        x / y
% 	        Modulus 	        x % y 	# 7 % 2 = 1 (a whole reminder/остаток)
** 	        Exponentiation 	    x ** y 	# 2**3 = 2 to the power of 3, степень
// 	        Floor division 	    x // y  # 7 // 2 = 3 whole number, целое деление

# PYTHON ASSIGNMENT OPERATORS
Operator 	Example 	Same As
= 	        x = 5 	    x = 5
+= 	        x += 3 	    x = x + 3
-= 	        x -= 3 	    x = x - 3
*= 	        x *= 3 	    x = x * 3
/= 	        x /= 3 	    x = x / 3
%= 	        x %= 3 	    x = x % 3    # x = the whole reminder, остаток
//= 	    x //= 3 	x = x // 3   # x = the whole number after devision
**= 	    x **= 3 	x = x ** 3   # x = 5**3 = 100
<<== Don't know these yet, return back to study
&= 	        x &= 3 	    x = x & 3    # returns 1
|= 	        x |= 3 	    x = x | 3
^= 	        x ^= 3 	    x = x ^ 3
>>= 	    x >>= 3 	x = x >> 3
<<= 	    x <<= 3 	x = x << 3

# COMPARISON OPERATORS
Operator 	Name 	                    Example
== 	        Equal 	                    x == y
!= 	        Not equal 	                x != y
> 	        Greater than 	            x > y
< 	        Less than 	                x < y
>= 	        Greater than or equal to 	x >= y
<=          Less than or equal to 	    x <= y

# LOGICAL OPERATOR
Operator 	Description 	                                             Example
and  	    Returns True if both statements are true 	                 x < 5 and  x < 10
or 	        Returns True if one of the statements is true 	             x < 5 or x < 4
not 	    Reverse the result, returns False if the result is true      not(x < 5 and x < 10)

# MEMBERSHIP OPERATORS
Operator 	Description 	                                                                     Example
in  	    Returns True if a sequence with the specified value is present in the object 	     x in y
not in 	    Returns True if a sequence with the specified value is not present in the object 	 x not in y

# BITWISE OPERATORS
Operator 	Name 	                Description
&  	        AND 	                Sets each bit to 1 if both bits are 1
| 	        OR 	                    Sets each bit to 1 if one of two bits is 1
 ^ 	        XOR 	                Sets each bit to 1 if only one of two bits is 1
~  	        NOT 	                Inverts all the bits
<< 	        Zero fill left shift 	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>> 	        Signed right shift 	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off