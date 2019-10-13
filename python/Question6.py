# modify this function, and create other functions below as you wish
def mymethod(ch1,ch2,s):
    idx=-1
    for si in s:
        if si[0]==ch1 and si[-1]==ch2 and idx<s.index(si):
            idx=s.index(si)
    return (idx)
def question06(portfolio):
    # modify and then return the variable below
    answer = mymethod('A','W',portfolio)
    return answer
