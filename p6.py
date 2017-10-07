#Counting Point Mutations

dna1 = 'GGTACCTAGGTCGTTAGTCTCCTTACTGGACCGCCGATCTCCTAAACAGCCTAGTTGGTCTTTATTTTAGGTATTCGATCCGCTGGAACCCGCCCACCCACTCCCTCATTACCCTGCATTCTGAGTATCACGCGAATGTAATAGTCTAATATCTTAAACCACACAGATGAGGTAATGGTTCCGCAGGGTACACTAGAGTATGGTAAGTAATGATTTGAGTCTGCGTCGCTAATGCGAGCCAAGATCCCAGGAATGCGTTAGCGAATTCTTCATGGACGAAGCGTGCCCGGGCGCTGTGTTTCGAAAGCTCTGGCTTGACGGCGGCCGAGGACGAGCCGTCGATCGACTTGTGGGAAATCGTCCTTGACCGTTAAAGCAGCATGATAACTCATATATATTGCAATCGAATATACACTACCTAAGTACGCAACAGGATCTCGGGAGGGTGTTCGCACAGCAAAAAAGATGTAGACGGCGTGGTATGGGATTAGTGAAACAGCATCCTCCACCGAGTTCAATCACTAACCAAGAAGTCAGTACGGGTGACAGGTGTGCGCACCACCCTAGTGACGGTGAAATTGTATGGCGCTCTAGAGCTCACCCGGCCACGCAATTTTTCGGGACCTTCAGTGAATAAGACACTATACGTAGCAAATATATTGTGGACGTTCTCGTGGATCGGCTACGTCTACAATTAGATGCCCTAAGCGGTGCTGTTGAGAAGACTGTTCCTTTCCCGTACTAAAATAAAGACTCCGAACTAGGAGGCTTATATAGCAATGCAAGGCTGAGTTTCAGGAGGGATGAACTCGGCCACCCATTATAAAAGATCTTCCCAGGTGCGCACGGTTAAATCCTACACATTATAAACATGGCAATTTGAGGTTTGCTTGACATGCCCTATGTACAGCG'
dna2 = 'GGTACCAGATACGCTAGCCTCTTGACTCTAACGCTTCTTACGTACATCTATTGATGGGTCATTATTTTAGGAATTCGCCCTGCTGGGCGGCGCCGTCCCAGTTTGTCGTCACCTTACTATCTCAGTCGCCGGACGGTGTAGTGCCCATTTTTCTGAGGCCACTCATTTGAGACCAGACCATCGCAGACTAGACTAGAAGGCAGTAATTAGGGCTTAAACGTTTCGATGCGTTCATGTGTGAAGTTGCCAATGTCGTATATGTGAATCCTTCGGGGCAAACCCTCGGGAATGCGCTGCATCTTTAATAGCCTGTCTGAAGGTTCTCCACTAAAATTATCGCGCTAGGAGCTTGCGTTTCACGGATTGATAGTGACCGCTCATTTATTCGGAGTTTATCTAGAATATTACGATTCGCACGGTCAGACCGGAAAAGCCTCTATCGAGGTAATCCCGTCAGGTCGAAAGTCCTGGGGGCAGTGGGATTGGATAGTTGGAAGATTTTCCTCGACCGCAATAACTGACAAATCAAGAAGTCCTACTTGGTGCCACTCGAGCGCTCCGCCCCATTCAGGTTCCGTTTATGCGCCCCTTTCAAAGTCTTCCGCGCAGCTAAAATGGTAGATACTTATGCTGTTAACACTCAATACGTTGCGTAAAACTCCTGTAGCGTCGTGGGTGTGGGCTACCAATAATACAAGACGCCCGAGTTGGTACTGGTGTCCTGGACCCGGTCTTCATGTCGAATACTAAAGACTCCCAACTATGCAACTGCTATAATACCTGAAGACAGTCTCTAAGGAAGTAAACAGGCAGTTACCCCACTCCAACTAACAATCCGCCTTGGCCCGGTTATAGGATGAATAGCACGCACCTGGTAGTTGGTGGTCGCATTTGCCAACCATATATAAACAC'

hamming = 0
for i in range(0,len(dna1)):
    if dna1[i] != dna2[i]:
        hamming = hamming + 1

print(hamming)