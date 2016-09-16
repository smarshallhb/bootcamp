# py.test gives the testing functionality
import pytest

# We'll use our bioinformatics dictionary from before
import bioinfo_dicts as bd

def n_neg(seq):
    """Number of negative residues a protein sequence"""
    seq = seq.upper()
    for aa in seq:
        if aa not in bd.aa.keys():
            raise RuntimeError(aa + ' is not a valid amino acid.')
    return seq.count('E') + seq.count('D')


def test_n_neg():
    """Perform unit tests on n_neg."""

    assert n_neg('E') == 1
    assert n_neg('D') == 1
    assert n_neg('') == 0
    assert n_neg('ACKLWTTAE') == 1
    assert n_neg('DDDDEEEE') == 8
    assert n_neg('acklwttae') == 1


# Run all the tests
test_n_neg()
