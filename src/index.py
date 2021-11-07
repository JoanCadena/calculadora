from flask import Flask, render_template
import numpy as np
from sympy import * 
#import matplotlib.pyplot as plt

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rk_4to')
def rk_4to_front():
    return render_template('rk_4to.html')

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

    return ('Xsol = ' + str(xsol) + '\n' + 'Ysol = ' + str(ysol))

@app.route('/interpolacion')
def interpolacion_front():
    return render_template('interpolacion.html')

def difs(lx,ly):
    if len(lx) == 2:
        return (ly[0]-ly[1])/(lx[0]-lx[1])
    else:
        return (difs(lx[1:],ly[1:]) - difs(lx[:-1],ly[:-1]))/(lx[-1] - lx[0])

@app.route('/interpolacion/<string:x1>/<string:lx>/<string:ly>')
def interpolacion(x1,lx,ly):

    x1 = x1.split(",")
    x1 = list(x1)
    lx = lx.split(",")
    ly = ly.split(",")
    lx = list(lx)
    ly = list(ly)
    for z in range(len(x1)):
        x1[z] = float(x1[z])

    resX = []

    for xfinal in x1:
        
        for k,j,cont in zip(lx,ly,range(len(lx))):
            k = float(k)
            j = float(j)
            lx[cont] = k
            ly[cont] = j
        

        result = 0
        aux = 0
        for i in range(len(lx)):
            if i != 0:  
                aux = lx[0]
                for j in range(i):
                    aux *= (xfinal - lx[j])
                result += aux * difs(lx[:(i+1)],ly[:(i+1)])
            else:
                result = ly[0]

        resX.append(result)

            
    return ('La respuesta es ' + '\n' + str(resX))
    #return render_template('prueba.html')

if __name__ == '__main__':
    app.run(debug=True)