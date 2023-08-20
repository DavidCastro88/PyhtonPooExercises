class Main:
    def main():
        edadJuan = float(input('Hola Juan, ingresa tu edad: '))
        edadAna=4*(edadJuan/3)
        edadAlberto=2*(edadJuan/3)
        edadMama = edadJuan + edadAna + edadAlberto
        print(f'Edad de Juan: {edadJuan}')
        print(f'Edad de Ana: {edadAna}')
        print(f'Edad de Alberto: {edadAlberto}')
        print(f'Edad de Mamá: {edadMama}')

if __name__ == "__main__":
    Main.main()