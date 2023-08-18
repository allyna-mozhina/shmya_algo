def check_brackets(bseq):
    s = 0

    for b in bseq:
        if b == '(':
            s += 1
        elif b == ')':
            s -= 1
        else:
            return False
        
        if s < 0:
            return False
    
    return s == 0

bseq = '()((()))()'
assert(check_brackets(bseq) == True)

bseq = '()(((()))()'
assert(check_brackets(bseq) == False)
