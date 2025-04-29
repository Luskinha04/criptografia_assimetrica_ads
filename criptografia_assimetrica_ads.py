# criptografia_assimetrica_ads.py
# Desenvolvido por Lucas Lemos Pavesi - Prova 2 - Segurança da Informação

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
import base64


# Função para limpar o terminal
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


# Função para exibir o cabeçalho visual do sistema
def mostrar_logo():
    print("=" * 70)
    print("SISTEMA DE CRIPTOGRAFIA ASSIMÉTRICA - RSA - PROVA 2")
    print("Desenvolvido por Lucas Lemos Pavesi - IFTM - 2025")
    print("=" * 70)


# Função para gerar e salvar par de chaves
def gerar_chaves():
    chave = RSA.generate(2048)
    chave_privada = chave.export_key()
    chave_publica = chave.publickey().export_key()

    with open("chave_privada.pem", "wb") as priv_file:
        priv_file.write(chave_privada)

    with open("chave_publica.pem", "wb") as pub_file:
        pub_file.write(chave_publica)

    print(
        "\n🔑 Chaves geradas e salvas com sucesso em 'chave_privada.pem' e 'chave_publica.pem'!"
    )


# Função para carregar chave pública
def carregar_chave_publica():
    with open("chave_publica.pem", "rb") as file:
        chave_publica = RSA.import_key(file.read())
    return chave_publica


# Função para carregar chave privada
def carregar_chave_privada():
    with open("chave_privada.pem", "rb") as file:
        chave_privada = RSA.import_key(file.read())
    return chave_privada


# Função para criptografar mensagem
def criptografar_mensagem():
    chave_publica = carregar_chave_publica()
    cipher = PKCS1_OAEP.new(chave_publica)

    mensagem = input("Digite a mensagem que deseja criptografar: ")
    mensagem_bytes = mensagem.encode("utf-8")
    mensagem_cifrada = cipher.encrypt(mensagem_bytes)
    mensagem_cifrada_b64 = base64.b64encode(mensagem_cifrada).decode("utf-8")

    print("\n🔒 Mensagem criptografada com sucesso:")
    print(mensagem_cifrada_b64)

    salvar = input(
        "\nDeseja salvar a mensagem criptografada em um arquivo? (s/n): "
    ).lower()
    if salvar == "s":
        nome_arquivo = input(
            "Digite o nome do arquivo para salvar (ex: mensagem_cifrada.txt): "
        )
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(mensagem_cifrada_b64)
        print("Arquivo salvo com sucesso!")

    input("\nPressione Enter para voltar ao menu...")


# Função para descriptografar mensagem
def descriptografar_mensagem():
    chave_privada = carregar_chave_privada()
    cipher = PKCS1_OAEP.new(chave_privada)

    escolha = input(
        "\nDeseja ler a mensagem criptografada de um arquivo? (s/n): "
    ).lower()
    if escolha == "s":
        nome_arquivo = input("Digite o nome do arquivo (ex: mensagem_cifrada.txt): ")
        if not os.path.exists(nome_arquivo):
            print("⚠ Arquivo não encontrado!")
            input("\nPressione Enter para voltar ao menu...")
            return
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            mensagem_cifrada_b64 = arquivo.read()
    else:
        mensagem_cifrada_b64 = input("Digite a mensagem criptografada (base64): ")

    try:
        mensagem_cifrada = base64.b64decode(mensagem_cifrada_b64)
        mensagem_decifrada = cipher.decrypt(mensagem_cifrada)
        print("\n🔓 Mensagem descriptografada com sucesso:")
        print(mensagem_decifrada.decode("utf-8"))
    except Exception:
        print(
            "\n⚠ Erro ao descriptografar! Verifique se a chave é correta e se a mensagem está válida."
        )

    input("\nPressione Enter para voltar ao menu...")


# Menu interativo
def menu():
    while True:
        limpar_tela()
        mostrar_logo()
        print("1 - Gerar novas chaves RSA")
        print("2 - Criptografar mensagem")
        print("3 - Descriptografar mensagem")
        print("0 - Sair")
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            gerar_chaves()
            input("\nPressione Enter para voltar ao menu...")
        elif escolha == "2":
            criptografar_mensagem()
        elif escolha == "3":
            descriptografar_mensagem()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")


# Execução principal
if __name__ == "__main__":
    menu()
