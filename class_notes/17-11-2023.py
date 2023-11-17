# Introduction to programming for biologists - Notes - 17.11.2023
# ROSALIND DICTIONARIES:
# we need new python file and ipytyhon command line

s = "We tried list and we tried dicts also we tried Zen"
words = s.split()

# we look at every word in words
# if it is "we"
# we count it

how_many_times_did_we_see_we = 0
for word in words:
   if word == "we":
     how_many_times_did_we_see_we += 1
     print(how_many_times_did_we_see_we)

# 1. go through the list of words
# 2. for each word in the list:
# 2A> if we haven't seen it before:
#   put it in our bag of knowledge
#   set its counter to 1
# 2B> if we have seen it before:
#   increase its counter by 1

words = s.split()
bag_of_knowledge = []

for word in words:
    if word in bag_of_knowledge:
      # increase counter by 1
        bag_of_knowledge[word] += 1
    else:
      # set counter to 1
      bag_of_knowledge = 1
# pretty print like this
# key value

for key, value in bag_of_knowledge.items():
   print(key, value)


# complementing a strand of DNA (Rosalind exercise)
# we get a DNA sequence and have to calculate its reverse complement (A->T, C->G, T->A, G->C) + since its a reverse complement, we also have to flip the sequence around!
# input: AAAACCCGT
# want: reverse complement - 2 components = reverse and complement!
# decision tree see picture
# this is what happens at every step

# first, he wrote down input
# then he wrote down, where he wants to arrive
# then he wrote down the smaller steps
# he figured out how to do frist step
# then how to do other one
# the last step: figure out how to write it down in code!
# .. so know we have something that seems bulletproof! he came up with a recipe to complement ALL DNA strings - an algorithm; he did this by thinking out loud!
# ... basically combining 2 ideas (loop over + check at every position IF something is one thing or the other!)
# if you take a little bit of time to spell it out for ourselves, the code basically writes itself!
# we now need to figure out how to translate this into code

