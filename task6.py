def check_brackets(bseq):
    s = []

    for b in bseq:
        if b == '(':
            s.append(b)
        elif b == ')':
            if s:
                s.pop()
            else:
                return False
        else:
            return False
    
    if s:
        return False
    else:
        return True

bseq = '()((()))()'
assert(check_brackets(bseq) == True)

bseq = '()(((()))()'
assert(check_brackets(bseq) == False)
