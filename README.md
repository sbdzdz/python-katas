# Python katas
Short exercises in Python. Mostly FizzBuzz level, although some are more interesting (e.g. `Pi`, `Genomic range query`, `Passing cars`, `Max counter`).

## Miscellaneous
Problems from various sources, mostly from this [excellent repo](https://github.com/karan/Projects).

#### Pi
Calculate the first `n` digits of π using a spigot algorithm (Rabinowitz, Wagon, 1995). 

#### Asterisk triangle
Print some simple figures.

## Code Jams
Problems from Google Code Jams.

#### Counting sheep
Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep faster. First, she picks a number `N`. Then she starts naming `N`, `2N`, `3N`, and so on. Whenever she names a number, she thinks about all of the digits in that number. She keeps track of which digits she has seen at least once so far as part of any number she has named. Once she has seen each of the ten digits at least once, she will fall asleep. Knowing `N`, print the last number Bleatrix will see before falling asleep. If the poor sheep will count forever, print INSOMNIA instead.

#### Revenge of the pancakes
Given a string of `-` and `+` describing a stack of pancakes, print the minimal number of flips required so that all pancakes are happy side up (`+`).

The flip is defined as follows: if we number the pancakes `1, 2, ..., N` from top to bottom, choose the top `i` pancakes to flip. Then, after the flip, the stack is `i, i-1, ..., 2, 1, i+1, i+2, ..., N`. Pancakes `1, 2, ..., i` now have the opposite side up, whereas pancakes `i+1, i+2, ..., N` have the same side up that they had up before.

#### Coin jam
A jamcoin is a string of N >= 2 digits with the following properties:

* Every digit is either 0 or 1.
* The first digit is 1 and the last digit is 1.
* If you interpret the string in any base between 2 and 10, inclusive, the resulting number is not prime.

There are communities that use jamcoins as a form of currency. When sending someone a jamcoin, it is polite to prove that the jamcoin is legitimate by including a nontrivial divisor of that jamcoin's interpretation in each base from 2 to 10. For convenience, these divisors must be expressed in base 10.

Given `J` and `N`, produce `J` different jamcoins of length `N`, along with proof that they are legitimate.

#### File fix-it
Given a list of paths of existing directories on a Unix system and a list of paths of directories to create, output the minimal number of `mkdir` commands required to create the new directories. For example, given:
	Existing:
		/chicken
		/chicken/egg
		/chicken/egg/spam
	New:
		/chicken
		/chicken/egg/ham/spam
		/chicken/spam
the answer should be 3, because the required commands are:
	mkdir chicken/egg/ham
	mkdir chicken/egg/ham/spam
	mkdir chicken/spam

#### Minimum scalar product
You are given two vectors: X and Y. Suppose you are allowed to permute the coordinates of each vector as you wish. Choose two permutations such that the scalar product of your two new vectors is the smallest possible, and output that minimum scalar product. 

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
Find an integer `P` that splits a non-empty array `A` into two non-empty parts: `A1=A[0], ..., A[P-1]` and `A2=A[P], ..., A[N-1]` such that `A1=A2`.
