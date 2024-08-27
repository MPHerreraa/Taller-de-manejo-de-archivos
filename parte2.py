f = open("nombres.txt")
g = open("lalala.txt", "w") 

texto = f.read()
g.write(texto)

f.close()
g.close()