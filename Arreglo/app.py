## Importamos flask
from flask import Flask
import numpy as np
app=Flask(__name__)
## Importamos la libreria numpy
## si no existe la instalamos con:
## pip install numpy

@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos (valores=0,columnas=0,filas=0):
    if filas==0:
        arreglo=np.random.randint(valores,size=columnas)
    else:
        arreglo=np.random.randint(valores,size=(filas,columnas))
        
    return f"El arreglo aleatorio es : {arreglo}"

if __name__=='__main__':
    ## El valor True indica que la app se deja
    ## en modo debug
    app.run(debug=True)
    
    