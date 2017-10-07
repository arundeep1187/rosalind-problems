#Calculating Expected Offspring

h1 = 19045
h2 = 19541
h3 = 17845
h4 = 17222
h5 = 18875
h6 = 18716

OFFSPRING = 2

off1 = h1 * OFFSPRING
off2 = h2 * OFFSPRING
off3 = h3 * OFFSPRING
off4 = h4 * OFFSPRING * .75
off5 = h5 * OFFSPRING * .5
off6 = 0

expected = off1 + off2 + off3 + off4 + off5 + off6
print(expected)
