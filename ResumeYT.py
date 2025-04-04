from youtube_transcript_api import YouTubeTranscriptApi
from dataclasses import dataclass
import requests
import json

url = input("Entrer l'URL de la vidéo Youtube : ")
params = input("Choisir un type de résumé : 1. Résumé détaillé ; 2. Résumé en points clés : ")

url = url.split("v=",1)[1]

print(url)
if params == "1":
    prompt = "Résume en français cette vidéo en un paragraphe à partir du transcript (juste le résumé) : "
elif params == "2":
    prompt = "Résume en français cette vidéo en points clés style bullet points à partir du transcript (juste le résumé): "

ytt_api = YouTubeTranscriptApi()
transcript = ytt_api.fetch(url)
all_text = ' '.join(snippet.text for snippet in transcript.snippets)

prompt = prompt + all_text

def openrouter_api_call(prompt):
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer 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"
    },
    data=json.dumps({
        "model": "mistralai/mistral-small-24b-instruct-2501:free", # Optional
        "messages": [
        {
            "role": "user",
            "content": prompt
        }
        ]
    })
    )

    data = response.json()
    answer_text = data["choices"][0]["message"]["content"]

    return answer_text

print(openrouter_api_call(prompt))