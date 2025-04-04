from youtube_transcript_api import YouTubeTranscriptApi
import requests
import json
import os
from typing import Tuple, Optional

def extract_video_id(url: str) -> str:
    """Extraire l'ID de la vidéo à partir de l'URL YouTube."""
    if "v=" in url:
        return url.split("v=", 1)[1].split("&", 1)[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/", 1)[1].split("?", 1)[0]
    return url

def get_transcript(video_id: str) -> Optional[str]:
    """Récupérer la transcription d'une vidéo YouTube."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['fr', 'en'])
        all_text = ' '.join(item['text'] for item in transcript)
        return all_text
    except Exception as e:
        print(f"Erreur lors de la récupération de la transcription: {e}")
        return None

def generate_summary(transcript: str, summary_type: str) -> Tuple[str, Optional[str]]:
    """Générer un résumé à partir du transcript via l'API OpenRouter."""
    # Définir le prompt en fonction du type de résumé
    if summary_type == "detailed":
        prompt = "Résume en français cette vidéo en un paragraphe à partir du transcript (juste le résumé) : "
    elif summary_type == "bullet":
        prompt = "Résume en français cette vidéo en points clés style bullet points à partir du transcript (juste le résumé): "
    else:
        return "Type de résumé non valide", None

    prompt = prompt + transcript
    
    # Récupérer la clé API depuis les variables d'environnement
    api_key = os.environ.get("OPENROUTER_API_KEY", "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")
    
    try:
        # Préparation de la requête
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "mistralai/mistral-small-24b-instruct-2501:free",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        
        # Envoi de la requête
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            data=json.dumps(payload),
            timeout=30
        )
        
        # Vérification du code de statut
        if response.status_code != 200:
            print(f"Erreur API: Statut {response.status_code} - {response.text}")
            return f"Erreur API: Code {response.status_code}", None
        
        # Analyse de la réponse
        try:
            data = response.json()
        except json.JSONDecodeError as e:
            print(f"Erreur de décodage JSON: {e} - Réponse: {response.text}")
            return "Erreur: Impossible de décoder la réponse de l'API", None
        
        # Vérification de la structure de la réponse
        if 'choices' not in data:
            print(f"Erreur: 'choices' non trouvé dans la réponse - Réponse: {data}")
            return "Erreur: Format de réponse API inattendu (choices manquant)", None
            
        if not data['choices'] or not isinstance(data['choices'], list):
            print(f"Erreur: 'choices' vide ou de format incorrect - Réponse: {data}")
            return "Erreur: Liste de choix vide ou incorrecte", None
            
        if 'message' not in data['choices'][0]:
            print(f"Erreur: 'message' non trouvé dans choices[0] - Réponse: {data}")
            return "Erreur: Format de réponse API inattendu (message manquant)", None
            
        if 'content' not in data['choices'][0]['message']:
            print(f"Erreur: 'content' non trouvé dans choices[0]['message'] - Réponse: {data}")
            return "Erreur: Format de réponse API inattendu (content manquant)", None
        
        # Extraction du texte de la réponse
        answer_text = data["choices"][0]["message"]["content"]
        return "success", answer_text
    except requests.RequestException as e:
        print(f"Erreur de requête HTTP: {e}")
        return f"Erreur de connexion à l'API: {e}", None
    except Exception as e:
        print(f"Exception inattendue: {e}")
        return f"Erreur lors de la génération du résumé: {e}", None
