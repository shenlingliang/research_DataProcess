import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

values=["n01","0","01"]
poss=[-1,0,1]
nums=["030","060","090"]
marker=['r^--', 'bs-', 'go:']
x=[i/100 for i in range(101)]
for p,i in enumerate(values):
    figTitle="alpha&beta="+str(poss[p])
    fig,axe=plt.subplots(1,1,figsize=(10,10))
    axe.set_title(figTitle)
    lineLst=[]
    for pos,j in enumerate(nums):
        path="/Users/shenll1997/Desktop/ResearchProject/results/fig5/fg5_lambda_"+j+"_"+i+".txt"
        file=open(path)
        file.readline()
        file.readline()
        R=[0]*101
        for k in range(1000):
            for z in range(101):
                tmp=file.readline().split("\t")
                R[z]+=int(tmp[2])/1000
                file.readline()
                file.readline()
        for z in range(101):
            R[z]/=5000
        l1,=axe.plot(x,R,marker[pos])
        axe.set_xlabel("threshold")
        axe.set_ylabel("R(∞)")
        lineLst.append(l1)
    axe.legend(handles=[lineLst[0], lineLst[1], lineLst[2]], labels=["lambda="+str(0.3), "lambda="+str(0.6), "lambda="+str(0.9)],loc='best')
    plt.show()