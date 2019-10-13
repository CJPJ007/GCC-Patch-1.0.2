# modify this function, and create other functions below as you wish
def question02(risk, bonus, trader):
    # modify and then return the variable below
    answer = -5
    for i in range(0,len(trader)):
        lis.append(bonus[i]+trader[i]-risk[i])
    answer = len(trader)*(bonus[lis.index(max(lis))])
    return answer
