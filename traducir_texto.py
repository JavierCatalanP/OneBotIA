import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

def traducir_texto(texto, idioma):
    prompt = f"Traduce el texto '{texto}' al {idioma}."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        n=1,
        temperature=0.5,
        max_tokens=500
    )
    return response.choices[0].text.strip()

#probar la función
mi_texto = input("Escribe el texto que quieres traducir: ")
mi_idioma = input("A qué idioms lo quieres traducir: ")
traduccion = traducir_texto(mi_texto, mi_idioma)
print(traduccion)
