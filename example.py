from feexpay import PaymentRequest, send_payment_request

# Créez un objet PaymentRequest avec les données de la requête
payment_data = PaymentRequest(
    phoneNumber="22962037761",
    amount=100,
    firstName="John",
    lastName="Doe",
    shop="65a15914f7c3688685a04ad2",
    description="FeexPay"
)

# Utilisez votre clé API FeexPay
api_key = "fp_iVqQPZl4ZRL7Exlg3455zf2YoyD255T8wW3mswcyb4I7OpmWbzwwfaxlRc5HUZM2"
# Envoyez la requête de paiement
response = send_payment_request(payment_data, api_key)

# Vérifiez la réponse
print(response.status_code, response.json())
