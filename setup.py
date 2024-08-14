from setuptools import setup, find_packages

setup(
    name="payment_aggregator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pydantic",
        "requests",
    ],
    description="Package pour l'agrégation de paiements via MTN MOBILE MONEY",
    author="Votre Nom",
    author_email="votre.email@example.com",
    url="https://github.com/votrecompte/payment_aggregator",
)
