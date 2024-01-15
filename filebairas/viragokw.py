virágok=["rózsa","szegfű","liliom","nárcisz"]
darabszámok=[50,12,600,18]
g=open("v.txt","w",encoding="utf-8")
for i in range(0,len(virágok)):
    g.write(virágok[i]+":"+str(darabszámok[i])+"\n")
g.close()
