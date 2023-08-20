import math
class Main:
    def main():
        numero = float(input('Ingrese un número: '))
        print(f'El cuadrado de {numero} es {math.pow(numero,2)}')
        print(f'El cubo de {numero} es {math.pow(numero,3)}')
        
if __name__ == "__main__":
    Main.main()