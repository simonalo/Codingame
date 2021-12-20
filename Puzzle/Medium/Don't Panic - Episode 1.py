o=input
p=int
q=print
a,_,_,_,b,_,_,c=map(p,o().split())
m=[b]*a
for i in range(c):
 d,e=map(p,o().split())
 m[d]=e
while 1:
 f,g,h=o().split()
 f=p(f)
 g=p(g)
 q("BLOCK" if g<m[f] and h=="LEFT" or g>m[f] and h=="RIGHT" else "WAIT")