# RésuméYT

Application web pour résumer automatiquement des vidéos YouTube en français. Cette application utilise l'API YouTube Transcript pour extraire le contenu des vidéos et l'API OpenRouter pour générer des résumés en français.

## Fonctionnalités

- Interface utilisateur intuitive et réactive
- Résumés en deux formats : détaillé (paragraphe) ou points clés (bullet points)
- Animations CSS pour une expérience utilisateur fluide et agréable
- Responsive design (fonctionne sur mobile, tablette et desktop)

## Technologie

- **Backend** : Flask (Python)
- **Frontend** : HTML, CSS, JavaScript
- **APIs** : YouTube Transcript API, OpenRouter API (IA)

## Démarrage Rapide

### Installation Locale

1. Clonez ce dépôt :
   ```
   git clone <url-du-repo>
   cd resumeyt
   ```

2. Créez un environnement virtuel Python :
   ```
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```

3. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

4. Configurez les variables d'environnement :
   ```
   # Créez un fichier .env à la racine du projet
   OPENROUTER_API_KEY=votre_clé_api_openrouter
   SECRET_KEY=une_clé_secrète_pour_flask
   ```

5. Lancez l'application :
   ```
   flask run
   ```

6. Accédez à l'application dans votre navigateur : [http://localhost:5000](http://localhost:5000)

### Déploiement sur Render

1. Créez un compte sur [Render](https://render.com/) si vous n'en avez pas déjà un.

2. Dans votre tableau de bord Render, cliquez sur "New +" puis sélectionnez "Blueprint".

3. Connectez votre dépôt GitHub contenant ce projet.

4. Render détectera automatiquement le fichier `render.yaml` et configurera les services.

5. Ajoutez la variable d'environnement `OPENROUTER_API_KEY` avec votre clé API OpenRouter dans les paramètres du service.

6. Déployez le projet et attendez que le déploiement soit terminé.

7. Votre application sera accessible à l'URL fournie par Render.

## Remarques

- L'API OpenRouter nécessite une clé API valide. Vous pouvez en obtenir une sur [OpenRouter](https://openrouter.ai/).
- Certaines vidéos YouTube peuvent ne pas avoir de transcription disponible.

## Licence

Ce projet est sous licence MIT.
