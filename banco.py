class CuentaBancaria: ##Creo el objeto padre de las cuentas bancarias
    def __init__(self, titular: str, saldo_inicial: float =0.0): # con type hints le decimos que el titular es un string y el saldo inicial es un numero flotante, ademas le damos un valor por defecto de 0.0
        self.titular = titular
        #al poonele dos guiones bajos el saldo es privado no se puede editar fuera de esta clase osea lo encapsulamos 
        self.__saldo = saldo_inicial

#Metodos para interactuar de forma segura con el saldo 
    def obtener_saldo(self) -> float:  # el (self) es por que pedimos datos a la clase CuentaBancaria y le decimos que el resultado va a ser un numero float
        """devuelve le saldo actual de forma segura""" #el docstring es para explicar que hace la funcion con fastapi
        return self.__saldo #aqui devolvemos el saldo actual
    
    def depositar(self, monto: float) -> None: #le decimos que el monto es un numero flotante y que no devuelve nada
        """agrega el monto al saldo de forma segura""" # el doctringes para explicar qie hace la funciion con fastapi
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo") #si el monto es menor o igual a 0 se lanza un error
        self.__saldo += monto #aqui se suma el monto al saldo actual  
        return f"Depósito exitoso. Nuevo saldo: {self.__saldo}" #aqui devolvemos un mensaje de que el deposito fue exitoso y el nuevo saldo
    
    def retirar(self, monto: float) -> None: #le decimos que el monto es un numero flotante y que no devuelve nada
        """resta el monto retirado de saldo de forma segura""" #el docstring es para explicar que hace la funcion con fastapi
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo") #si el monto es menor o igual a 0 se lanza un error// podemos tirar errores sin necesidad de usar try except gracias a fastapi
        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes para retirar") #si el monto es mayor al saldo se lanza un error
        self.__saldo -= monto #aqui se resta el monto al saldo actual
        return f"Retiro exitoso. Nuevo saldo: {self.__saldo}" #aqui devolvemos un mensaje de que el retiro fue exitoso y el nuevo saldo


class CuentaDeAhorros(CuentaBancaria): #Creao la clase hija de cuenta bancaria que seria cuenta corriente y depsues la vista de ahorros cuenta de ahorros hereda de cuenta bancaria
    def __init__(self, titular:str, saldo_inicial: float =0.0, tasa_interes: float =0.01): #le decimos que el titular es un string el saldo inicial es un numero float equivalente a 0.0 y la tasa de interes es un numero float equivalente a 0.1 
        super().__init__(titular, saldo_inicial) #aqui llamamos al constructor de la clase padre para inicializar el titular y el saldo
        self.tasa_interes = tasa_interes # aqui inciamos la tasa de interes que es un atributo adicional de la clase hija


    def calcular_interes(self) -> float: #le decimos que el resultado de esta funcion va a ser un numero float
        """calcula el interes acumulado basado en el saldo actual y la tasa de interes""" #el docstring es para explicar que hace la funcion con fastapi
        interes = self.obtener_saldo() * self.tasa_interes #aqui calculamos el interes multiplicando el saldo actual por la tasa de interes
        return interes #aqui devolvemos el interes calculado"""
        
        
    def aplica_interes(self) -> str:
        """aplica el interes acumulado al saldo """
        interes = self.calcular_interes()
        self.depositar(interes) ##aplicamos el interes 
        return f"interes apicado exitosamente. Nuevo saldo: {self.obtener_saldo()}"
    

    def retirar_ahorros(self, monto: float) -> None:
        """retira dinero de la cuenta de ahorros pero nos quedamos con el interes """
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0") #si el monto es menor o igual a 0 se lanza un error
        if monto > self.obtener_saldo():
            raise ValueError("Fondos insuficientes para retirar")
        return super().retirar(monto) #aqui llamamos al metodo retirar de la clase padre para retirar el monto pero sin afectar el interes acumulado


    def depositar_ahorros(self, monto: float) -> None:
        """depositar dinero en la cuenta de ahorros pero sin afectar el interes acumulado"""
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a 0") #si el monto es menor o igual a 0 se lanza un error
        return super().depositar(monto) #aqui llamamos al metodo depositar de la clase padre para depositar el monto pero sin afectar el interes acumulado

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular: str, saldo_inicial: float=0.0, sobre_giro: float=0.0)-> None:
        super().__init__(titular , saldo_inicial)
        self.sobre_giro = sobre_giro #aqui agregamos el sobregiro correspondiente a la logica de comofunciona una cuenta correinte

    

