import bioinfo_dicts
def one_to_three(seq):
    seq=seq.upper()
    aa_list=[]
    for amino_acid in seq:
        aa_list+=[bioinfo_dicts.aa[amino_acid],"-"]
    return "".join(aa_list[:-1])
