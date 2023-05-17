def somaImposto(taxaImposto,custo):
    imposto = custo * (taxaImposto/100)
    custo+=imposto
    return custo

def valorPagamento(valor_prestacao,dias_atraso):
    if dias_atraso == 0:
        return valor_prestacao
    else:
        multa = valor_prestacao * 0.03
        juros = valor_prestacao * (0.001 * dias_atraso)
        valor_total = valor_prestacao + multa + juros
        return  valor_total

def main():
    valor_prestacao = float(input("Digite o valor da prestação: "))
    dias_atraso = int(input("Digite o numero de dias em atraso: "))
    valor_final = valorPagamento(valor_prestacao,dias_atraso)
    print("O valor a ser pago é: ", valor_final)
   

if __name__ == "__main__":
    main()