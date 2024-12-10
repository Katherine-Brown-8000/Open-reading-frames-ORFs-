sequence = "TGGATGTTAATTGTTTTAATTGTTTTAATTGTTTTAATTGTTTTAATTGTTTTAATTGTTTTAATTGTTTTAATTGTTTTAATTGTTTTAATTGTTTTAATTGTTTGA"

def ORF(sequence):
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    orfs = []

    for frame in range(3):
        for i in range(frame, len(sequence) - 2, 3):
            codon = sequence[i:i+3]

            if codon == start_codon:
                for j in range(i + 3, len(sequence) - 2, 3):
                    if sequence[j:j+3] in stop_codons:
                        orfs.append(sequence[i:j+3])
                        break

    return orfs

orfs = ORF(sequence)
for i, orf in enumerate(orfs):
    print(f"ORF {i+1}: {orf}")
