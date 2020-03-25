# -----------------------------------------------------------------------------
# File Name: instrumentApi.py
# Copyright: 2020.03 Shanghai Mowen Technology Co., Ltd
# Author:    Jason. Yao
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import json
import time

from aiohttp import web

from db.models import FuturesInstrumentReference, StocksInstrumentReference
from utils.get_table_class import createCandlelinePeeweeClass
from utils.makeresp import make_resp

# -----------------------------------------------------------------------------
# Globals
# -----------------------------------------------------------------------------
instrumentapiroutes = web.RouteTableDef()


# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
# 获取合约列表
#         {
#             "exchange_id": "CFFEX",
#             "id": "IF2003",
#             "type": 2,
#             "status": 0,
#             "name": "IC2003",
#             "pre_close_price": 4191.80,
#             "pre_settlement_price": 4194.60,
#             "upper_limit_price": 4614.0,
#             "lower_limit_price": 3775.2,
#             "update_time": "2020-03-06 08:34:03"
#         }
@instrumentapiroutes.get('/instrument')
async def acquire_instrument_list(request):
    reader = await request.read()
    reader = json.loads(reader)
    exchange_id = reader["exchange_id"]
    type = reader["type"]
    status = reader["status"]


# 获取合约参考信息
@instrumentapiroutes.get('/instrument_ref')
async def acquire_instrument_reference_info(request):
    reader = await request.read()
    reader = json.loads(reader)
    symbol_list = reader["symbol_list"]
    content = {}
    for symbol in symbol_list:
        content_list = []
        symbol_split = symbol.split(".")
        instrument_id = symbol_split[0].lower()
        exchange_id = symbol_split[1].lower()
        print(instrument_id,exchange_id)
        futures_query_res = FuturesInstrumentReference.select().where(
            (FuturesInstrumentReference.security_id == instrument_id) &
            (FuturesInstrumentReference.exchange_id == exchange_id) &
            (FuturesInstrumentReference.trading_day == str(time.strftime("%Y%m%d", time.localtime(time.time()))))
        ).dicts()
        stock_query_res = StocksInstrumentReference.select().where(
            (StocksInstrumentReference.instrument_id == instrument_id) &
            (StocksInstrumentReference.exchange_id == exchange_id) &
            (StocksInstrumentReference.trading_day == str(time.strftime("%Y%m%d", time.localtime(time.time()))))
        ).dicts()
        for vf in futures_query_res:
            content_list.append(vf)
        for vs in stock_query_res:
            content_list.append(vs)
        content[symbol] = content_list

    return make_resp(content=content)



# data = [
#         {
#             "exchange_id": "SH",
#             "id": "600570",
#             "type": 1,
#             "status": 0,
#             "name": "恒生电子",
#             "volume": 98500,
#             "amount": 10270000000,
#             "pre_close_price": 104.69,
#             "open_price": 104.69,
#             "current_price": 100.80,
#             "delta_price": -1.79,
#             "delta_amplitude": -0.0180,
#             "highest_price": 105.50,
#             "lowest_price": 100.00,
#             "upper_limit_price": 113.08,
#             "lower_limit_price": 92.52,
#             "update_time": "2020-03-05 10:34:03"
#         },
#         {
#             "exchange_id": "SZ",
#             "id": "002745",
#             "type": 1,
#             "status": 0,
#             "name": "木林森",
#             "volume": 45700,
#             "amount": 59700000,
#             "pre_close_price": 12.91,
#             "open_price": 12.91,
#             "current_price": 12.87,
#             "delta_price": -0.03,
#             "delta_amplitude": -0.0230,
#             "highest_price": 13.14,
#             "lowest_price": 12.81,
#             "upper_limit_price": 14.20,
#             "lower_limit_price": 11.62,
#             "update_time": "2020-03-05 10:34:04"
#         },
#         {
#             "exchange_id": "SHFE",
#             "id": "ZN2005",
#             "type": 2,
#             "status": 0,
#             "name": "沪锌2005",
#             "volume": 24545,
#             "amount": 19650000000,
#             "pre_close_price": 15970,
#             "open_price": 15995,
#             "current_price": 15995,
#             "delta_price": 25,
#             "delta_amplitude": 0.0160,
#             "highest_price": 16050,
#             "lowest_price": 15975,
#             "upper_limit_price": 16760,
#             "lower_limit_price": 15165,
#             "update_time": "2020-03-05 10:34:04"
#         },
#         {
#             "exchange_id": "CFFEX",
#             "id": "IF2003",
#             "type": 2,
#             "status": 0,
#             "name": "IF2003",
#             "volume": 42080,
#             "amount": 523870000000,
#             "pre_close_price": 4140.00,
#             "open_price": 4146.00,
#             "current_price": 4143.40,
#             "delta_price": 53.60,
#             "delta_amplitude": 0.0134,
#             "highest_price": 4156.20,
#             "lowest_price": 4116.40,
#             "upper_limit_price": 4497.40,
#             "lower_limit_price": 3679.80,
#             "update_time": "2020-03-05 10:34:04"
#         }
#     ]
# 获取合约行情快照
@instrumentapiroutes.get('/instrument_snapshot')
async def acquire_instrument_quote_snapshot(request):
    reader = await request.read()
    reader = json.loads(reader)
    symbol_list = reader["symbol_list"]


# 获取合约K线
@instrumentapiroutes.get('/instrument_candleline')
async def acquire_instrument_candleline(request):
    reader = await request.read()
    reader = json.loads(reader)
    filter_list = reader["filter"]
    content_dict = {}
    for filter in filter_list:
        content_list = []
        symbol_split = filter["symbol_id"].split(".")
        instrument_id = symbol_split[0].lower()
        exchange_id = symbol_split[1].lower()
        try:
            table_cls = createCandlelinePeeweeClass(f"{exchange_id}{instrument_id}")
            query_res = table_cls.select().where(
                (table_cls.tradedate>=int(filter["start_time"]))&
                (table_cls.tradedate<=int(filter["stop_time"]))&
                (table_cls.period == filter["period"])
            ).order_by(table_cls.tradedate).limit(filter["count"]).dicts()
            content_list = [i for i in query_res]
            content_dict[filter["symbol_id"]] = content_list
        except:
            pass
    return make_resp(content=content_dict)




# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------
