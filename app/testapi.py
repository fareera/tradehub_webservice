import json

from aiohttp import web

from utils.makeresp import make_resp

testapiroutes = web.RouteTableDef()
@testapiroutes.post('/api')
async def test(request):
    try:
        reader = await request.read()
        print(json.loads(reader))
        # reader = await request.multipart()
        # file = await reader.next()
        # filename = file.filename if file.filename else 'undefined'
        # size = 0
        # with open(filename, 'wb') as f:
        #     while True:
        #         chunk = await file.read_chunk()  # 默认是8192个字节。
        #         if not chunk:
        #             break
        #         size += len(chunk)
        #         f.write(chunk)
        return make_resp()

    except Exception as e:
        print(e)
        pass
