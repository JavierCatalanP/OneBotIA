import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def crear_contenido(tema, tokens, temperatura, modelo="text-davinci-002" ):
    prompt = f"Por favor escribe un articulo corto sobre el tema: {tema}\n\n"
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperatura
    )
    return respuesta.choice[0].text.strip()

def resumir_texto(texto, tokens, temperatura, modelo="text-davinci-002"):
    prompt= f"Por favor resume el siguiente texto: {texto}\n\n"
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperatura
    )
    return respuesta.choices[0].text.strip()

#Probando función crear_contenido
#tema = input("Elije un tema para tu articulo: ")
#tokens = int(input("Cuantos tokens máximos tendrá tu articulo:"))
#temperatura = int(input("Del 1 al 10, que tan creativo quieres que sea tu articulo?: "))
#articulo_creado = crear_contenido(tema,tokens,temperatura)
#print(articulo_creado)

#Probando función resumir_texto
original = input("Pega aquí el articulo que quieres resumur: ")
tokens = int(input("Cuantos tokens máximos tendrá tu resumen:"))
temperatura = int(input("Del 1 al 10, que tan creativo quieres que sea tu resumen?: ")) / 10
resumen = resumir_texto(original,tokens,temperatura)
print(resumen)
