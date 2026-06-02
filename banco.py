class CuentaBancaria: ##Creo el objeto padre de las cuentas bancarias
    def __init__(self, titular: str, saldo_inicial: float =0.0): # con type hints le decimos que el titular es un string y el saldo inicial es un numero flotante, ademas le damos un valor por defecto de 0.0
        self.titular = titular
        #al poonele dos guiones bajos el saldo es privado no se puede editar fuera de esta clase osea lo encapsulamos 
        self.saldo = saldo_inicial

#Metodos para interactuar de forma segura con el saldo 
    def obtener_saldo(self) -> float:  # el (self) es por que pedimos datos a la clase CuentaBancaria y le decimos que el resultado va a ser un numero float
        """devuelve le saldo actual de forma segura""" #el docstring es para explicar que hace la funcion con fastapi
        return self.saldo #aqui devolvemos el saldo actual
    
    def depositar(self, monto: float) -> None: #le decimos que el monto es un numero flotante y que no devuelve nada
        """agrega el monto al saldo de forma segura""" # el doctringes para explicar qie hace la funciion con fastapi
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo") #si el monto es menor o igual a 0 se lanza un error
        self.saldo += monto #aqui se suma el monto al saldo actual  
        return f"Depósito exitoso. Nuevo saldo: {self.saldo}" #aqui devolvemos un mensaje de que el deposito fue exitoso y el nuevo saldo
    
    def retirar(self, monto: float) -> None: #le decimos que el monto es un numero flotante y que no devuelve nada
        """resta el monto retirado de saldo de forma segura""" #el docstring es para explicar que hace la funcion con fastapi
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo") #si el monto es menor o igual a 0 se lanza un error// podemos tirar errores sin necesidad de usar try except gracias a fastapi
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes para retirar") #si el monto es mayor al saldo se lanza un error
        self.saldo -= monto #aqui se resta el monto al saldo actual
        return f"Retiro exitoso. Nuevo saldo: {self.saldo}" #aqui devolvemos un mensaje de que el retiro fue exitoso y el nuevo saldo
    



