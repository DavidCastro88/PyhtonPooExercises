import math
class Main:
    def main():
        suma=0
        x=20
        y=40
        suma=suma+x
        x=x+math.pow(y,2)
        suma = suma + x/y
        print(f'El valor de la suma es {suma}')

if __name__ == "__main__":
    Main.main()