from flask import Flask, render_template
import numpy as np
from sympy import * 
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/rk_4to')
def rk_4to_front():
    difs
    return render_template('index.html')

@app.route('/rk_4to/<string:x1>/<string:y1>/<string:h>/<string:fun>/<string:xf>')
def rk_4to(x1,y1,h,fun,xf):
    x1 = float(x1)
    y1 = float(y1)
    h = float(h)
    xf = float(xf)
    f = lambda x,y: eval(fun)
    n = int((xf-x1)/h)
    ya= y1
    xa = x1
    xsol = [xa]
    ysol = [ya]
    k1 = 0
    k2 = 0
    i = 0
    
    for i in range(n):
        k1 = f(xa,ya)
        k2 = f(xa + ((1/2)*h), ya + ((1/2)*k1*h) )
        k3 = f(xa + ((1/2)*h), ya + ((1/2)*k2*h) )
        k4 = f(xa + h, ya + (k3*h))
        yn = ya + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        xa = xa + h
        ya = yn
        xsol.append(xa)
        ysol.append(yn)
        i += 1

    return ('La respuesta es ' + str(xsol) + ' y ' +  str(ysol))

def difs(lx,ly):
    if len(lx) == 2:
        return (ly[0]-ly[1])/(lx[0]-lx[1])
    else:
        return (difs(lx[1:],ly[1:]) - difs(lx[:-1],ly[:-1]))/(lx[-1] - lx[0])

@app.route('/interpolacion/<string:x1>/<string:lx>/<string:ly>')
def interpolacion(x1,lx,ly):
    lx = lx.split(",")
    ly = ly.split(",")
    lx = list(lx)
    ly = list(ly)
    
    for k,j,cont in zip(lx,ly,range(len(lx))):
        k = float(k)
        j = float(j)
        lx[cont] = k
        ly[cont] = j
        
    x1 = float(x1)
    result = 0
    aux = 0
    for i in range(len(lx)):
        if i != 0:  
            aux = lx[0]
            for j in range(i):
                aux *= (x1 - lx[j])
            result += aux * difs(lx[:(i+1)],ly[:(i+1)])
        else:
            result = ly[0]
    return ('La respuesta es ' + str(result))
    #return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)