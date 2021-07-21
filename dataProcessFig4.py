# path="/Users/shenll1997/Desktop/ResearchProject/results/fig4/fg4_lambda_020_f_002.txt"
# file=open(path)
# tmp=file.readline().split("\t")
# print(len(tmp))
import matplotlib.pyplot as plt
import matplotlib
import copy
lst=[]
length=401
tmplist=[0]*length
rounds=20

lambdas=[20,25,35]
adder=[0,5,20]
values=["002","005","010"]
# marker=['r^--', 'bs-', 'go:']
x=[(i-200)/200 for i in range(401)]


for pos,k in enumerate(values):
    for z in lambdas:
        figTitle="lambda ="+str(z+adder[pos])+" f="+k
        fig,axe=plt.subplots(1,1,figsize=(10,10))
        
        
        path="/Users/shenll1997/Desktop/ResearchProject1/results/fig4/fg4_lambda_0"+str(z+adder[pos])+"_f_"+k+".txt"
        file=open(path)
        lst=[]
        for i in range(length):
            lst.append(copy.deepcopy(tmplist))
        for i in range(rounds):
            for j in range(length):
                tmp=file.readline().split("\t")
                for t in range(length):
                    lst[j][t]+=int(tmp[t])/(rounds*5000)
        p=axe.pcolor(x,x,lst,cmap=matplotlib.cm.RdYlBu,vmin=0,vmax=1)
        axe.set_xlabel("alpha")
        axe.set_ylabel("beta")
        plt.title(figTitle)
        cb=fig.colorbar(p,ax=axe)
        plt.show()   

