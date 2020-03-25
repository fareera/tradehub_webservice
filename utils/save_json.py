# -----------------------------------------------------------------------------
# File Name: save_json.py
# Copyright: 2020.03 Shanghai Mowen Technology Co., Ltd
# Author:    Jason. Yao
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import datetime
import os

# -----------------------------------------------------------------------------
# Globals
# -----------------------------------------------------------------------------
import time

from db.models import FuturesInstrumentReference

PREVIOUS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------
def read_csv():
    res_list = []
    with open(os.path.join(PREVIOUS_PATH, "future_ref.json"), "rb") as f:
        json_ref = eval(f.read())
    json_ref = json_ref["RECORDS"]
    for data in json_ref:
        data["trading_day"] = "20200325"
        data["security_id"] = data["security_id"].lower()
        data["exchange_id"] = data["exchange_id"].lower()
        data["update_time"] = datetime.datetime.now()
        res_list.append(data)
    FuturesInstrumentReference.insert_many(
        res_list
    ).execute()

    res = FuturesInstrumentReference.select(FuturesInstrumentReference.cc_type)
    print(len(res))


# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    read_csv()
