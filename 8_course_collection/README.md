# Course Collection

View the problem on [HackerRank](https://www.hackerrank.com/contests/competitive-programming-x-acm-g-coding-competition/challenges/class-combination)

### Description
You are planning courses that you need to take for a given quarter, but you are behind on units, so you are trying to take as many as you can. There are M courses offered in one quarter and each course will give you U units. Certain courses can only be taken if their corequisite course is also being taken at the same time. You have to take a certain core class, denoted as class 0, and from there you can choose other classes that have class 0 as a corequisite. Given that you can only take N classes this quarter, determine the maximum number of units you can take.

### Input Format

The maximum units that you can take.

### Constraints

```
1 <= N <= M <= 50
0 <= U <= 10^4
```

### Output Format

The maximum units that you can take.

### Sample Input 0

```
4 7
0 1
0 2
1 3
1 4
2 5
2 6
1 2 2 4 5 3 2
```
### Sample Output 0
```
12
```
### Explanation 0

0, 1, 3, 4 are the classes with units 1, 2, 4, 5 that result in the highest total units of 12.
