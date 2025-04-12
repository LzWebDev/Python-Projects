import array
import json

# Abre o arquivo
with open('src/perguntas.json', 'r', encoding='utf-8') as alternativa:
    perguntas = json.load(alternativa)

print(perguntas['alternativa-1'])