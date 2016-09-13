with open("/Users/stephenmarshall/git/bootcamp/data/salmonella_spi1_region.fna") as f:
    seq=f_list = f.readlines()

final=[]
for each in seq:
    if ">" not in each:
        final.append(each.strip())

ID=seq[0].strip()
salm="".join(final)







def gc_blocks(seq, block_size):
    count1=0
    count2=block_size
    GClist=[]
    while count2<len(seq):
        seq2=seq[count1:count2]
        GClist.append((seq2.count("G")+seq2.count("C"))/float(len(seq2)))
        count1+=block_size
        count2+=block_size
    return tuple(GClist)


def gc_map(seq, block_size, gc_thresh):
    count1=0
    count2=block_size
    GClist=[]
    while count2<len(seq):
        seq2=seq[count1:count2]
        if((seq2.count("G")+seq2.count("C"))/float(len(seq2)))>=gc_thresh:
            GClist.append(seq2.upper())
        else:
            GClist.append(seq2.lower())
        count1+=block_size
        count2+=block_size
    return "".join(GClist)


def longest_orf(seq):
    s=seq
    longest=''
    while len(s)>=6:
        s=s[s.find("ATG"):]
        longlist=["ATG"]
        count1=0
        count2=3
        stop=False
        stops=["TGA","TAG","TAA"]
        while count2<len(s) and stop==False:
            if s[count1:count2] in stops:
                stop=True
            longlist.append(s[count1:count2])
            count1+=3
            count2+=3
        for each in stops:
            if each == longlist[-1]and len("".join(longlist))>len(longest) :
                longest="".join(longlist)
        s=s[1:]
    return longest

salmlong=longest_orf(salm)

import bioinfo_dicts as bd

def translate(seq):
    aa=[]
    count1=0
    count2=3
    while count2<len(seq)+1:
        aa.append(bd.codons[seq[count1:count2]])
        count1+=3
        count2+=3
    return "".join(aa)

translate(salmlong)

#two-component sensor histidine kinase BarA [Salmonella enterica]


def longest_n_orf(seq,n):
    s=seq
    longest=[""]*n
    while len(s)>=6:
        s=s[s.find("ATG"):]
        longlist=["ATG"]
        count1=0
        count2=3
        stop=False
        stops=["TGA","TAG","TAA"]
        while count2<len(s) and stop==False:
            if s[count1:count2] in stops:
                stop=True
            longlist.append(s[count1:count2])
            count1+=3
            count2+=3
        for each in stops:
            if each == longlist[-1]:
                x=0
                cont=True
                while x<n and cont==True:
                    if len("".join(longlist))>len(longest[x]):
                        longest[x]="".join(longlist)
                        cont=False
                    x=x+1
        s=s[1:]
    return longest

longest_n_orf(salm,2)
