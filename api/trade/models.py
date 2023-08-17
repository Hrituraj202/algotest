from pydantic import BaseModel

class TradeUpdateRequestModel(BaseModel):
    user_id: int
    asset: str
    exchanges: str
    profit: str
    timestamp: str

class TradeResponseModel(BaseModel):
    id: int
    user_id: int
    asset: str
    exchanges: str
    profit: str
    timestamp: str