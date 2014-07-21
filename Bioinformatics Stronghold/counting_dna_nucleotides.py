from collections import defaultdict

def count_nucleotides(dna_sequence):
    nucleotides = defaultdict(int)
    
    for nucleotide in dna_sequence:
        nucleotides[nucleotide] += 1
    
    print nucleotides["A"], nucleotides["C"], nucleotides["G"], nucleotides["T"]

if __name__ == '__main__':
    count_nucleotides("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")