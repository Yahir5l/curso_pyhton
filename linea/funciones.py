import mtplotlib.pyplot as plt

def calcular_Y(x:float, m:float, b:float)->float:
    
    return m * x + b
    
    
def test_linea():
    y = calcular_y(0.0,2.0,3.0)
    return y


def main():
    m = 2
    b = 3
    x = 5
    y = calcular_Y(x,m,b)
    print(f'Para x = {x}, y = {y}')
    
if __name__== '__main__':
    if test_linea()==3.0:
        print ("Prueba exitosa")
else:
        print ("Prueba fallida")

def grafica_linea(X:list, Y:list, m:float, b:float):
    plt.plot(X,Y)
    plt.title(f'Linea recta ')
