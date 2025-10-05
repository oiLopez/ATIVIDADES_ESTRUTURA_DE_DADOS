senha_correta = "1724"

while True:
    senha_digitada = input("Digite a senha: ")
    
    if senha_digitada == senha_correta:
        print("✅ Senha correta!")
        break
    else:
        print("❌ Senha incorreta!")