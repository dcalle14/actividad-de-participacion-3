class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, monto):
        self.balance += monto
        print(f"Se depositaron {monto} unidades. Nuevo balance: {self.balance}")