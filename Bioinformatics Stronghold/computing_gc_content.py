from collections import defaultdict

def count_gc(sequence):
    count = 0
    for nuc in sequence:
        if nuc == "G" or nuc == "C":
            count += 1
    return count

def parse_file(file_name):
    file = open(file_name, "r")
    fasta_data = file.readlines()
    file.close()
    
    fasta_id_sequences = defaultdict(lambda: "")
    id = ""

    for line in fasta_data:
        if line[0] == '>':
            id = line[1:].rstrip()
        else:
            fasta_id_sequences[id] += line.rstrip()

    return fasta_id_sequences

if __name__ == '__main__':
    fasta_id_sequences = parse_file("data.txt")

    for id in fasta_id_sequences:
        count = count_gc(fasta_id_sequences[id])
        fasta_id_sequences[id] = float(count * 100) / float(len(fasta_id_sequences[id]))

    #max_id = max(fasta_id_sequences.iterkeys(), key=(lambda key: fasta_id_sequences[key]))
    max_id = max(fasta_id_sequences, key=fasta_id_sequences.get)
    
    print max_id
    print fasta_id_sequences[max_id]