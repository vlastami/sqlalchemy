from sqlalchemy import  Table, Column, Integer, DECIMAL, String, ForeignKey

def create_db(engine, metadata):
    tab_markets = Table(
        "markets",
        metadata,
        Column("market_id", Integer, primary_key=True),
        Column("full_name", String(128)),
        Column("location", String(32), nullable=False)
    )
    tab_investors = Table(
        "investors",
        metadata,
        Column("investor_id", Integer, primary_key=True),
        Column("first_name", String(16), nullable=False),
        Column("surname", String(16), nullable=False),
        Column("first_name", String(16), nullable=False),
        Column("cash_CZK", DECIMAL(10,2)),
        Column("cash_EUR", DECIMAL(10, 2)),
        Column("cash_USD", DECIMAL(10, 2))

    )
    tab_symbols = Table(
        "symbols",
        metadata,
        Column("symbol_id", Integer, primary_key=True),
        Column("full_name", String(32), nullable=False),
        Column("dollar_value", DECIMAL(10,2)),
        Column("market_id", ForeignKey("tab_markets.market_id"))
    )
    tab_investor_symbol = Table(
        "investor_symbol",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("investor_id", ForeignKey("tab_investors.investor_id"), nullable=False),
        Column("symbol_id", ForeignKey("tab_symbols.symbol_id"),nullable=False),
        Column("share_amount", Integer)
    )
    tab_exchange_rates = Table(
        "exchange_rates",
        metadata,
        Column("rate_id", Integer, primary_key=True),
        Column("rate", DECIMAL(10,2), nullable=False)
    )


    with engine.begin() as conn:
        metadata.create_all(conn)
        conn.commit()

