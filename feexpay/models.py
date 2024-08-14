from pydantic import BaseModel, Field, validator
from typing import Optional


class MobilePaymentRequest(BaseModel):
    phoneNumber: str = Field(..., description="Un numéro de téléphone au format du pays.")
    amount: int = Field(..., ge=50, description="Le montant de la transaction, minimum 50.")
    firstName: Optional[str] = Field(None, description="Prénom du client.")
    lastName: Optional[str] = Field(None, description="Nom du client.")
    shop: str = Field(..., description="ID de la boutique.")
    description: Optional[str] = Field(None, description="Une description sur la transaction.")

    @validator('phoneNumber')
    def validate_phone_number(cls, v):
        if not (v.startswith('+') and len(v) >= 10 and len(v) <= 15 and v[1:].isdigit()):
            raise ValueError(
                "Le numéro de téléphone doit être au format international, commençant par '+', avec 10 à 15 chiffres.")
        return v


class CardPaymentRequest(BaseModel):
    phone: str = Field(..., description="Un numéro de téléphone au format du pays.")
    amount: int = Field(..., ge=50, description="Le montant de la transaction, minimum 50.")
    first_name: str = Field(..., description="Prénom du client.")
    last_name: str = Field(..., description="Nom du client.")
    shop: str = Field(..., description="ID de la boutique.")
    title: str = Field(..., description="Titre du client.")
    address: str = Field(..., description="Adresse du client.")
    locality: str = Field(..., description="Localité du client.")
    type_card: str = Field(..., description="Type de carte: VISA ou MASTERCARD.")
    country: str = Field(..., description="Le pays du client en version anglaise.")

    @validator('type_card')
    def validate_type_card(cls, v):
        if v not in ["VISA", "MASTERCARD"]:
            raise ValueError("Le type de carte doit être 'VISA' ou 'MASTERCARD'.")
        return v

    @validator('phone')
    def validate_phone_number(cls, v):
        if not (v.startswith('+') and len(v) >= 10 and len(v) <= 15 and v[1:].isdigit()):
            raise ValueError(
                "Le numéro de téléphone doit être au format international, commençant par '+', avec 10 à 15 chiffres.")
        return v

