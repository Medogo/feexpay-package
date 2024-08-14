FeexPay Payment Package

Overview

FeexPay Payment Package is a Python package designed to facilitate the integration of payment services using mobile money and card payments through the FeexPay API. It supports automatic network detection for mobile payments and provides a simple interface for initiating both mobile and card transactions.

Features

Mobile Payments: Automatically detect the mobile network based on the phone number and process the payment.

Card Payments: Initiate card payments with support for VISA and MASTERCARD.

Flexible API Integration: Easy-to-use functions for interacting with the FeexPay API.

Installation

To install the package, use pip:

pip install feexpay

Usage

Basic Setup

First, import the necessary classes and functions from the package:

from feexpay.models import MobilePaymentRequest, CardPaymentRequest

from feexpay.utils import send_payment_request

Mobile Payment Example

To initiate a mobile payment, create an instance of MobilePaymentRequest and call send_payment_request:

data = MobilePaymentRequest(
    phoneNumber="+22966000000",
    amount=1000,
    firstName="John",
    lastName="Doe",
    shop="shop123",
    description="Payment for services"
)

api_key = "your_api_key_here"
response = send_payment_request(data, api_key, payment_type="mobile")

print(response.json())

Card Payment Example

To initiate a card payment, create an instance of CardPaymentRequest and call send_payment_request:

data = CardPaymentRequest(
    cardNumber="4111111111111111",
    amount=5000,
    firstName="Jane",
    lastName="Doe",
    shop="shop123",
    description="Payment for products",
    type_card="VISA"
)

api_key = "your_api_key_here"
response = send_payment_request(data, api_key, payment_type="card")

print(response.json())

Error Handling

The package raises appropriate exceptions for validation errors, network detection failures, and API errors. Ensure that you handle these exceptions in your implementation:


try:
    response = send_payment_request(data, api_key, payment_type="mobile")
except ValueError as e:
    print(f"Validation error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

Contributing
We welcome contributions to improve this package. Please fork the repository, create a new branch, and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Support
If you encounter any issues, please open an issue on GitHub or contact us at contact@feexpay.me.

