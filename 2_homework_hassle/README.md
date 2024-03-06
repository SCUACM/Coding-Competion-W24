# Homework Hassle

View the problem on [HackerRank](https://www.hackerrank.com/contests/competitive-programming-x-acm-g-coding-competition/challenges/homework-hastle)

### Description
It’s nearing the end of the quarter and you’ve totally been slacking on your COEN 12 assignments! You’re not sure if you can do them all, but you want to maximize your grade given the amount of time you have left, and you know that each assignment is worth the same amount of points. You have N assignments, and each one will take T[i] minutes to complete. Given that you only have M minutes to do work, find out the maximum number of assignments you can completely finish.

### Input Format

The first line is integer N, the number of assignments.  
The second line is integer M, the number of minutes you have.  
The third line contains N integers, which are the amount of time each assignment will take to complete.

### Constraints
```
0 <= M <= 10^4
1 <= N <= 10^4
1 <= T[i] <= 1000
```
### Output Format

The number of assignments you end up completing in the given time.

### Sample Input 0
```
7
100
15 25 20 50 20 15 25
```
### Sample Output 0
```
5
```
### Explanation 0

Do the assignments that take 15, 25, 20, 20, and 15 minutes. It can be shown that this is the maximum number of assignments that can be done.
