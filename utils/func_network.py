import requests

URL_DOFUS_MAP = "https://dofus-map.com/getRessourceData.php?"

def make_request_dofus_map(ressourceId, groupId=0):
    url = URL_DOFUS_MAP + "ressourceId=" + str(ressourceId) + "&groupId=" + str(groupId)
    response = make_http_request(url)

    return response

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