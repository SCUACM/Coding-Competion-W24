# Silence, Swig

View the problem on [HackerRank](https://www.hackerrank.com/contests/competitive-programming-x-acm-g-coding-competition/challenges/silence-swig)

### Description
You unfortunately got selected for Swig Residence Hall... However, you’re lucky enough to be able to choose your own room, but your quest for convenience comes with a catch — certain rooms are louder than others when outsiders shout “Wake Up, Swig!”.

There are N rooms to pick between and the ith room has a certain volume V[i]. You want to pick the room with the lowest score, which is defined by the following formula:

![score formula](https://s3.amazonaws.com/hr-assets/0/1709351503-6338d9896c-Screenshot2024-03-01at7.51.21PM.jpg)

(Try and think about what this formula means. You replace the residents of a room i.e. their volume doesn't matter, the further away a room is the less loud it is, etc.)

### Input Format

The first line is integer N, the number of rooms there are.  
The second line contains the volume of room i as a float, V[i].

### Constraints
```
0 < N <= 1000
0.0 <= V[i] <= 1000
```
### Output Format

The index of the room with the minimum score.

### Sample Input 0
```
3
1.0 2.0 1.0
```
### Sample Output 0
```
1
```
### Sample Input 1
```
10
6.5 5.5 5.0 6.3 9.4 7.2 9.7 9.9 5.4 4.1
```
### Sample Output 1
```
0
```