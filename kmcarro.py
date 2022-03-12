def iniciar():
    print("Para chegar em Toquio voce precisa de 30 litros de gasolina")

    valor_do_litro = float(5)

    dinheiro = float(input("Quanto de dinheiro você tem ? "))

    litroscomprados = dinheiro / valor_do_litro
    km_comprados =  20 * litroscomprados

    if(km_comprados >= 70):
        print("Você consegue, Litros comprados: ", litroscomprados, " Km rodados vai ser de: ", km_comprados, "KM")
    else:
        print("Você não consegue viajar para toquio, Litros comprados: ", litroscomprados, " Km rodados vai ser de: ", km_comprados, "KM")
