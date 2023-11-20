# Rosalind REVC: Complementing a Strand of DNA

# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement s cof s.

# Note: No yet "officially" solved with individual dataset on Rosalind.

s = "AAAACCCGGT"

# translate:
s_c = ""
for letter in s:
    if letter == "A":
        s_c = s_c + "T"
    if letter == "C":
        s_c = s_c + "G"
    if letter == "G":
        s_c = s_c + "C"
    if letter == "T":
        s_c = s_c + "A"

# reverse:
s_c = s_c[::-1]
print(s_c)
