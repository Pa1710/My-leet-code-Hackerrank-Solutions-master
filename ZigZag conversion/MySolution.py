def convert(self, s: str, numRows: int) -> str:
    l = list(s)
    ans = list()
    # rowNo = 2
    # print(l[ : :numRows-1+numRows-1])
    # print(l[numRows-1: :numRows-1+numRows-1])
    # print(l[rowNo: :2*numRows-2])
    # print(l[rowNo: :2*(numRows-rowNo-1)])
    if(numRows == 1):
        return s
    for i in range(numRows):

        if i == 0:
            lTemp = l[::2*numRows-2]
            str1 = ''.join(lTemp)
            ans.append(str1)
            continue
        if i == numRows-1:
            lTemp = l[numRows-1::numRows-1+numRows-1]
            str2 = ''.join(lTemp)
            ans.append(str2)

            break
        j = i
        flag = 'D'
        while j <= len(l) - 1:
            if flag == 'D':
                ans.append(l[j])
                j = j + 2*(numRows - i - 1)
                flag = 'U'
            if flag == 'U':
                if(j <= len(l) - 1):
                    ans.append(l[j])
                    j = j + 2*i
                    flag = 'D'
    ansstr = ''.join(ans)
    return ansstr
