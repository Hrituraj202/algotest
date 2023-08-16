from database.query import query_get, query_put, query_update
from .models import TradeUpdateRequestModel

def add_trade(trade_model: TradeUpdateRequestModel):
    query_put("""
                INSERT INTO trade (
                    trade.user_id,
                    trade.asset,
                    trade.exchanges,
                    trade.profit_percent,
                    trade.timestamp
                ) VALUES (%s,%s,%s,%s,%s)
                """,
              (
                  trade_model.user_id,
                  trade_model.asset,
                  trade_model.exchanges,
                  trade_model.profit_percent,
                  trade_model.timestamp
              )
              )
    return true

def get_all_trades():
    trade = query_get("""
        SELECT  
            trade.id,
            trade.user_id,
            trade.asset,
            trade.exchanges,
            trade.profit_percent,
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
            trade.profit_percent,
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
            trade.profit_percent,
            trade.timestamp
        FROM trade 
        WHERE user_id = %s
        """, (id))
    return trade
