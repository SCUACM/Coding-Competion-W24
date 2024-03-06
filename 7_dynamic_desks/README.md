# Dynamic Desks

View the problem on [HackerRank](https://www.hackerrank.com/contests/competitive-programming-x-acm-g-coding-competition/challenges/dynamic-desks)

### Description
You are a TA for Dr. Dezfouli and students in their class are allowed to retake an exam during your office hours. However, Dr. Dezfouli is worried if the students sit too close to each other, they will cheat off of each other. Dr. Dezfouli wants to make sure that any students taking the exam have desks at least S spaces apart. Given a total of N desks, return the number of unique states where the desks are arranged properly.

### Input Format

The first is the number of desks, integer N. The second number (on the same line) is the minium number of spaces, integer S, between each desk.

### Constraints

```
1 <= N <= 50
0 <= S <= 50
```

### Output Format

The number of unique states where the desks are arranged properly.

### Sample Input 0

```
4 2
```
### Sample Output 0
```
6
```
### Explanation 0

The six valid states of 4 spaces are OOOO, XOOO, OXOO, OOXO, OOOX, and XOOX. XOXO and OXOX are invalid because there is only one space in between two desks.
