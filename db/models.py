from peewee import *

database = PostgresqlDatabase('mwmarketdata', **{'host': 'mowentech.cn', 'port': 50000, 'user': 'fwang', 'password': 'wang123'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class FuturesInstrumentReference(BaseModel):
    c_months_desc = CharField(null=True)
    cc_type = CharField(null=True)
    ce_multiplier = CharField(null=True)
    code_id = CharField(null=True)
    contract_value_desc = CharField(null=True)
    d_data_desc = CharField(null=True)
    delist_date = CharField(null=True)
    dl_month = CharField(null=True)
    dmean_desc = CharField(null=True)
    down_limit_price = CharField(null=True)
    dsite_desc = CharField(null=True)
    ename = CharField(null=True)
    exchange_id = CharField(null=True)
    fs_p_uint = CharField(null=True)
    ft_margins = CharField(null=True)
    full_name = CharField(null=True)
    l_price = CharField(null=True)
    l_tdl_date = CharField(null=True)
    list_date = CharField(null=True)
    lt_date_hour_desc = CharField(null=True)
    lt_dated_desc = CharField(null=True)
    max_price_fluct_desc = CharField(null=True)
    mf_price = CharField(null=True)
    name = CharField(null=True)
    p_uint = CharField(null=True)
    post_limit_desc = CharField(null=True)
    pre_settle_price = CharField(null=True)
    rtd = CharField(null=True)
    security_id = CharField(null=True)
    security_type = CharField(null=True)
    source_type = CharField(null=True)
    t_hours_desc = CharField(null=True)
    t_uint = CharField(null=True)
    trading_day = CharField(null=True)
    type_code = CharField(null=True)
    underlying_security_id = CharField(null=True)
    up_limit_price = CharField(null=True)
    update_time = DateTimeField(null=True)

    class Meta:
        table_name = 'futures_instrument_reference'
        schema = 'instrument'
        primary_key = False

class StocksInstrumentReference(BaseModel):
    exchange_id = CharField(null=True)
    instrument_id = CharField(null=True)
    lower_limit_price = DecimalField(null=True)
    name = CharField(null=True)
    pre_close_price = DecimalField(null=True)
    status = IntegerField(null=True)
    trading_day = CharField(null=True)
    type = IntegerField(null=True)
    update_time = DateTimeField(null=True)
    upper_limit_price = DecimalField(null=True)

    class Meta:
        table_name = 'stocks_instrument_reference'
        schema = 'instrument'
        primary_key = False

