import matplotlib.pyplot as plt

sallary = [1000,1100,1110,1200,1300]
plt.plot(sallary,color='red')
plt.show()
plt.savefig('graf1.png')

names = ['Rafael','Joao','Maria','Ana','Lucia']

plt.figure(0)
plt.bar(names,sallary)
plt.show()
plt.savefig('graf2.png')


