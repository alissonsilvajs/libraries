def analisar_numeros(lista):
    if not lista:
        return "Lista vazia"

    media = sum(lista) / len(lista)
    maior = max(lista)
    menor = min(lista)
    pares = len([num for num in lista if num % 2 == 0])

    resultado = {
        "media": round(media, 2),
        "maior": maior,
        "menor": menor,
        "pares": pares
    }

    return resultado