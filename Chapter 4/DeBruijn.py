"""
    File: DeBruijn
    Author: steve
    Created: 06/12/14
    
"""
from builtins import sorted, dict
import sys
from builtins import open


def build_debruijn_graph(kmers):
    """
    Each kmer forms 2 nods with one edge between them. Create nodes merge with existing collection.
    :param kmers:
    :return:
    """
    dbg = dict()

    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]

        if prefix in dbg:
            dbg[prefix].append(suffix)
        else:
            dbg[prefix] = [suffix]

    return dbg


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    k = 12
    seq = "GCCCCCGCGGGGTAGTCCCCAGTAACATTCTAAGCTAGGGCTCGGCCCAAGCTACAAGGAGAAACACTATAGTGTAGGCGAGGATTGTCATGACACAACTGGTGAAAGTCATACCTCTTCCGCTTCTTAACCGGCGGCATCAGAGAAAAGTATAACGAACCTAAAGTTGAACACTCCGTTTCAGTGACCACGAGTTGTACCCGTTGTGTTATGGCCCGACGCTGGTTGATGGCTCCCTGACCTTTGTCAACAGCCCCCTGCATATTATATGAGGGCATCATGTAAGCGTTCCACTTGAACACGATGCGCACACCCTGTCCAAAAGTGTGAACGGCACTTGATAATCACGCGGGATACTCCTATCTGCACAACTTGAGGAGAAGGGCTTCCCGTCGCTCGACGACAATCCATGCTGGCTAACAGGTCCGTACCATATGTTGAAATGCGAAGGTTCTCGGTGGTGCCGCTCCACTTCAGCATGTACTGGTATGAGCTTGGTGAGTCATGGAAGCTCGATTCTTATACTCCCATGGGTGCTCGGCGGTCCACACATCGCATATGGCCCCAGGGGATGGATGAAACGTTGAGCGTTTTAGAACATGACATAAGGGAGGTGATTTACCCCACCCACCAACGAGCGATTCATCTTACGCCGACTGCACAGCCACGGTATCTACCGCTACGATGCAAACCTTTCTATTATCCTACTGGCGTCAGCCACTGCGCGTTGGTTTGGTGATAATTTGGACCGTACGGACTCTACCAAGGAGCCATGCTGAGCAGTCCAGTTGTATCTTCGATTGAAGATCAAGGTCGCAGCATCATGGTACGAGGGTGACTTCCTGGTGGCCCCGCGATTGAGATCCAGTCCCCGTTGCCATACCACTACGCACACCACTTGGTGTTAAGCGAAACCCTTCGCGCATTGTCCTCCATTGTCTGAGTGGATGCGCTAAATTAACTTCTACGTGGACAATGGTGCAGCGTACTGTCCATGGCGATTCGTACAGGAGTGGTGTTTGAACAGCTCTGGAGCGAAGTGAGAAGTGGTGTGGCGGCTCCCGGTCGTGGAGTCGCCGGAGACTTCTTATTTCACGTACTGTAAATAATGATCGCCCTAATTCGGCGCCCACCCTCGTGCCCCGCCCCTGCTGATTTTCGTCACATGGCGCGTGCTAACCCACATTTTGCGTCCTGGCTTGTTAGTCCCTGGATCCCCAAAAAATAATCTCCGCTGACTACTGTTTTGGACGGAAAACGAGGATCAGTAAACAGGTGTGAGCATCACGGTGCGTAAGACGTTACAACACCTTCGTTGTGGTTCTATTTACTGTGGTCCATCCGGAGAACCGAATCACGTAGTGCGAATCTGTTGCCTCTAGTCGACCATGACAGTTTCCCTAACATGCGTGACGGGACATGAACGGAGGACACTCTTTGTTCTTAATAGTTCTGTAACCCAACCTGTTGTTAGTGGGAGTACCAAAGATGATGTACAGAGAACCAGCATAGATGTTACACGACTACCTCACGGGTTAGTACGTATGGGCTTGAAAGATTGTTTTTTAGGTAGTCATGTGGTCTTTTTAGATCATGGACAGTCGCCCATAGACTCCTGCTAGGGGCCGCGGTAATTCTCCGCCCTGAACCGGTCCCTCCTTAGCCCCCAGGGGCGGCCGGGTCCAGTGTGGCAAGACCTTTTTCAAGTCCTGCCTATGGCCACGGCGAGATCCTATTATATGTACTTAAACATCGTTTAGAGTTCCCTACGTCTCACGATTCGAGTCTCGGGCTTCCCGCAGCACGCTACCTACTCCTGCACGCCTGTCTCACATTAGAACACGTCAGGTTGGATGTTTGGTCGGGAACTGCCGTACACTACCCACCTTCGTTGACTCTTGGCGAATTATCGCGTCATGATTTCCCTAAACTTGGTTTTTGGTTAACTTAGCTATCTCAACTAGATATTTTCGAAGCCTGCTCGCCCCACATCCCAAATG"

    with open("kmers.txt") as contents:
        kmers = [line.rstrip('\n') for line in contents]

    # for s in SequenceUtils.each_kmer(seq, k):
    # kmers.append(s)

    result = build_debruijn_graph(kmers)

    with open("debruijn.txt", "w") as text_file:
        for key, value in sorted(result.items()):
            text_file.write(key + " -> " + ",".join(value) + "\n")


if __name__ == "__main__":
    sys.exit(main())