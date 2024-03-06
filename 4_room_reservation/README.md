# Room Reservation

View the problem on [HackerRank](https://www.hackerrank.com/contests/competitive-programming-x-acm-g-coding-competition/challenges/silence-swig)

### Description
With the end of the quarter approaching, library rooms at Santa Clara University are in high demand. N rooms can be reserved in time intervals (L, R), and students are looking for the room that offers the longest continuous availability to prepare for their finals. Each room has a list of S segments that are already booked that are sorted in order. What’s the longest continuous time you can book a room for?

### Input Format

The first line is the integer N, the number of available rooms you can book.  
The following lines of input start with integer S, the number of segments that are already booked for that room, followed by the start and ending time of those booked intervals as integer pairs.

### Constraints
```
1 <= N <= 100
0 <= S <= 23
0 <=  L <  R <= 24
```
### Output Format

The largest amount of time you can book a room for without any conflicts.

### Sample Input 0
```
2
1
5 7
2
10 12
15 17
```
### Sample Output 0
```
17
```
### Explanation 0
![reservation diagram](https://s3.amazonaws.com/hr-assets/0/1709331911-adda0a6beb-IMG_0068.jpg)
The first room (0-indexed) provides the largest interval of 17 hours (from 7-24).