import array
import json
import random

def ler_perguntas():
    try:
        with open('src/perguntas.json', 'r', encoding='utf-8' ) as arquivo:
            return list(json.load(arquivo).values())
    except FileNotFoundError:
        return []  # Caso o arquivo não exista, retorna uma lista vazia

perguntas_feitas = []

def escolher_pergunta(perguntas, feitas):
    perguntas_restantes = [p for p in perguntas if p not in feitas]
    
    # Se a lista de perguntas estiver vazia, retornar None
    if not perguntas_restantes:
        print("Todas as perguntas já foram feitas.")
        return None

    nova = random.choice(perguntas_restantes)
    feitas.append(nova)
    return nova

perguntas = ler_perguntas()

for _ in range(1):
    pergunta = escolher_pergunta(perguntas, perguntas_feitas)
    if pergunta:
        print(f"Pergunta: {pergunta}")