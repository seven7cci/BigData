nf = 1
ns = 1

for i in range(9):
    nf = nf + (nf * 0.05)
    ns = ns + (ns * 0.07)

print(nf, ns)