from pydantic import BaseModel

class TradeUpdateRequestModel(BaseModel):
    user_id: int
    asset: str
    exchange: str
    profit: float
    timestamp: str

class TradeResponseModel(BaseModel):
    id: int
    user_id: int
    asset: str
    exchange: str
    profit: float
    timestamp: str