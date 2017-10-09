This solution for the Finding a Shared Motif problem on Rosalind
inputs a FASTA file, separating ID and sequence into two lists. It
will then create a matrix of the first two sequences based on
matching base pairs, where 0 = non-match and 1 = match. Using this
information, it will create a list of common subsequences from
largest to smallest. It will then test that list against the
remaining DNA sequences, deleting the current substring and
restarting its search for every search that fails until one succeeds.
That string will finally be printed and the program will terminate.
Time Complexity: Approximately O(m*n)
(Note: Testing this program requires the rosalind_lcsm.txt file,
also located in this repository)
