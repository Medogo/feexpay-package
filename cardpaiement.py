from feexpay import CardPaymentRequest, send_payment_request

# Exemple pour CardPaymentRequest
card_payment_data = CardPaymentRequest(
    phone="+22966000000",
    amount=100,
    first_name="John",
    last_name="Doe",
    shop="65a15914f7c3688685a04ad2",  # Remplacez ceci par un ID de boutique valide
    title="Mr",
    address="Cotonou",
    locality="Cotonou",
    type_card="MASTERCARD",
    country="Benin"
)

api_key = "fp_iVqQPZl4ZRL7Exlg3455zf2YoyD255T8wW3mswcyb4I7OpmWbzwwfaxlRc5HUZM2"  # Remplacez ceci par une clé API valide
payment_type = "card"

response = send_payment_request(card_payment_data, api_key, payment_type)
print(response.json())
