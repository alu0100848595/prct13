#! encoding: UTF-8
import time
import timeit
import modulo
import sys
import matplotlib.pyplot as pl

def error(nro_intervalos,nro_test,umbral):
  fallos=0
  for i in range (nro_test):
    m=modulo.aproxpi(nro_intervalos)
    error=abs(m-modulo.pi)
    if error>=umbral:
      fallos=fallos+1
  return ((fallos/nro_test)*100)  
  
x=[]
y=[]
for j in range(10):
 #start=time.time()
 #if (len(sys.argv)==4):
 p1=10
 p2=10
 p3=float(raw_input("introduzca el valor del umbral:"))
 s=error(p1,p2,p3)
 print "El porcentaje de error es de: %5.3f" %s
 x=x+[p3]
 y=y+[s]
pl.plot(x,y)
pl.show()
pl.savefig("secons.eps", dpi=72)