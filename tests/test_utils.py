import pytest
from nougat import TestClient
from nougat_router import *
from functools import wraps


class TestFeature:

    @pytest.mark.asyncio
    async def test_format_int(self, app, router, port):

        class MainRestRouting(RestRouting):

            @get('/')
            async def static_route(self):
                return 0

        router.add(MainRestRouting)
        app.use(router)

        async with TestClient(app, port) as client:
            res = await client.get('/?name=world')
            assert res.text == '0'

            res = await client.get('/')
            assert res.text == '0'
