resposta=input("Ola! Você deseja calcular o seu IMC? ").lower()         

if resposta==("sim"):
    print("Ok vamos la!")
    
    peso=float(input("Digite seu peso: "))
    
    altura=float(input("Digite sua altura: "))
    
    imc=peso/(altura*altura)
    
    print("Seu imc é: ", imc)
    
    if imc<18.5:
        classificacao=("Baixo peso")
    elif imc>=18.5 and imc<=24.9:
        classificacao=("Peso normal")
    elif imc>=25 and imc<=29.9:
        classificacao=("Pré-obesidade")
    elif imc>=30 and imc<=33.9:
        classificacao=("Obesidade grau I")
    elif imc>=35 and imc<=39.9:
        classificacao=("Obesidadde grau II")
    elif imc>40:
        classificacao=("Obesidadde grau III")
        
    print("Ele está classificado como: ", classificacao)
    
    input("Aperte Enter para encerrar o programa.")                 

    exit()                                                         


elif resposta in ["não", "nao"]:                                  
    print("Que pena até a proxima!")
    input("Aperte Enter para encerrar o programa.")
    exit()                                                        

else: print("Por favor tente novamente e responda sim ou não.")

exit()
