from feexpay import CardPaymentRequest, send_payment_request

# Exemple pour CardPaymentRequest
card_payment_data = CardPaymentRequest(
    phone="numero de telephone",
    amount=100,
    first_name="John",
    last_name="Doe",
    shop="id boutique",  # Remplacez ceci par un ID de boutique valide
    title="Mr",
    address="Cotonou",
    locality="Cotonou",
    type_card="MASTERCARD",
    country="Benin"
)
#Vous devez avoir un compte valide et faire les demarche aupres de feexpay pour utiliser ce service
api_key = "votre clé d'API"  # Remplacez ceci par une clé API valide
payment_type = "card"

response = send_payment_request(card_payment_data, api_key, payment_type)
print(response.json())