#Metodos para interactuar de forma segura con el saldo 
    def obtener_saldo(self) -> float:  # el (self) es por que pedimos datos a la clase CuentaBancaria y le decimos que el resultado va a ser un numero float
        """devuelve le saldo actual de forma segura""" #el docstring es para explicar que hace la funcion con fastapi
        return self.__saldo #aqui devolvemos el saldo actual
    
    def depositar(self, monto: float) -> None: #le decimos que el monto es un numero flotante y que no devuelve nada
        """agrega el monto al saldo de forma segura""" # el doctringes para explicar qie hace la funciion con fastapi
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo") #si el monto es menor o igual a 0 se lanza un error
        self.__saldo += monto #aqui se suma el monto al saldo actual  
        return f"Depósito exitoso. Nuevo saldo: {self.__saldo}" #aqui devolvemos un mensaje de que el deposito fue exitoso y el nuevo saldo
    
    def retirar(self, monto: float) -> None: #le decimos que el monto es un numero flotante y que no devuelve nada
        """resta el monto retirado de saldo de forma segura""" #el docstring es para explicar que hace la funcion con fastapi
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo") #si el monto es menor o igual a 0 se lanza un error// podemos tirar errores sin necesidad de usar try except gracias a fastapi
        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes para retirar") #si el monto es mayor al saldo se lanza un error
        self.__saldo -= monto #aqui se resta el monto al saldo actual
        return f"Retiro exitoso. Nuevo saldo: {self.__saldo}" #aqui devolvemos un mensaje de que el retiro fue exitoso y el nuevo saldo


class CuentaDeAhorros(CuentaBancaria): #Creao la clase hija de cuenta bancaria que seria cuenta corriente y depsues la vista de ahorros cuenta de ahorros hereda de cuenta bancaria
    def __init__(self, titular:str, saldo_inicial: float =0.0, tasa_interes: float =0.01): #le decimos que el titular es un string el saldo inicial es un numero float equivalente a 0.0 y la tasa de interes es un numero float equivalente a 0.1 
        super().__init__(titular, saldo_inicial) #aqui llamamos al constructor de la clase padre para inicializar el titular y el saldo
        self.tasa_interes = tasa_interes # aqui inciamos la tasa de interes que es un atributo adicional de la clase hija


    def calcular_interes(self) -> float: #le decimos que el resultado de esta funcion va a ser un numero float
        """calcula el interes acumulado basado en el saldo actual y la tasa de interes""" #el docstring es para explicar que hace la funcion con fastapi
        interes = self.obtener_saldo() * self.tasa_interes #aqui calculamos el interes multiplicando el saldo actual por la tasa de interes
        return interes #aqui devolvemos el interes calculado"""
        
        
    def aplica_interes(self) -> str:
        """aplica el interes acumulado al saldo """
        interes = self.calcular_interes()
        self.depositar(interes) ##aplicamos el interes 
        return f"interes apicado exitosamente. Nuevo saldo: {self.obtener_saldo()}"
    

    def retirar_ahorros(self, monto: float) -> None:
        """retira dinero de la cuenta de ahorros pero nos quedamos con el interes """
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0") #si el monto es menor o igual a 0 se lanza un error
        if monto > self.obtener_saldo():
            raise ValueError("Fondos insuficientes para retirar")
        return super().retirar(monto) #aqui llamamos al metodo retirar de la clase padre para retirar el monto pero sin afectar el interes acumulado


    def depositar_ahorros(self, monto: float) -> None:
        """depositar dinero en la cuenta de ahorros pero sin afectar el interes acumulado"""
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a 0") #si el monto es menor o igual a 0 se lanza un error
        return super().depositar(monto) #aqui llamamos al metodo depositar de la clase padre para depositar el monto pero sin afectar el interes acumulado

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular: str, saldo_inicial: float=0.0, sobre_giro: float=0.0)-> None:
        super().__init__(titular , saldo_inicial)
        self.sobre_giro = sobre_giro #aqui agregamos el sobregiro correspondiente a la logica de comofunciona una cuenta correinte

    def retirar_sobregiro(self , monto: float)-> None:
        """Version especial para la cuenta corriente"""
        saldo_actual = self.obtener_saldo()
        saldo_final = saldo_actual - monto
        
        
        
        if monto < -0:
            raise ValueError(f"no puedes pasar de el tope de el sobregiro, ${self.sobre_giro}")
        if saldo_actual < -self.sobre_giro:
            raise ValueError(f"supera el limite de sobregiro de ${self.sobre_giro}")
        return super().retirar(monto)
        

        