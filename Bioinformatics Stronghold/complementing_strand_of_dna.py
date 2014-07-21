def reverse_complement(dna_sequence):
    reverse_complement = ""
    i = len(dna_sequence) - 1
    
    while i >= 0:
        if dna_sequence[i] == "A":
            reverse_complement += "T"
        elif dna_sequence[i] == "T":
            reverse_complement += "A"
        elif dna_sequence[i] == "C":
            reverse_complement += "G"
        else:
            reverse_complement += "C"
        i -= 1

    return reverse_complement

if __name__ == '__main__':
    print reverse_complement("AAAACCCGGT")