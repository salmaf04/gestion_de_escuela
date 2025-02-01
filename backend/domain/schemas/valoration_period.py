from pydantic import BaseModel

class ValorationPeriodChangeRequest(BaseModel):
    open : bool | None = None