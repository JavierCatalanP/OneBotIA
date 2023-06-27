import os
import openai
import spacy
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

modelo = 'text-davinci-002'
prompt = "cuenta una historia breve de un viaje al sur de chile"

respuesta = openai.Completion.create(
    engine=modelo,
    prompt=prompt,
    n=1,
    temperature=1,
    max_tokens=50
)

#for idx, opcion in enumerate(respuesta.choices):
 #   texto_generado = opcion.text.strip()
 #   print(f"Respuesta {idx + 1}: {texto_generado}\n")

texto_generado = respuesta.choices[0].texto.strip()
print(texto_generado)

print("***")

modelo_spacy = spacy.load("es_core_news_md")
analisis = modelo_spacy(texto_generado)

ubicacion = None

#for token in analisis:
 #   print(token.text)

for ent in analisis.ents:
    if ent.label_ == "LOC":
    ubicacion = ent
    break

if ubicacion:
    prompt2 = f"Dime más acerca de {ubicacion}"
    respuesta2 = openai.Completion.create(
        engine=modelo,
        prompt=prompt2,
        n=1,
        max_tokens=50
    )
    print(respuesta2.choices[0].text.strip())


