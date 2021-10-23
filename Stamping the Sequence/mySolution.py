class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:

        sizeS = len(stamp)
        sizeT = len(target)
        stamp, target = list(stamp), list(target)
        flag1 = True
        flag2 = True
        l = list()
        while(flag1):
            flag1 = False
            for i in range(sizeT-sizeS+1):
                flag2 = False
                for j in range(sizeS):
                    if target[i+j] == '?':
                        continue
                    elif target[i+j] != stamp[j]:
                        break
                    flag2 = True
                else:
                    if flag2:
                        flag1 = True
                        for k in range(i, i + sizeS):
                            target[k] = '?'
                        l.append(i)
        for i in range(sizeT):
            if target[i] != '?':
                return []
        return reversed(l)
