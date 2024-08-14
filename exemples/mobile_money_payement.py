from feexpay import MobilePaymentRequest, CardPaymentRequest, send_payment_request, detect_network

# Exemple de données pour un paiement mobile
mobile_payment_data = MobilePaymentRequest(
    phoneNumber="numero de telephone",
    amount=10000,
    firstName="test",
    lastName="test",
    shop="id de la boutique",
    description="Paiement pour service"
)

api_key = "votre clé d'API"
payment_type = "mobile"

# Envoyer la requête de paiement
response = send_payment_request(mobile_payment_data, api_key, payment_type)
print(response.json())  # Affiche la réponse de l'API


