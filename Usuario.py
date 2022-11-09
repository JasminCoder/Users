#hacer_retiro(self, amount): haz que este método reduzca el balance del usuario en la cantidad especificada 
#mostrar_balance_usuario(self): haz que este método imprima el nombre del usuario y el balance de cuenta en la terminal 
#Ej.: “Usuario: Guido van Rossum, Balance: $150
#BONUS: transfer_dinero(self, other_user, amount): haz que este método reduzca el balance del usuario por el monto 
#y agrega esa cantidad al balance de otro_usuario 


#Crea un archivo con la clase Usuario, incluyendo los métodos __init__ y hacer_depósito

#Agrega un método hacer_retiro a la clase Usuario

#Agrega un método mostrar_balance_usuario a la clase Usuario

#Crea 3 instancias de la clase Usuario

#Haz que el primer usuario haga 3 depósitos y 1 giro, y luego muestra sus balances

#Haz que el segundo usuario haga 2 depósitos y 2 giros, y luego muestra sus balances

#Haz que el tercer usuario haga 1 depósito y 3 giros, y luego muestra sus balances

#BONUS: Agrega un método transferir_dinero; haz que el primer usuario transfiera dinero al tercer usuario 
#y luego imprime los balances de ambos usuarios



# declarar una clase y darle el nombre Usuario
class Usuario:		
    def __init__(self, name, email, saldo):
        self.name = name
        self.email = email
        self.saldo = saldo


    def hacer_deposito(self, deposito):
        self.saldo += deposito
        return(self)
        

    def hacer_retiro(self, amount):
        self.saldo -= amount
        return(self)


    def mostrar_saldo(self):
        self.saldo
        print(f"El saldo de {self.name} es $ {self.saldo}")
        return(self)



    def transferir_dinero(self, amount, name_user):
        self.saldo -= amount
        name_user.saldo += amount
        return(self)
