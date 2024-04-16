import requests

def make_http_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print("La requête a échoué avec le code de statut:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Une erreur s'est produite lors de la requête:", e)
        return None