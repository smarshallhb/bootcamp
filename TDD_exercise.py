def find_codon_lesson6(codon, seq):
    """Find a specified codon with a given sequence."""

    i = 0
    # Scan sequence until we hit the start codon or the end of the sequence
    while seq[i:i+3] != codon and i < len(seq):
        i += 1

    if i == len(seq):
        return -1

    return i




seq='ATGGAGAACAACGAAGCCCCCTCCCCCTCGGGATCCAACAACAACGAGAACAACAATGCAGCCCAGAAGAAGCTGCAGCAGACCCAAGCCAAGGTGGACGAGGTGGTCGGGATTATGCGTGTGAACGTGGAGAAGGTCCTGGAGCGGGACCAGAAGCTATCGGAACTGGGCGAGCGTGCGGATCAGCTGGAGCAGGGAGCATCCCAGTTCGAGCAGCAGGCCGGCAAGCTGAAGCGCAAGCAATGGTGGGCCAACATGAAGATGATGATCATTCTGGGCGTGATAGCCGTTGTGCTGCTCATCATCGTTCTGGTGTCGCTTTTCAATTGA'
#################

def find_codon_lesson6(codon, seq):
    """Find a specified codon with a given sequence."""

    i = 0
    # Scan sequence until we hit the start codon or the end of the sequence
    while seq[i:i+3] != codon and i < len(seq):
        i += 3

    if i == len(seq):
        return -1

    return i

def test_find_codon():
    assert find_codon_lesson6("ATG",seq)==0
    assert find_codon_lesson6("AAT",seq)==54
    assert find_codon_lesson6("TGT",seq)==119
    assert find_codon_lesson6("TGC",seq)==-1



######################

def concentrations(Kd,ca0, cb0):
    cab=0.5*(ca0+cb0+Kd-numpy.sqrt((ca0+cb0+Kd)**2-4*ca0*cb0))
    ca=ca0-cab
    cb=cb0-cab
    return cab , ca , cb

def test_concentrations():
    Kd=numpy.logspace(1**-100,10)
    Kd=list(Kd)
    Kd.append(numpy.inf)
    ca0=numpy.logspace(1**-100,10)
    ca0=list(ca0)
    ca0.append(numpy.inf)
    cb0=numpy.logspace(1**-100,10)
    cb0=list(cb0)
    cb0.append(numpy.inf)
    for x in Kd:
        for y in ca0:
            for z in cb0:
                output=concentrations(x,y, z)
                assert numpy.isclose(x, (output[1]*output[2]/output[0]), atol=.01) , "Failure is {x},{y},{z},{t}".format(x=x,y=y,z=z,t=(output[1]*output[2]/output[0]))
                assert numpy.isclose(y, (output[0]+output[1]), atol=.01)
                assert numpy.isclose(z, (output[0]+output[2]), atol=.01)



test_concentrations()
