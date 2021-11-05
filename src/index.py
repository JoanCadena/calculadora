from flask import Flask, render_template
import numpy as np
from sympy import * 
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/interpolacion')
def interpolacion():
    return render_template('index.html')

@app.route('/rk_4to')
def rk_4to_front():
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
    print(xsol,ysol)

    #return xsol, ysol
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)