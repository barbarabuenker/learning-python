# Rosalind IPRB: Mendel's First Law

# given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

# my dataset:
k = 26
m = 22
n = 28

# possibilities of mating where offspring will possess a dominant allele
## k x k
## k x m
## k x n
## m x k
## m x m
## m x n
## n x k
## n x m
## note: n x n would only leave offspring with recessive alleles!

# number of individuals in population:
total_population = k + m + n

# percentage of offspring with dominant allele for ...
## k x k --> 100%
## k x m --> 100%
## k x n --> 100%
## m x k --> 100%
## m x m --> 75%
## m x n --> 50%
## n x k --> 100%
## n x m --> 50%

# probabilities:
prob_kk = (k/total_population) * ((k-1)/(total_population-1)) 
prob_km = (k/total_population) * (m/(total_population-1))
prob_kn = (k/total_population) * (n/(total_population-1))
prob_mk = (m/total_population) * (k/(total_population-1))
prob_mm = (m/total_population) * ((m-1)/(total_population-1)) * 0.75
prob_mn = (m/total_population) * (n/(total_population-1)) * 0.5
prob_nk = (n/total_population) * (k/(total_population-1))
prob_nm = (n/total_population) * (m/(total_population-1)) * 0.5

# probability that two randomly selected mating organisms will produce an individual possessing a dominant allele:
prob_dominant_phenotype = prob_kk + prob_km + prob_kn + prob_mk + prob_mm + prob_mn + prob_nk + prob_nm
print(prob_dominant_phenotype)

# my result: 0.7390350877192982 (which is correct)