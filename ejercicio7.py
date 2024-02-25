class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

cuenta1 = CuentaBancaria("123456789", ["Juan", "María"], 1000.0)
print("Número de cuenta:", cuenta1.numero_cuenta)
print("Propietarios:", cuenta1.propietarios)
print("Balance:", cuenta1.balance)