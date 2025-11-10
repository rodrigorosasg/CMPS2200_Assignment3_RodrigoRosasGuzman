import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def fast_MED(S, T):
    m, n = len(S), len(T)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        dp[i][0] = i
    for j in range(1, n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if S[i-1] == T[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
    return dp[m][n]


def fast_align_MED(S, T):
    m, n = len(S), len(T)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        dp[i][0] = i
    for j in range(1, n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if S[i-1] == T[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
    i, j = m, n
    out_S = []
    out_T = []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and S[i-1] == T[j-1] and dp[i][j] == dp[i-1][j-1]:
            out_S.append(S[i-1])
            out_T.append(T[j-1])
            i -= 1
            j -= 1
        elif i > 0 and (j == 0 or dp[i][j] == dp[i-1][j] + 1):
            out_S.append(S[i-1])
            out_T.append('-')
            i -= 1
        else:
            out_S.append('-')
            out_T.append(T[j-1])
            j -= 1
    return ''.join(reversed(out_S)), ''.join(reversed(out_T))
