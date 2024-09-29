# SUGESTÃO DE PROJETO:

# SIMULADOR DE CADASTRO DE SENHA E INICIALIZAÇÃO DE CELULAR

# Utilizando o aprendizado desta aula, implementaremos um sistema de cadastro de senha e inicialização do celular utilizando o loop "for".

# Após ligar o celular, o usuário é solicitado a inserir a senha cadastrada.
# São permitidas 3 tentativas até que o telefone seja bloqueado.
# Se o usuário acertar a senha, uma mensagem de boas-vindas é exibida: "Bem-vindo."
# Se o usuário errar a senha, uma mensagem informando o erro é exibida, junto com o número de tentativas restantes até o bloqueio do telefone.
# Pense em todas as possibilidades e faça um sistema completo.

# Simulador de Cadastro de Senha e Inicialização de Celular

# Cadastro de senha (senha fictícia para o exemplo)
senha_cadastrada = "1234"

# Número máximo de tentativas
tentativas_restantes = 3

# Loop de inicialização
for tentativa in range(1, tentativas_restantes + 1):
    senha_inserida = input("Insira sua senha: ")
    
    if senha_inserida == senha_cadastrada:
        print("Bem-vindo.")
        break
    else:
        tentativas_restantes -= 1
        if tentativas_restantes > 0:
            print(f"Senha incorreta. Você tem {tentativas_restantes} tentativa(s) restante(s).")
        else:
            print("Telefone bloqueado. Todas as tentativas foram usadas.")

