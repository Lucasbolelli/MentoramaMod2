def mult (mensagem, num1, num2):
    while True:
        try: 
            v=int(input(mensagem))
            if v > num1 and v <= num2:
                return v
            else:
                print("Digite um valor entre %.1f %.1f"%(num1, num2))
        except:
            print("Voce deve digitar um numero")