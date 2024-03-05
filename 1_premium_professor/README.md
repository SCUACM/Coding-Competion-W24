# Premium Professor

It’s the middle of Fall quarter of freshman year and course registration is just around the corner. You know exactly what courses you want (or need), but you are not sure which professor to take. As a college beginner, you want to take the professors who teach the subject the best. You also have a fresh GPA, so you don’t want to take professors that will significantly impact your GPA in a bad way. You determine that the professor that you want to take has a high quality and a low difficulty. You're given access to N professors' RateMyProfessors scores.

Return the professor with the highest overall score, which is defined by the following formula:

![score formula](https://s3.amazonaws.com/hr-assets/0/1709345313-bf28db21ae-Screenshot2024-03-01at6.08.17PM.jpg)

It is guaranteed that only one professor will have the highest score.

### Input Format

The first line is integer N, the number of professors.
The second line consists of N strings, which are the professors’ names.
The third line consists of N floats, the professors’ quality scores.
The fourth line consists of N floats, the professors’ difficulty scores.

### Constraints

names are non-empty unique strings

```
1 <= N <= 1000
1.0 <= quality[i], difficulty[i] <= 5.0
```

### Output Format

The name of the professor with the highest score.

**Sample Input 0**

```
5
Eskafi Ostrov Rahman Atkinson Fang
4.00 4.54 3.57 4.53 4.46
3.85 4.47 3.58 4.10 4.37
```

**Sample Output 0**
```
Atkinson
```
**Explanation 0**

An example of a score calculation is as follows: Eskafi's overall score is **4.00** + (5.00 - **3.85**) = 5.15.

The 5 overall scores for the professors would be 5.15, 5.07, 4.99, 5.43, 5.09, and Atkinson has the highest score of 5.43.

**Sample Input 1**
```
3
A B C
1.0 1.0 1.0
4.5 3.9 2.7
```
**Sample Output 1**
```
C
```

**Sample Input 2**
```
3
Yin Ho Herzig
5.0 4.0 3.0
4.5 4.0 3.5
```

**Sample Output 2**
```
Yin
```