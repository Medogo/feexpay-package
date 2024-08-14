import requests
from typing import Union
from .models import MobilePaymentRequest, CardPaymentRequest


def detect_network(phoneNumber: str) -> str:
    """
    Détecte le réseau en fonction du préfixe du numéro de téléphone.

    :param phoneNumber: str - Le numéro de téléphone au format international (e.g., +22966000000)
    :return: str - Le nom du réseau détecté (e.g., 'mtn', 'moov', 'orange_ci').
    """
    network_map = {
        "mtn": [
            "22942", "22946", "22950", "22951", "22952", "22953", "22954",
            "22956", "22957", "22959", "22961", "22962", "22966", "22967",
            "22969", "22990", "22991", "22996", "22997"
        ],
        "moov": ["22999", "22964", "22995", "22994"],
        "togocom_tg": ["22890", "22899"],
        "moov_tg": ["22891", "22892"],
        "orange_ci": ["22507", "22557"],
        "mtn_ci": ["22505", "22555"],
        "wave_ci": ["22501", "22550"],
        "moov_ci": ["22506", "22556"],
        "orange_bf": ["22670", "22671"],
        "moov_bf": ["22672", "22673"],
        "orange_sn": ["22177", "22178"],
        "free_sn": ["22170", "22175"]
    }

    # Valider le format du numéro de téléphone
    if not phoneNumber.startswith('+'):
        raise ValueError("Le numéro de téléphone doit commencer par un '+'.")

    # Détecter le réseau en fonction du préfixe
    for network, prefixes in network_map.items():
        if any(phoneNumber[1:].startswith(prefix) for prefix in prefixes):  # Supprimer le '+' pour la comparaison
            return network

    raise ValueError("Réseau non reconnu pour ce numéro de téléphone")


def send_payment_request(data: Union[MobilePaymentRequest, CardPaymentRequest], api_key: str,
                         payment_type: str) -> requests.Response:
    """
    Envoie une requête de paiement à l'API FeexPay en fonction du type de paiement.

    :param data: Union[MobilePaymentRequest, CardPaymentRequest] - Les données validées de la requête.
    :param api_key: str - La clé API pour l'authentification.
    :param payment_type: str - Le type de paiement ('mobile' ou 'card').
    :return: Response object - La réponse de l'API.
    """
    if payment_type == "mobile":
        network = detect_network(data.phoneNumber)  # Détecter le réseau pour les paiements mobiles
        url = f"https://api.feexpay.me/api/transactions/public/requesttopay/{network}"
    elif payment_type == "card":
        url = "https://api.feexpay.me/api/transactions/public/initcard"
    else:
        raise ValueError("Le type de paiement doit être 'mobile' ou 'card'")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Envoyer la requête avec les données validées
    response = requests.post(url, headers=headers, json=data.dict())
    return response
