def dna_to_rna(dna_sequence):
    return dna_sequence.replace("T", "U")

if __name__ == '__main__':
    print dna_to_rna("GATGGAACTTGACTACGTAAATT")