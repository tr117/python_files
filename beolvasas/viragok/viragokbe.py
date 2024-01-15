#A v.txt nevű, utf-8 kódolású fájlból beolvasunk egy csokrok listába
csokrok=[]
u=open("v.txt","r",encoding="utf-8")
for sor in u:
    csokor=sor[:-1].split(":")
    csokrok.append(csokor)
u.close()
