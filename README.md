# 🔐 criptografia_assimetrica_ads.py

**Desenvolvido por Lucas Lemos Pavesi**  
Prova da disciplina **Segurança da Informação** - IFTM - 2025

---

## 📌 Sobre o Projeto
Este projeto apresenta a implementação de um sistema de **criptografia assimétrica** utilizando o algoritmo **RSA** para proteger mensagens de texto. 

O objetivo é aplicar os princípios da criptografia moderna, permitindo ao usuário gerar um par de chaves (pública e privada), criptografar mensagens usando a chave pública e descriptografar usando a chave privada. O sistema é operado via linha de comando com um menu interativo.

---

## 🛠 Tecnologias Utilizadas
- **Python 3.10+**
- Biblioteca [pycryptodome](https://pypi.org/project/pycryptodome/) para operações criptográficas
- Algoritmo RSA (2048 bits) com esquema PKCS1_OAEP

---

## ▶️ Como Executar o Programa

1. Instale a biblioteca necessária:
```
pip install pycryptodome
```

2. Execute o script no terminal:
```
python criptografia_assimetrica_ads.py
```

---

## ✅ Funcionalidades
- Geração de par de chaves RSA (pública e privada) salvas em arquivos `.pem`
- Criptografia de mensagens de texto usando a chave pública
- Descriptografia de mensagens usando a chave privada
- Salvar e carregar mensagens criptografadas de arquivos `.txt`
- Interface via terminal simples e intuitiva

---

## 💡 Explicação do Funcionamento
1. O usuário gera um par de chaves RSA, que são salvas em dois arquivos:
   - `chave_publica.pem`: usada para criptografar
   - `chave_privada.pem`: usada para descriptografar

2. O usuário pode digitar uma mensagem e criptografá-la usando a chave pública.

3. A mensagem criptografada pode ser salva em um arquivo ou copiada manualmente.

4. Para recuperar a mensagem original, o sistema utiliza a chave privada correspondente.

---

## 🎥 Demonstração em Vídeo

Assista ao vídeo demonstrando o funcionamento completo do sistema de criptografia RSA:

🔗 [Clique aqui para assistir à demonstração](https://youtu.be/HUTdhfAtvK4)

> O vídeo mostra as etapas de geração de chaves, criptografia, salva de mensagens e descriptografia usando arquivos `.pem`.

---

## 👨‍🎓 Sobre
Este projeto foi desenvolvido como parte da Prova 2 da disciplina de **Segurança da Informação** do curso de **Análise e Desenvolvimento de Sistemas - IFTM**.

**Aluno:** Lucas Lemos Pavesi  
**Professor:** Júnio Moreira  
**Data de Entrega:** 28/03/2025

---

**Repositório privado e de uso exclusivo para fins avaliativos.**
