def parse_mono_table(file_name):
    mono_table = {}

    with open(file_name, 'r') as file:
        for line in file:
            amino_acid, weight = line.rstrip().split("   ")
            mono_table[amino_acid] = float(weight)
    
    return mono_table

if __name__ == '__main__':
    mono_table = parse_mono_table("monoisotopic_mass_table.txt")
    protein_string = "SKADYEK"
    total_weight = 0
    
    for amino_acid in protein_string:
        total_weight += mono_table[amino_acid]

    print total_weight