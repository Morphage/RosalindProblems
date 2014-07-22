import itertools

def parse_rna_table(file_name):
    rna_table = {}

    with open(file_name, 'r') as file:
        for line in file:
            codon, protein = line.rstrip().split(" ")
            rna_table[codon] = protein
    
    return rna_table        

if __name__ == '__main__':
    rna_table = parse_rna_table("rna_table.txt")
    rna_sequence = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    protein = ""
    
    for i in range(0, len(rna_sequence), 3):
        amino_acid = rna_table[rna_sequence[i:i+3]]
        if amino_acid == "Stop":
            break
        else:
            protein += amino_acid

    print protein