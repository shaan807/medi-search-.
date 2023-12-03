from pydantic import BaseModel, validator

class YourModel(BaseModel):
    field1: str
    field2: int

    @validator("*", pre=True, skip_on_failure=True)
    def check_values(cls, v, field, values, **kwargs):
        # Your validation logic here
        return v
