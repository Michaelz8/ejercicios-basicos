## Importamos flask
from flask import Flask
##import math
app=Flask(__name__)

## Definimos la ruta principal
@app.route("/")
def area():
    return "<h1> Cálculo de áreas </h1><hr>"

## Ruta para el cálculo de área del círculo 
@app.route("/circulo/<int:r>")
def area_cir(r=0,pi=0):
    A_cir=3.1416*r**2
    return f"<h1>El área del círculo es : {A_cir}</h1> <hr>"

## Ruta para el cálculo de área del cuadrado triángulo 
@app.route("/cuadrado/<int:b1>/<int:a1>")
def area_cua(b1=0,a1=0):
    A_cua=a1*b1
    return f"<h1>El área del cuadrado es : {A_cua}</h1> <hr>"

## Ruta para el cálculo de área del triángulo 
@app.route("/triangulo/<int:b2>/<int:a2>")
def area_tri(b2=0,a2=0):
    A_tri=(a2*b2)/2
    return f"<h1>El área del triángulo es : {A_tri}</h1> <hr>"

if __name__ == '__main__':
    ## El valor True indica que la app se dejo en modo debug
    app.run(debug=True)
    
    

