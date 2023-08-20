class Main:
    def main():
        horas=48
        salarioHora=5000
        porcentajeRetencion=0.125
        salarioBruto=horas*5000
        retencionFuente=salarioBruto*porcentajeRetencion
        salarioNeto = salarioBruto - retencionFuente
        print(f'Salario Bruto: ${salarioBruto}')
        print(f'Retención en la Fuente: ${retencionFuente}')
        print(f'Salario Neto: ${salarioNeto}')
        
if __name__ == "__main__":
    Main.main()
