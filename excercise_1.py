
def reverser(each):
    new_str=""
    for each in each:
        new_str= each+new_str
    return new_str

def reverser(each):
    count=len(each)-1
    new_str=""
    while count>=0:
        new_str+= each[count]
        count-=1
    return new_str


def longest_same(seq1,seq2)
    count1=0
    count2=len(seq1)
    longest=''
    while count2>=1:
        while count1<count2:
            if seq1[count1:count2] in seq2:
                if len(seq1[count1:count2])>len(longest):
                    longest=seq1[count1:count2]
            count1+=1
        count2-=1
        count1=0
    return longest





def parenth_equal(ss):
    countopen=0
    countclosed=0
    for each in ss:
        if each=="(":
            countopen+=1
        if each==")":
            countclosed+=1
    if countopen==countclosed:
        return "equal"
    else:
        return "not equal"



def dotparen_to_bp(ss)
    tup=[]
    s= list(ss)
    revs=list(ss)
    revs.reverse()
    s="".join(s)
    revs="".join(revs)
    while "(" in s:
        s= list(s)
        revs=list(revs)
        mylist=[]
        sa="".join(s)
        mylist.append(sa.find("("))
        s[sa.find("(")]="."
        s="".join(s)
        s= list(s)
        revsa="".join(revs)
        mylist.append(len(revs)-revsa.find(")")-1)
        revs[revsa.find(")")]="."
        revs="".join(revs)
        revs= list(revs)
        tup.append(tuple(mylist)
    return tuple(tup)



def hairpin(y):
    x=dotparen_to_bp(y)
    left=[]
    right=[]
    for each in x:
        left.append(each[0])
        right.append(each[1])
    if int(min(right))-int(max(each(left))>3:
        return "valid"
    else:
        return "invalid"



def rna_ss_validator(seq, sec_struc, wobble=True):
        each=dotparen_to_bp(sec_struc)
        if wobble==True:
            for each in x:
                if seq[each[0]]=="G":
                    if seq[each[1]]!="U" and seq[each[1]]!="C":
                        return False
                if seq[each[0]]=="U":
                    if seq[each[1]]!="A" and seq[each[1]]!="G":
                        return False
                if seq[each[0]]=="C":
                    if seq[each[1]]!="G":
                        return False
                if seq[each[0]]=="A":
                    if seq[each[1]]!="U":
                        return False
            return True
        if wobble==False:
            for each in x:
                if seq[each[0]]=="G":
                    if seq[each[1]]!="C":
                        return False
                if seq[each[0]]=="U":
                    if seq[each[1]]!="A":
                        return False
                if seq[each[0]]=="C":
                    if seq[each[1]]!="G":
                        return False
                if seq[each[0]]=="A":
                    if seq[each[1]]!="U":
                        return False
            return True
