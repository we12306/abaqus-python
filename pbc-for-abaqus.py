# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 10:16:58 2020

@author: 26364
"""
'''
from abaqus import *
from abaqusConstants import *
import assembly

a = mdb.models['Renumber'].rootAssembly
for i in range(1,22):
	j = i+20
	k = 102-j
	a.SetFromNodeLabels(name='Node_'+str(j), nodeLabels=(('PART-1-1', (j, )), )) #创建Node集
	a.SetFromNodeLabels(name='Node_'+str(k), nodeLabels=(('PART-1-1', (k, )), ))
	mdb.models['Renumber'].Equation(name='E_'+str(j)+'-'+str(k), terms=((1.0, 'Node_'+str(j), 1), (-1.0, 
    'Node_'+str(k), 1))) #创建Equation
 
#创建上下边节点集 以及 方程约束（Equation)
for i in range(2,21):
	j = i
	k = 62-j
	a.SetFromNodeLabels(name='Node_'+str(j), nodeLabels=(('PART-1-1', (j, )), ))#创建Node集
	a.SetFromNodeLabels(name='Node_'+str(k), nodeLabels=(('PART-1-1', (k, )), ))
	mdb.models['Renumber'].Equation(name='E_'+str(j)+'-'+str(k), terms=((1.0, 'Node_'+str(j), 2), (-1.0, 
    'Node_'+str(k), 2))) #创建Equation
    
'''
from abaqus import *
from abaqusConstants import *
import assembly
#定义需要定义周期性边界条件的一对面上的节点集
node_x1=mdb.models['RVE'].rootAssembly.sets['Set-l2'].nodes
node_x2=mdb.models['RVE'].rootAssembly.sets['Set-l'].nodes
x1=[]
x2=[]
#在列表x1中记下x1节点的编号
for i in node_x1:
    x1.append(i.label)
#对node_x1中节点循环，在node_x2中查找跟node_x1中对应的节点，并保存到列表x2中，这里根据坐标来判断
for i in node_x1:
    for j in node_x2:
        if abs(j.coordinates[1]-i.coordinates[1])<0.2 and abs(j.coordinates[2]-i.coordinates[2])<0.2:
            x2.append(j.label)
for i in range(len(x1)):
    mdb.models['RVE'].rootAssembly.SetFromNodeLabels(name='set_x1_%03d'%(i),nodeLabels=(('RVE-1',(x1[i],),),),)
    mdb.models['RVE'].rootAssembly.SetFromNodeLabels(name='set_x2_%03d'%(i),nodeLabels=(('RVE-1',(x2[i],),),),)
    mdb.models['RVE'].Equation(name='Constraintx-%03d'%(i),terms=((-1.0,'set_x1_%03d'%(i),1),(1.0,'set_x2_%03d'%(i),1),(-1.0,'Set-rf1',1)))

