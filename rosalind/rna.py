# Rosalind RNA: Transcribing DNA into RNA

# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.

# Note: No yet "officially" solved with individual dataset on Rosalind.

t = "GATGGAACTTGACTACGTAAATT"

u = ""
for letter in t:
    if letter == "A":
        u = u + "A"
    if letter == "C":
        u = u + "C"
    if letter == "G":
        u = u + "G"
    if letter == "T":
        u = u + "U"

print(u)