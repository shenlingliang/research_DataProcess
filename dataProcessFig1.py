import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
values=["n05","0","05"]
nums=[-0.5,0.0,0.5]
markerLst_R = ['r^--', 'bs-', 'go:'] 
markerLst_D = ['r--', 'b-', 'g:']
for b in values:
    figTitle="fig1_beta="+b+"_f_005"
    fig ,axe =plt.subplots(2,1,figsize=(10,20))
    axe[0].set_title(figTitle+" R")
    axe[1].set_title(figTitle+" D")
    lineLst_R=[]
    lineLst_D=[]
    x=[i/100 for i in range(101)]
    for pos,a in enumerate(values):
        path="/Users/shenll1997/Desktop/ResearchProject/results/fig1/fg1__alpha_"+a+"_beta_"+b+"_f_005.txt"
        file=open(path)
        file.readline()
        file.readline()
        file.readline()
        R=[0.0]*101
        D=[0.0]*101
        # 数据处理
        for i in range(1000):
            for j in range(101):
                tmp=file.readline().split("\t")
                R[j]=R[j]+int(tmp[2])
                D[j]=D[j]+int(tmp[2])**2
        # 画图
        for i in range(101):
            R[i]=R[i]/1000
            D[i]=D[i]/1000
            D[i]=math.sqrt(D[i]-R[i]**2)/R[i]
            R[i]=R[i]/5000
        l1,=axe[0].plot(x,R,markerLst_R[pos])
        axe[0].set_xlabel("infectRate")
        axe[0].set_ylabel("R")
        l2,=axe[1].plot(x,D,markerLst_D[pos])
        axe[1].set_xlabel("infectRate")
        axe[1].set_ylabel("D")
        lineLst_R.append(l1)
        lineLst_D.append(l2)
    axe[0].legend(handles=[lineLst_R[0], lineLst_R[1], lineLst_R[2]], labels=['a=-0.5', 'a=0', 'a=0.5'],
                             loc='best')  # todo
    axe[1].legend(handles=[lineLst_D[0], lineLst_D[1], lineLst_D[2]], labels=['a=-0.5', 'a=0', 'a=0.5'],
                              loc='best')
    plt.show()
    fig.save_fig=(figTitle+".jpg")




