from flask import Flask, render_template, request, redirect, url_for, flash
import os
from dotenv import load_dotenv
from utils.youtube_helper import extract_video_id, get_transcript, generate_summary

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "une_cle_secrete_temporaire")
app.debug = os.environ.get("FLASK_ENV") == "development"

@app.route('/')
def index():
    """Page d'accueil avec le formulaire."""
    return render_template('index.html')

@app.route('/resume', methods=['POST'])
def resume():
    """Traitement de la demande de résumé."""
    # Récupérer les données du formulaire
    youtube_url = request.form.get('youtube_url', '')
    summary_type = request.form.get('summary_type', 'detailed')
    
    # Valider l'URL
    if not youtube_url:
        flash("Veuillez entrer une URL YouTube valide", "error")
        return redirect(url_for('index'))
    
    # Extraire l'ID de la vidéo
    video_id = extract_video_id(youtube_url)
    
    # Récupérer la transcription
    transcript = get_transcript(video_id)
    if not transcript:
        flash("Impossible de récupérer la transcription pour cette vidéo", "error")
        return redirect(url_for('index'))
    
    # Générer le résumé
    status, summary = generate_summary(transcript, summary_type)
    if status != "success":
        flash(status, "error")
        return redirect(url_for('index'))
    
    # Charger la page de résultat
    return render_template('result.html', 
                          summary=summary, 
                          video_id=video_id, 
                          summary_type=summary_type)

@app.errorhandler(404)
def page_not_found(e):
    """Gestion des erreurs 404."""
    return render_template('error.html', error="Page non trouvée"), 404

@app.errorhandler(500)
def server_error(e):
    """Gestion des erreurs 500."""
    return render_template('error.html', error="Erreur serveur interne"), 500

if __name__ == '__main__':
    # Pour le développement local
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
