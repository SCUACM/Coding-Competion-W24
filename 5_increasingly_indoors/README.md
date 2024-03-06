# Increasingly Indoors

View the problem on [HackerRank](https://www.hackerrank.com/contests/competitive-programming-x-acm-g-coding-competition/challenges/increasingly-indoors)

### Description
The ACM Club president, Jordan Mosakowski, is very curious about how far “indoors” he can get inside SCU, so he asks you to help him with the task. He defines how indoors a room is by the minimum number of doors you can go through to go from the room to the outdoors or from the outdoors to the room. For example, the furthest inside he can be in SCDI is a factor of 3, since you enter any set of doors from the outside, then enter a certain classroom that has a closet, then enter the closet. However, a door such as a bathroom stall door does not count as being more indoors because you don't enter a new room. Given a building as a list of D doors connecting rooms to each other or connecting a room R[i] to the outside, determine how far indoors you can be in the building and determine the rooms that are the most indoors.

### Input Format

The first line is the number of doors in the building.
Each of the following rows of input consists of rooms i and j that indicate that i and j are connected by a door. (There are cases where i == j, like the bathroom stall door)

### Constraints

```
1 <= D <= 10^4
0 <= R[i] <= 10^4
```

### Output Format

The first line is how far indoors you can be inside of the building.The second line is the room numbers that are the most indoors, sorted by room number.

### Sample Input 0

```
7
0 1
8 9
1 2
2 4
1 3
4 5
3 8
```
### Sample Output 0
```
4
5 9
```
### Explanation 0
![image](https://s3.amazonaws.com/hr-assets/0/1709247909-7a0f1209eb-IMG_0066.jpg)

Start outside (indicated by 0), go to room 1, then go to room 2, then room 4, then room 5. It takes 4 doors to get to room 5. Start outside, go to room 1, then go to room 3, then room 8, then room 9. It takes 4 doors to get to room 9. It can be shown that 5 and 9 are the rooms that are the most indoors with a factor of 4
