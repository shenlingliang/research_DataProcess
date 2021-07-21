import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


values=["002","005","010"]
nums=[20,25,30,35]
marker=['r^--', 'bs-', 'go:','k+-.']
adder=[0,5,15]
x=[(i-10)/10 for i in range(21)]
for pos,i in enumerate(values):
    figTitle="f_"+i
    fig,axe=plt.subplots(1,1,figsize=(10,10))
    axe.set_title(figTitle)
    lineLst=[]
    for j in range(4):
        Lambda=nums[j]+adder[pos]
        path="/Users/shenll1997/Desktop/ResearchProject/results/fig2/fg2_lambda_0"+str(Lambda)+"_f_"+i+".txt"
        file =open(path)
        file.readline()
        file.readline()
        file.readline()
        R=[0.0]*21
        for k in range(1000):
            for z in range(21):
                tmp=file.readline().split("\t")
                R[z]+=int(tmp[3])/1000
        for z in range(21):
            R[z]=R[z]/5000
        l1,=axe.plot(x,R,marker[j])
        axe.set_xlabel("alpha")
        axe.set_ylabel("R(∞)")
        lineLst.append(l1)
    axe.legend(handles=[lineLst[0], lineLst[1], lineLst[2],lineLst[3]], labels=["lambda="+str((nums[0]+adder[pos])/100), "lambda="+str((nums[1]+adder[pos])/100), "lambda="+str((nums[2]+adder[pos])/100),"lambda="+str((nums[3]+adder[pos])/100)],loc='best')
    plt.show()

        