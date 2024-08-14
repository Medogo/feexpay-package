import requests
from .models import PaymentRequest


def detect_network(phoneNumber: str) -> str:
    """
    Détecte le réseau en fonction du préfixe du numéro de téléphone.

    :param phone_number: str - Le numéro de téléphone au format international (e.g., +22966000000)
    :return: str - Le nom du réseau détecté (e.g., 'mtn', 'moov', 'orange_ci').
    """
    network_map = {
        "mtn": ["22962", "22997"],  # Bénin (exemples)
        "moov": ["22999", "22991"],  # Bénin (exemples)
        "togocom_tg": ["22890", "22899"],  # Togo (exemples)
        "moov_tg": ["22891", "22892"],  # Togo (exemples)
        "orange_ci": ["22507", "22557"],  # Côte d'Ivoire (exemples)
        "mtn_ci": ["22505", "22555"],  # Côte d'Ivoire (exemples)
        "wave_ci": ["22501", "22550"],  # Côte d'Ivoire (exemples)
        "moov_ci": ["22506", "22556"],  # Côte d'Ivoire (exemples)
        "orange_bf": ["22670", "22671"],  # Burkina Faso (exemples)
        "moov_bf": ["22672", "22673"],  # Burkina Faso (exemples)
        "orange_sn": ["22177", "22178"],  # Sénégal (exemples)
        "free_sn": ["22170", "22175"]  # Sénégal (exemples)
    }

    # Parcourir le mapping pour trouver le réseau correspondant au préfixe
    for network, prefixes in network_map.items():
        if any(phoneNumber.startswith(prefix) for prefix in prefixes):
            return network

    raise ValueError("Réseau non reconnu pour ce numéro de téléphone")


def send_payment_request(data: PaymentRequest, api_key: str):
    """
    Envoie une requête de paiement à l'API FeexPay via le réseau détecté automatiquement.

    :param data: PaymentRequest - Les données validées de la requête.
    :param api_key: str - La clé API pour l'authentification.
    :return: Response object - La réponse de l'API.
    """
    # Détecter le réseau en fonction du numéro de téléphone
    network = detect_network(data.phoneNumber)

    url = f"https://api.feexpay.me/api/transactions/public/requesttopay/{network}"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Envoyer la requête avec les données validées
    response = requests.post(url, headers=headers, json=data.dict())
    return response









"""
def send_paymet_request(data: PaymentRequest, api_key: str, network: str):

    # Valider le réseau et construire l'URL
    if network not in ["mtn", "moov",
                       "togocom_tg",
                       "moov_tg",
                       "moov_bf",
                       "orange_bf",
                       "orange_sn",
                       "free_sn",
                       "mtn_ci",
                       "wave_ci",
                       "moov_ci",
                       "orange_ci"]:
        raise ValueError("Le réseau doit être 'mtn' ou 'moov'")

    url = f"https://api.feexpay.me/api/transactions/public/requesttopay/{network}"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Envoyer la requête avec les données validées
    response = requests.post(url, headers=headers, json=data.dict())
    return response
"""