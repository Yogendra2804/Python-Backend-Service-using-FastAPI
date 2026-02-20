from pydantic import field_validator , BaseModel 

class Value(BaseModel):
    IIN : int 

    @field_validator("IIN")
    @classmethod
    def check_len(clv , data):
        if len(str(data)) != 6:
            return "Length should be exectly 6"
        return data