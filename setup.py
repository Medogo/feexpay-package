from setuptools import setup, find_packages

setup(
    name="payment_aggregator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pydantic",
        "requests",
    ],
    description="Package pour l'agrégation de paiements  MOBILE MONEY ET card",
    author="Dominique Megnidro",
    author_email="dmegnidro@gmail.com",
    url="https://github.com/Medogo/feexpay-package.git",
)
