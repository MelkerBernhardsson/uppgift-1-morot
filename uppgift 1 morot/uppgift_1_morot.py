
import random 

tt = random.randint(1,100) 
mt = random.randint(1,100) 

mor=1
tor=1

morot=(1/(tt+mt))*40
if morot*tt==20: #om det blir lika mellan dem kommer de behove dela pa sista moroten
    print("de kan inte dela pa sista moroten")
else :
    print("mor tid: ",mt,"\n")
    print("tor tid: ",tt,"\n")
    print("svar : tor",round(morot*tt),"\t mor",round(morot*mt))