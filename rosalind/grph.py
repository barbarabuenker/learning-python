# Rosalind: GRPH

# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
# Return:
## The adjacency list corresponding to the overlap graph O_k. You may return edges in any order. 
## k = 3 and refers to a positive integer.
## each string is represented by a node, 
## and string s is connected to string t with a directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s≠t

input = open("rosalind_grph.txt", "r")

fasta_list = input.read().split(">")[1:]

input.close()

fasta_dictionary = {}

for i in fasta_list:
    i = i.split("\n")
    print(i)
    key = i[0]
    value = ""
    for j in i[1:]:
        value = value + j
        fasta_dictionary[key] = value

id_list = []
dna_list = []

for key in fasta_dictionary:
    id_list.append(key)
    dna_list.append(fasta_dictionary[key])

string_list_1 = []
string_list_2 = []

for string1 in dna_list:
    for string2 in dna_list:
        if string1 != string2 and string1[-3:] == string2[:3]:
            string_list_1.append(string1)
            string_list_2.append(string2)

indices_list_1 = []
indices_list_2 = []

for string1 in dna_list:
    for string2 in dna_list:
        if string1 != string2 and string1[-3:] == string2[:3]:
            indices_list_1.append(dna_list.index(string1))
            indices_list_2.append(dna_list.index(string2))

for i in range(len(indices_list_1)):
    print(id_list[indices_list_1[i]], id_list[indices_list_2[i]])