# CMPS 2200 Assignment 3
## Answers

**Name:**Rodrigo Rosas Guzman


Place all written answers from `assignment-03.md` here for easier grading.

1a. Take the largest coin with a value less than the remaining amount. Repeat this until the remainder is 0.

1b.  
Greedy- Assume 2^k is the largest coin, all solutions must use at least one of these coins. Any other combination will use more than one coin to reach the same value. 
Optimal- After you take on of the high denomination coins keep taking until you run out of currency. 

1c. The work and span of this algorithm is W 0(logn) S 0(logn)

2a. 1,3,4 n=6
Greedy picks 4+1+1, best picks 3+3, taking up a less amount of coins.

2b. OPT(x) = 1 + min(OPT(x - d))
each amount depends on the smaller one, so it works on less overall problems, being more efficient. 

2c. For each amount, check every coins value and take the smalles. 
w= 0(number of coins*value of money) s= 0(number of coins*value of money) since each one depends on the last.

3a. if the leters match, cost stays the same, if not, add one

3b. fast align med rebuilds the aligned strings by moving backwards and adding - where a character was added or deleted
