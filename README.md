# Python katas
Short exercises in Python from Advent of Code, Code Jams, Codility, Hackerrank, Cracking the Coding Interview, and this [repo](https://github.com/karan/Projects).

## AoC 2017
Problems from [Advent of Code 2017](https://adventofcode.com/2017).

## Code Jams
Problems from Google Code Jams.

## Codility
Training exercises from [Codility](https://www.codility.com). Probably correct, at least according to the autograder (all score 100%).

#### Array rotation
Given a non-empty array `A` consisting of `N` integers, return the array shifted to the right by `K` indices.

#### Binary gap
Find the longest sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of an integer `N`.

#### Brackets
A string `S` is considered to be properly nested if any of the following conditions is true:

* `S` is empty;
* `S` has the form `(U)` or `[U]` or `{U}` where `U` is a properly nested string;
* `S` has the form `VW` where `V` and `W` are properly nested strings.

Write a function that returns 1 if `S` is properly nested and 0 otherwise.

#### Count div
Compute the number of integers divisible by `k` in range `[a, b]`.

#### Disc intersections
We draw `N` discs on a plane. The discs are numbered from 0 to `N-1`. A zero-indexed array `A` of `N` non-negative integers, specifying the radiuses of the discs, is given. The `J`-th disc is drawn with its center at `(J, 0)` and radius `A[J]`.

Two disc intersect if they have at least one common point (assuming that the discs contain their borders). Write a function that, given an array `A` describing `N` discs as explained above, returns the number of unordered pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

#### Distinct pythonic
Calculate the number of distinct values in an array `A` using a pythonic one-liner.

#### Distinct unpythonic
Calculate the number of distinct values in an array `A`. Probably the expected solution, as the exercise is meant to use sorting.

#### Fish
You are given two non-empty zero-indexed arrays `A` and `B` consisting of `N` integers. Arrays `A` and `B` represent `N` voracious fish in a river, ordered downstream along the flow of the river.

The fish are numbered from 0 to `N-1`. If `P` and `Q` are two fish and `P < Q`, then fish `P` is initially upstream of fish `Q`.

Array `A` contains the sizes of the fish. Array `B` contains the directions of the fish, where:

* 0 represents a fish flowing upstream,
* 1 represents a fish flowing downstream.

Two fish `P` and `Q` meet each other when `P` < `Q`, `B[P] = 1` and `B[Q] = 0`, and there are no living fish between them. After they meet:

* If `A[P] > A[Q]` then `P` eats `Q`, and `P` will still be flowing downstream,
* If `A[Q] > A[P]` then `Q` eats `P`, and `Q` will still be flowing upstream.

We assume that fish moving in the same direction never meet. The goal is to calculate the number of fish that will stay alive.

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

#### Nesting
A string `S` consisting of `N` characters is called properly nested if:

* `S` is empty;
* `S` has the form "(U)" where `U` is a properly nested string;
* `S` has the form "VW" where `V` and `W` are properly nested strings.

Write a function that, given a string `S` consisting of N characters, returns 1 if string `S` is properly nested and 0 otherwise.

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

## Miscellaneous
Problems from various sources, mostly from this [repo](https://github.com/karan/Projects).

#### Asterisk triangle
Print some simple figures.

#### Pi
Calculate the first `n` digits of π using a spigot algorithm (Rabinowitz, Wagon, 1995). 
