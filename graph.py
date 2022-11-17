import matplotlib.pyplot as plt
import math

f = open('run.txt', 'r') # abre o arquivo com modo read
text = f.readlines() # transforma linhas em lista

# init listas
x = []
y = []
dist = []
timesqrt = []

# listas com o intuito de dividir dist/tsqrt em x para facilitar a visualizacao da progressao grafica
dist_divide = []
timesqrt_divide = []

# variavel com posiçao inicial
originx = float(text[0].split('/')[0])
originy = float(text[0].split('/')[1])

for i in range(len(text)): # for em cada linha
    sptxt = text[i].split('/') # split / (separando x e y)
    xval = float(sptxt[0]) # get x
    yval = float(sptxt[1]) # get y
    x.append(xval) # store x
    y.append(yval) # store y

    timesqrt.append(math.sqrt(i+1)) # store raiz quadrada de tempo (representado pelo n linha)
    if i==0: dist.append(0) # se i==0, x e y estarao na origem, portanto dist = 0
    else:
        targetx = xval # get x para calculo dist
        targety = yval # get y para calculo dist
        dx = targetx-originx
        dy = targety-originy
        distval = math.sqrt(dx*dx+dy*dy) # calculo dist
        dist.append(distval) # store dist da origem

for i in range(0,len(dist),75): # pegar valor de dist a cada n valores, nesse caso n=75
    dist_divide.append(dist[i])
    timesqrt_divide.append(timesqrt[i])
 # pegar o ultimo valor de dist para deixar os dois graficos com o mesmo tamanho
dist_divide.append(dist[len(dist)-1])
timesqrt_divide.append(timesqrt[len(dist)-1])

# grafico caminho da bola grande
plt.plot(x, y, 'r')
plt.ylim(0, 1)
plt.xlim(0, 1)
plt.show()

# grafico relacao timesqrt dist
plt.plot(timesqrt,dist,'b')
plt.plot(timesqrt_divide,dist_divide,'b--')
plt.show()