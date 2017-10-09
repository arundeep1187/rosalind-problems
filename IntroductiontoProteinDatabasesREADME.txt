This program solves the Introduction to Protein Databases problem
located in Rosalind's bioinformatics armory. It inputs any protein ID
(entered in line 18) and scans through its text file located on the
UniProt database looking for the markers associated with the
biological processes. If it parses through to the end of file on any
of these steps, it will skips the rest of the steps and report none.
If it gets to the final step, it will input the biological processes
and print the results.
Time Complexity: O(1), though this particular problem asks for only 1
protein. The method for retrieving the information from UniProt is
also inefficient and therefore, the program operates slower than a
O(1) algorithm would ideally operate.
