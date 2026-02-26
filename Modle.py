from pydantic import field_validator, BaseModel
from engine import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String


class Value(BaseModel):
    IIN: int

    @field_validator("IIN")
    @classmethod
    def check_len(clv, data):
        if len(str(data)) != 6:
            return "Length should be exectly 6"
        return data


class CARDS(Base):
    __tablename__ = "CARDS"

    bin_iin: Mapped[int] = mapped_column("BIN/IIN", Integer, primary_key=True)
    network_Scheme: Mapped[str] = mapped_column(
        "Network/Scheme", String, nullable=False
    )
    card_type: Mapped[str] = mapped_column("Card Type", String, nullable=False)
    card_category: Mapped[str] = mapped_column("Card Category", String, nullable=False)
    issuer: Mapped[str] = mapped_column("Issuer", String, nullable=False)

