import matplotlib.pyplot as plt

#  saldos e meses
meses = ['Maio', 'Junho', 'Julho']
pessoa1 = [10450, 15000, 18000]
pessoa2 = [11000, 7000, 9000]
pessoa3 = [15000, 12000, 13000]
pessoa4 = [20000, 21000, 19000]

# Calculando 
total_pessoa1 = sum(pessoa1)
total_pessoa2 = sum(pessoa2)
total_pessoa3 = sum(pessoa3)
total_pessoa4 = sum(pessoa4)
# valores totais no term
print(f"Total Marllon: R${total_pessoa1}")
print(f"Total Maycon: R${total_pessoa2}")
print(f"Total Marcone: R${total_pessoa3}")
print(f"Total Mônica: R${total_pessoa4}")
plt.plot(meses, pessoa1, label='Marllon')
plt.plot(meses, pessoa2, label='Maycon')
plt.plot(meses, pessoa3, label='Marcone')
plt.plot(meses, pessoa4, label='Mônica')
# títulos
plt.title('SALDO')
plt.xlabel('MESES')
plt.ylabel('SALDO EM R$')
# cor
fig = plt.gcf()
fig.set_facecolor('lightyellow')
# Mostrando janela
plt.legend()
plt.show()

