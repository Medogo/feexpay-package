from feexpay import MobilePaymentRequest, CardPaymentRequest, send_payment_request, detect_network

# Exemple de données pour un paiement mobile
mobile_payment_data = MobilePaymentRequest(
    phoneNumber="+22962213185",
    amount=10000,
    firstName="test",
    lastName="test",
    shop="65a15914f7c3688685a04ad2",
    description="Paiement pour service"
)

api_key = "fp_iVqQPZl4ZRL7Exlg3455zf2YoyD255T8wW3mswcyb4I7OpmWbzwwfaxlRc5HUZM2"
payment_type = "mobile"

# Envoyer la requête de paiement
response = send_payment_request(mobile_payment_data, api_key, payment_type)
print(response.json())  # Affiche la réponse de l'API


