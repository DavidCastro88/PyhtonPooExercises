import math
class Main:
    def main():
        radio = float(input('Ingrese el radio del circulo: '))
        print(f'El area del circulo es: {round((math.pi*(math.pow(radio,2))),3)}')
        print(f'La longitud de la circunferencia es: {round((2*math.pi*radio),3)}')
        
if __name__ == "__main__":
    Main.main()