from fastapi import FastAPI, HTTPException #Importamos FastAPI para crear la aplicación web y HTTPException para manejar errores de manera adecuada
from banco import CuentaBancaria
from banco import CuentaDeAhorros
#Importamos la clase CuentaBancaria desde el archivo banco.py

#1-Creamos al guardia (la aplicación FastAPI)
app = FastAPI(
    title="API de Cuenta Bancaria", #Título de la API
    description= "Una API real para gestionar cuentas bancarias usando POO",
    version="1.0.0"#Versión de la API
) 

#2-Creamos una cuenta bancaria de ejemplo para probar la API
mi_cuenta = CuentaBancaria(titular="Juan Perez", saldo_inicial=1000.0)

mi_cuenta_ahorros = CuentaDeAhorros(titular = "Juan Perez", saldo_inicial = 0.0, tasa_interes = 0.05)



#3-Hacemos la primera ruta: ver ele saldo 
@app.get("/saldo") #Definimos la ruta para obtener el saldo
def ver_saldo():
    """Ruta para consultar el saldo disponible en la cuenta bancaria""" #Docstring para explicar qué hace esta ruta
    try:
        saldo = mi_cuenta.obtener_saldo() #Obtenemos el saldo usando el método de la clase CuentaBancaria
        return {"saldo": saldo} #Devolvemos el saldo en formato JSON
    except Exception as e: #Si ocurre cualquier error, lo capturamos
        raise HTTPException(status_code=500, detail=str(e)) #Lanzamos una excepción HTTP con el mensaje de error// que es loq ue hace raise HTTPException es que FastAPI se encarga de convertirlo en una respuesta HTTP adecuada, con el código de estado y el mensaje de error en formato JSON


#4-Hacemos la segunda ruta: depositar dinero
@app.post("/depositar") #Definimos la ruta para depositar dinero
def depositar_dinero(monto: float): #Definimos la función que maneja esta ruta, con un parámetro monto que es un número flotante
    """Ruta para depositar dinero en la cuenta bancaria""" #Docstring para explicar qué hace esta ruta
    try:
        resultado = mi_cuenta.depositar(monto) #Intentamos depositar el monto usando el método de la clase CuentaBancaria
        return {"mensaje": resultado} #Devolvemos un mensaje de éxito en formato JSON
    except ValueError as ve: #Si ocurre un error de valor (como monto negativo), lo capturamos
        raise HTTPException(status_code=400, detail=str(ve)) #Lanzamos una excepción HTTP con el mensaje de error y un código de estado 400 (Bad Request)
    except Exception as e: #Si ocurre cualquier otro error, lo capturamos
        raise HTTPException(status_code=500, detail=str(e)) #Lanzamos una excepción HTTP con el mensaje de error y un código de estado 500 (Internal Server Error)
    

#5-Hacemos la tercera ruta: retirar dinero
@app.post("/retirar") #Definimos la ruta para retirar dinero
def retirar_dinero(monto: float): #Definimos la función que maneja
    """Ruta para retirar dinero de la cuenta bancaria""" #Docstring para explicar qué hace esta ruta
    try:
        resultado = mi_cuenta.retirar(monto) #Intentamos retirar el monto usando el método de la clase CuentaBancaria
        return {"mensaje": resultado} #Devolvemos un mensaje de éxito en formato JSON
    except ValueError as ve: #Si ocurre un error de valor (como monto negativo o fondos insuficientes), lo capturamos
        raise HTTPException(status_code=400, detail=str(ve)) #Lanzamos una excepción HTTP con el mensaje de error y un código de estado 400 (Bad Request)
    except Exception as e: #Si ocurre cualquier otro error, lo capturamos
        raise HTTPException(status_code=500, detail=str(e)) #Lanzamos una excepción HTTP con el mensaje de error y un código de estado 500 (Internal Server Error)


#Creo las rutas nuevas para poder implementar mi cuentta de ahorros
@app.get("/saldo_ahorros")#Definimos la ruta para obtener el saldo de la cuenta de ahorros
def ver_saldo_ahorro():
    """Ruta para construir el saldo disponible"""
    try:
        saldo = mi_cuenta_ahorros.obtener_saldo() 
        return {"saldo_ahorros": saldo} #Devolvemos el saldo de la cuenta de ahorros en formato JSON
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#algo a no olvidar cuando pedimos que muestre el saldo tanto de la cuenta noraml como la de ahorros usamos get en esta nada mas por que como sunombre queremos que nos de algo un vlaor en este caso el salgo y por eso el resto es post por que nosotros le damos un valor 
@app.post("/depositar_ahorros")
def depositar_dinero_ahorros(monto: float):
    """ruta para depositar a la cuenta de ahorros"""
    try:
        resultado = mi_cuenta_ahorros.depositar(monto)
        return {"mensaje": resultado}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/retirar_ahorros")
def retirar_dinero_ahorros(monto: float):
    """ruta para retirar de la cuenta de ahorros"""
    try:
        resultado = mi_cuenta_ahorros.retirar_ahorros(monto)
        return {"mensaje": resultado}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/aplicar_interes")
def aplicar_interes_ahorros():
    """ruta para aplicar intereses a la cuenta de ahorros"""
    try:
        resultado = mi_cuenta_ahorros.aplicar_interes()
        return {"mensaje": resultado}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
