import datetime
import json

from aiohttp import web


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)


def make_resp(errno=0, errmsg="ok.", **kwargs):
    resp = {
        "error_no": errno,
        "error_msg": errmsg
    }
    resp.update(kwargs)
    return web.Response(text=json.dumps(resp, ensure_ascii=False, cls=DateEncoder),
                        content_type="application/json")
