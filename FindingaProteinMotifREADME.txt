This program solves the Finding a Protein Motif problem through a
simple process of retrieving the sequences for each protein, finding
all the locations of the N amino acid, then walking through the next
few amino acids to see if they meet the criteria for the
N-glycosylation motif. If they do, the location is added to a list.
When all the lists are compiled into one large list, the locations
are printed out alongside the ID of the protein. This program works
out this process step-by-step but it is important to note all three
loops can be consolidated into one loop. I split it into three parts
to make it easier to follow. The time complexity would therefore
technically be O(3n) which is of course still treated as O(n) since
the runtime of the algorithm still only increases linearly with n.
However, the program still runs rather slowly, since retrieving
sequences from UniProt with this method does not seem to be very
efficient.
(Note: Testing this program requires the rosalind_mprt.txt file,
also located in this repository)
