#Aplicativo Converte Dolar/Real - Real/Dolar - 31-07-2017 atualizado para versão 31/03/2021


#Valor cotação dolar de 31/07
Vd1=5.5
#Valor a converter

print ("Convertendo Valor de Real para Dolar")
Vconv=float(input("Qual valor em Real R$ "))
#print("%.2f" % (Vconv/Vd1))
print("%.2f" % (Vconv/Vd1))
#print ("Valor em Dolar $ "), ("%.2f" % (Vconv/Vd1))


print ("Convertendo Valor de Dolar para Real")
Vconv=float(input("Qual valor em Dolar $ "))
print("%.2f" % (Vconv*Vd1))
#print ("Valor em Real R$ "), ("%.2f" % (Vconv*Vd1))

exit()
