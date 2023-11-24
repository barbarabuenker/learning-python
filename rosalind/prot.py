# Rosalind PROT: Translating RNA into Protein 

# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
# Return: The protein string encoded by s.

# my dataset:
rna_string = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

# define empty triplet variable
rna_triplet = []

# split RNA string in triplets:
for index in range(len(rna_string)):
    if index == 0:
        rna_triplet.append(rna_string[index:index+3])
    if index % 3 == 0:
        rna_triplet.append(rna_string[index:index+3])

# create a dictionary for RNA codon table:
codon_table = {"UUU": "F",
               "CUU": "L",
                "AUU": "I",
                "GUU": "V",
                "UUC": "F", 
                "CUC": "L",
                "AUC": "I",
                "GUC": "V",
                "UUA": "L",
                "CUA": "L", 
                "AUA": "I", 
                "GUA": "V", 
                "UUG": "L",
                "CUG": "L",
                "AUG": "M",
                "GUG": "V",
                "UCU": "S",
                "CCU": "P",
                "ACU": "T",
                "GCU": "A", 
                "UCC": "S", 
                "CCC": "P",
                "ACC": "T",
                "GCC": "A",
                "UCA": "S",
                "CCA": "P",
                "ACA": "T",
                "GCA": "A",
                "UCG": "S",
                "CCG": "P",
                "ACG": "T",
                "GCG": "A",
                "UAU": "Y",
                "CAU": "H",
                "AAU": "N",
                "GAU": "D",
                "UAC": "Y",
                "CAC": "H",
                "AAC": "N",
                "GAC": "D",
                "UAA": "Stop",
                "CAA": "Q",
                "AAA": "K",
                "GAA": "E",
                "UAG": "Stop",
                "CAG": "Q",
                "AAG": "K",
                "GAG": "E",
                "UGU": "C",
                "CGU": "R",
                "AGU": "S",
                "GGU": "G",
                "UGC": "C",      
                "CGC": "R",
                "AGC": "S",
                "GGC": "G",
                "UGA": "Stop",
                "CGA": "R",
                "AGA": "R",
                "GGA": "G",
                "UGG": "W",
                "CGG": "R",
                "AGG": "R",
                "GGG": "G" 
}

# create empty variable for protein string:
protein_string = ""

# translate RNA triplets to amino acids (--> create protein string):
for codon in rna_triplet:
    if codon_table[codon] is not "Stop":
        protein_string = protein_string + codon_table[codon] 
    else:
        break

print(protein_string)

