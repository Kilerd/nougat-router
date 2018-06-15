import pytest
from nougat import TestClient
from nougat_router import *
from functools import wraps


class TestFeature:

    @pytest.mark.asyncio
    async def test_decorator(self, app, router, port):

        def return_other_things(controller):

            @wraps(controller)
            async def decorator(cls):
                cls.response.type = 'text/plain'

                return 'hello', 200

            return decorator

        class MainRestRouting(RestRouting):

            @get('/')
            @return_other_things
            async def static_route(self):
                return 'hello world'

        router.add(MainRestRouting)
        app.use(router)

        async with TestClient(app, port) as client:
            res = await client.get('/?name=world')
            assert res.text == 'hello'

            res = await client.get('/')
            assert res.text == 'hello'

    @pytest.mark.asyncio
    async def test_custom_response_type(self, app, router, port):

        def login_require(controller):
            @wraps(controller)
            async def decorator(cls):

                cls.response.type = 'text/plain'

                return 'no', 401

            return decorator

        class MainRestRouting(RestRouting):

            @get('/')
            @login_require
            async def static_route(self):
                return 'hello world'

        router.add(MainRestRouting)
        app.use(router)

        async with TestClient(app, port) as client:
            res = await client.get('/?name=world')
            assert res.text == 'no'
            assert res.status == 401
            assert res.headers.get('Content-Type') == 'text/plain;charset=utf-8'
