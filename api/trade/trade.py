from database.query import query_get, query_put, query_update
from .models import TradeUpdateRequestModel

def add_trade(trade_model: TradeUpdateRequestModel):
    query_put("""
                INSERT INTO trade (
                    trade.user_id,
                    trade.asset,
                    trade.exchanges,
                    trade.profit,
                    trade.timestamp
                ) VALUES (%s,%s,%s,%s,%s)
                """,
              (
                  trade_model.user_id,
                  trade_model.asset,
                  trade_model.exchanges,
                  trade_model.profit,
                  trade_model.timestamp
              )
              )
    return True

def get_all_trades():
    trade = query_get("""
        SELECT  
            trade.id,
            trade.user_id,
            trade.asset,
            trade.exchanges,
            trade.profit,
            trade.timestamp
        FROM trade
        """, ())
    return trade

def get_trade_by_id(id: int):
    trade = query_get("""
        SELECT 
            trade.id,
            trade.user_id,
            trade.asset,
            trade.exchanges,
            trade.profit,
            trade.timestamp
        FROM trade 
        WHERE id = %s
        """, (id))
    return trade

def get_trades_by_user_id(id: int):
    trade = query_get("""
        SELECT 
            trade.id,
            trade.user_id,
            trade.asset,
            trade.exchanges,
            trade.profit,
            trade.timestamp
        FROM trade 
        WHERE user_id = %s
        order by id desc
        limit 15 
        """, (id))
    return trade

def create_trade(id: int):
    user = get_user_by_email(user_model.email)
    if len(user) != 0:
        raise HTTPException(
            status_code=409, detail='Email user already exist.')
    hashed_password = auth_handler.encode_password(user_model.password)
    query_put("""
                INSERT INTO user (
                    first_name,
                    last_name,
                    email,
                    password_hash
                ) VALUES (%s,%s,%s,%s)
                """,
              (
                  user_model.first_name,
                  user_model.last_name,
                  user_model.email,
                  hashed_password
              )
              )
    user = get_user_by_email(user_model.email)
    return user[0]