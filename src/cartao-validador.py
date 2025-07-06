import re

def validar_luhn(numero):
    soma = 0
    inverso = numero[::-1]
    for i, digito in enumerate(inverso):
        n = int(digito)
        if i % 2:
            n *= 2
            if n > 9:
                n -= 9
        soma += n
    return soma % 10 == 0

def identificar_bandeira(numero):
    numero = re.sub(r"\D", "", numero)  # Remove espaços e traços

    if not numero.isdigit():
        return "Cartão inválido (somente números)"
    if not validar_luhn(numero):
        return "Número de cartão inválido (Luhn)"

    padroes = {
        "Visa": r"^4\d{12}(\d{3})?(\d{3})?$",
        "MasterCard": r"^5[1-5]\d{14}$",
        "American Express": r"^3[47]\d{13}$",
        "Diners Club": r"^3(0[0-5]|[68])\d{11}$",
        "Discover": r"^6(011|5\d{2}|4[4-9]\d)\d{12}$",
        "enRoute": r"^2(014|149)\d{11}$",
        "JCB": r"^35\d{14,17}$",
        "Voyager": r"^8699\d{11}$",
        "Hipercard": r"^(38\d{14}|606282\d{10})$",
        "Aura": r"^50\d{14}$",
    }

    for bandeira, padrao in padroes.items():
        if re.match(padrao, numero):
            return f"Bandeira: {bandeira}"

    return "Bandeira não reconhecida"

# Entrada do usuário
cartao = input("Digite o número do cartão de crédito: ")
print(identificar_bandeira(cartao))