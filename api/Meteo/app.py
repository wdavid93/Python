from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Route pour la page d'accueil
@app.route('/', methods=['GET', 'POST'])
def index():
    # Variable pour stocker les informations météorologiques
    weather_data = None

    # Si le formulaire a été soumis
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            # URL de l'API de météo (exemple avec OpenWeatherMap sans clé API)
            url = f'http://wttr.in/{city}?format=%t'
            try:
                response = requests.get(url)
                # Assurez-vous que la réponse est correcte
                if response.status_code == 200:
                    weather_data = response.text.strip()  # Nettoie la réponse
                else:
                    weather_data = "Erreur lors de la récupération des données."
            except requests.RequestException:
                weather_data = "Erreur lors de la requête API."

    # Affiche le formulaire et les résultats météorologiques
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
