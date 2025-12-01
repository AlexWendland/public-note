---
aliases: []
checked: false
created: 2023-04-20
draft: false
last_edited: 2023-11-11
tags:
  - programming
type: representations
---
# Two's complement

This is a way to represent [[Signed or unsigned integers|signed integers]]. Assuming the left most digit is the most significant [[bit]] then:

sign digit | numerical representation.

So assume you store your signed integer as a [[Byte|byte]] then left most [[Bit|bit]] would be for the sign and the other 7 [[Bit|bits]] would be for the number.

## Positive numbers

For example when representing 10 in 7 bits you would use

$$
000\ 1010 = 0*2^7 + 0*2^6 + 0*2^5 + 0*2^4 + 1*2^3 + 0*2^2 + 1*2^1 + 0*2^0
$$

therefore as 10 is positive it's full representation would be

0|000 1010

with the 0 representing positive numbers.

## Negative numbers

This is where stuff gets freaky - lets first start with the formula and go backwards to explain why this works.

Lets say we want to represent -10:

1. Start with the representation of the absolute value of number in binary e.g. 10 = 0000 1010
2. Flip all the digits e.g. 1111 0101
3. Add 1 to the representation and ignore overflow (this is pretty key as $-2^7$ is a legit option) e.g. 1111 0110

Ok great, so it has the left most digit being 1 (so not positive) and this seems to be unique. This might take a bit more maths but we actually use all the 'space' we have in the [[Byte|byte]]. 0111 1111 is $2^7 - 1$, 0000 0000 is $0$, 1000 0000 is -$2^7$ and 1111 1111 is $-1$.

Lets just cover how to go decimalise a binary representation of a negative number as well suppose we wanted to convert 1100 1100:

1. First subtract 1 from the expression (or add -1 but we will come back to that) e.g. 1100 1011.
2. Flip all the digits e.g. 0011 0100.
3. Convert the binary number into decimal representation and put a negative sign on it e.g. 32 + 16 + 4 = 52, so the number is -52.

That seems easy enough but there has to be simpler way to do this right?

## Addition

You add two numbers just as you would [[Signed or unsigned integers|unsigned integers]] by starting from the least significant [[Bit|bit]] (right most in our example) and carry the overflows forward. This works even when adding two negatives or a negative with a positive!

### Two positive

Lets add 10 = 0000 1010 with 12 = 0000 1100

$$
\begin{align*}
10 + 12 & = 0000\ 1010\\
& + 0000\ 1100\\
& = 0001\ 0110\\
& = 16 + 4 + 2\\
& = 22.
\end{align*}
$$
### Negative with a positive

Lets add -5 = 1111 1011 with 10 = 0000 1010

$$
\begin{align*}
-5 + 10 & = 1111\ 1011 \\
& + 0000\ 1010\\
& = 0000\ 0101\\
& = 4 + 1\\
& = 5.
\end{align*}
$$
### Two negative

Lets add -5 = 1111 1011 with -16 = 1111 0000

$$
\begin{align*}
-5 + 10 & = 1111\ 1011 \\
& + 1111\ 0000\\
& = 1110\ 1011\\
& = (-)\ 0001\ 0101\\
& = (-)\ 16 + 4 + 1\\
& = -21.
\end{align*}
$$

> [!Note] Over flow detection
> You can use the sign digit to detect overflow i.e. if you add two positive numbers the outcome should be positive!

## Comparison

This essentially works the same as unsigned integers starting from the most significant [[Bit|bit]] work your way to the least until you see a difference. Which ever is 1 in the different place is larger.

The only exclusion to this is if the signed [[Bit|bits]] of the two numbers are different. Then the positive number is larger!

## Conclusion

This does seem like a pretty good method to encode negative numbers ... you don't need to add in much additional logic on top of unsigned integers.
