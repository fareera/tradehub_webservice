# -----------------------------------------------------------------------------
# File Name: get_table_class.py
# Copyright: 2020.03 Shanghai Mowen Technology Co., Ltd
# Author:    Jason. Yao
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import datetime
from peewee import (
    Table,
    PostgresqlDatabase,
    Model,
    CharField,
    IntegerField,
    DateTimeField,
    DecimalField,
    BigIntegerField)
# -----------------------------------------------------------------------------
# Globals
# -----------------------------------------------------------------------------

DBCONN = PostgresqlDatabase('mwmarketdata', **{
    'host': 'mowentech.cn',
    'port': '50000',
    'user': 'fwang',
    'password': 'wang123',
})
CN_FUTURE_EXCHANGES = ('cffex', 'shfe', 'dce', 'czce', "ine",
                       "nib")
period_dict = {
    1: "1min",
    2: "5min",
    3: "15min",
    4: "30min",
    5: "60min",
}
stock_product_type = 1
future_product_type = 2


# ---------------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
def createCandlelinePeeweeClass(tablename: str) -> type:
    meta_cls = type('Meta', (), {
        'primary_key': False,
        'database': DBCONN,
        'table_name': tablename,
        'schema': 'test_candleline'
    })

    fields = {
        'tradedate': IntegerField(null=False),
        'tradingday': IntegerField(null=False),
        'exchange_id': CharField(max_length=20, null=False),
        'instrument_id': CharField(max_length=20, null=False),
        'start_time': CharField(max_length=10, null=False),
        'stop_time': CharField(max_length=10, null=False),
        'seq': IntegerField(),
        'open_price': DecimalField(max_digits=20, decimal_places=3),
        'close_price': DecimalField(max_digits=20, decimal_places=3),
        'highest_price': DecimalField(max_digits=20, decimal_places=3),
        'lowest_price': DecimalField(max_digits=20, decimal_places=3),
        'volume': IntegerField(null=False),
        'product_info': IntegerField(null=False),
        'period': IntegerField(null=False),
        'turnover': DecimalField(max_digits=20, decimal_places=3),
        'update_time': DateTimeField(default=datetime.datetime.now),
        'Meta': meta_cls
    }

    for cn_future_exchange_id in CN_FUTURE_EXCHANGES:
        if cn_future_exchange_id in tablename:
            fields['settlement_price'] = DecimalField(max_digits=20, decimal_places=3)
            fields['total_open_interest'] = BigIntegerField(null=False)
            break
    return type(tablename, (Model,), fields)

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------