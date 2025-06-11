while True:
    
    primeiroValor = int(input("digite um numero de 0 a 10: "))
    segundoValor = int(input("digite um numero de 0 a 10: "))
    if 0 <= primeiroValor <= 10 and 0 <= segundoValor <= 10:
        print(f"A subtraçãos entre os numeros {primeiroValor} e {segundoValor} é {primeiroValor - segundoValor}")
        break
    print("digite um numero entre 0 e 10, digite novamente")
