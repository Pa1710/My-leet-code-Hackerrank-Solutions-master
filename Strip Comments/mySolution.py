def solution(string, markers):
    si = 0
    esi = 0
    s = ""
    for index, i in enumerate(string):
        if(index < esi):
            continue
        if(i in markers):
            ssi = index
            esi = index
            while(string[esi] != "\n") and (esi != (len(string)-1)):
                esi += 1
            s += string[si:(ssi-1)] + "\n"
            si = esi+1
    s += string[si:]
    if(s[-1] == "\n"):
        return s[:-1]
    return s
