def remove_bad_chars(s1):
    bad_chars = ['.',' ']
    for i in bad_chars:
        s1 = s1.replace(i,'')
    return s1

def reverse(string):
    string = "".join(reversed(string))
    return string

def lcs(s1, s2):
    s1 = remove_bad_chars(s1)
    s2 = remove_bad_chars(s2)
    s1 = s1.lower()
    s2 = s2.lower()
    n = len(s1)
    m = len(s2)
    dp = [[0]*(m+3)]*(n+3)
    for i in range (0,n+1):
        for j in range (0, m+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif s1[i-1]==s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    p = n
    q = m
    str = ""
    while p!=0 and q!=0:
        if s1[p-1]==s2[q-1]:
            str = str+s1[p-1]
            p = p-1
            q = q-1
        else:
            if dp[p-1][q]>dp[p][q-1]:
                p = p-1
            else:
                q = q-1
    str = reverse(str)
    return len(str)


def sort(tup):
    tup.sort(key=lambda x: x[1],reverse=True)
    return tup