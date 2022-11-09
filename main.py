from Usuario import Usuario

#Crea 3 instancias de la clase Usuario
elena = Usuario("Elena", "elena@dojo.com", 500)
renata = Usuario("Renata", "renata@dojo.com", 7000)
catalina = Usuario("Catalina", "catalina@dojo", 4000)


#Haz que el primer usuario haga 3 depósitos y 1 giro, y luego muestra sus balances
elena.hacer_deposito(10000).hacer_deposito(7500).hacer_deposito(20000).hacer_retiro(15000).mostrar_saldo() #23000


#Haz que el segundo usuario haga 2 depósitos y 2 giros, y luego muestra sus balances
renata.hacer_deposito(8000).hacer_deposito(5000).hacer_retiro(5000).hacer_retiro(3000).mostrar_saldo() #12000


#Haz que el tercer usuario haga 1 depósito y 3 giros, y luego muestra sus balances
catalina.hacer_deposito(30000).hacer_retiro(10000).hacer_retiro(9000).hacer_retiro(5000).mostrar_saldo() #10000


#Agrega un método transferir_dinero; haz que el primer usuario transfiera dinero al tercer usuario 
#y luego imprime los balances de ambos usuarios
elena.transferir_dinero(5000, catalina)

print(elena.mostrar_saldo()) #18000
print(catalina.mostrar_saldo()) #15000

