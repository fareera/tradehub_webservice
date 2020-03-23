# -----------------------------------------------------------------------------
# File Name: manager.py
# Copyright: 2020.03 Shanghai Mowen Technology Co., Ltd
# Author:    Jason. Yao
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

import aiohttp_cors
from aiohttp import web

from app.instrumentApi import instrumentapiroutes
from app.testapi import testapiroutes

# -----------------------------------------------------------------------------
# Globals
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    app = web.Application()

    app.add_routes(testapiroutes)
    app.add_routes(instrumentapiroutes)
    # Add all resources to `CorsConfig`.
    # 支持跨域
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    # Configure CORS on all routes.
    for route in list(app.router.routes()):
        cors.add(route)
    web.run_app(app, port=10003)
