# Python katas
Short exercises in Python. Mostly FizzBuzz level, although some are more interesting (e.g. `Pi`, `Genomic range query`, `Passing cars`, `Max counter`).

## Miscellaneous
Problems from various sources, mostly from this [excellent repo](https://github.com/karan/Projects).

#### Pi
Calculate the first `n` digits of π using a spigot algorithm (Rabinowitz, Wagon, 1995). 

#### Asterisk triangle
Print some simple figures.

## Codility
Training exercises from [Codility](https://www.codility.com). Probably correct, at least according to the autograder (all score 100%).

#### Array rotation
Given a non-empty array `A` consisting of `N` integers, return the array shifted to the right by `K` indices.

#### Binary gap
Find the longest sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of an integer `N`.

#### Count div
Compute the number of integers divisible by `k` in range `[a, b]`.

#### Distinct pythonic
Calculate the number of distinct values in an array `A` using a pythonic one-liner.

#### Distinct unpythonic
Calculate the number of distinct values in an array `A`. Probably the expected solution (the exercise is meant to use sorting).

#### Frog jump
A mathematically inclined frog is located at position `X` and wants to get to a position greater than or equal to `Y`. The frog always jumps a fixed distance `D`. Return the minimal number of jumps that the frog must perform to reach its target.

#### Genomic range query
A DNA sequence is represented as a string consisting of the letters A, C, G, T, corresponding to the types of successive nucleotides in the sequence. Nucleotides A, C, G, and T have impact factors of 1, 2, 3, and4, respectively. Given a non-empty string `S` representing the DNA sequence and two non-empty arrays P and Q, each consisting of M integers, return an array of M integers representing the minimal factor between position `P[K]` and `Q[K]`.  

#### Max counter
Given N counters and a non empty array `A` of `M` integers representing a sequence of operations:
* if `A[K]=X` such that `1 <= X <= N`, increment counter `X`
* if `A[K]=N+1`, set all counters to the value of the maximal counter

calculate the value of every counter after all operations.

#### Max profit
An array `A` contains daily prices of a stock share for a period of `N` consecutive days. Return the maximal profit from a transaction that can be obtained by buying a single share on day `P` and selling it on day `Q` (where `0 <= P <= Q < N`, duh). Return 0 if it is impossible to make any money.

#### Min perimeter rectangle
Find the minimal perimeter of a rectangle whose area equals `N`. Assume that the lengths of sides are integers.

#### Odd occurences in array
Find the only element of a non-empty array `A` of `N` integers that occurs odd number of times.

#### Passing cars
A non-empty array `A` represents consecutive cars on a road:
* 0 represents a car travelling east
* 1 represents a car travelling west

Return the number of pairs of passing cars. Return -1 if it's really big.

#### Permutation missing element
Find the missing element in a given permutation.

#### String symmetry point
Given a string `S`, return the index of a character such that the part of the string to the left of that character is a reversal of the part of the string to its right. Return `-1` if no such index exists.

#### Tape equilibrium
Find an integer `P` that splits a non-empty array `A` into two non-empty parts: A<sub>1</sub>=A[0], ..., A[P-1] and A<sub>2</sub>=A[P], ..., A[N-1] such that A<sub>1</sub>=A<sub>2</sub>.
