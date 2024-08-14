from pydantic import BaseModel, Field, validator
from typing import Optional


class PaymentRequest(BaseModel):
    phoneNumber: str = Field(..., description="Un numéro de téléphone au format du pays.")
    amount: int = Field(..., ge=50, description="Le montant de la transaction, minimum 50.")
    firstName: Optional[str] = Field(None, description="Prénom du client.")
    lastName: Optional[str] = Field(None, description="Nom du client.")
    shop: str = Field(..., description="ID de la boutique.")
    description: Optional[str] = Field(None, description="Une description sur la transaction.")

    @validator('phoneNumber')
    def validate_phone_number(cls, v):
        if not (v.startswith('+') or v.isdigit()):
            raise ValueError("Le numéro de téléphone doit être au format international ou national.")
        return v
