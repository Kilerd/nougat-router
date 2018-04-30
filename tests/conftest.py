import pytest
from nougat import Nougat
from nougat_router import Router


@pytest.fixture
@pytest.mark.asyncio
def app() -> 'Nougat':

    return Nougat()


@pytest.fixture
def router():
    return Router()


@pytest.fixture
@pytest.mark.asyncio
def port(unused_tcp_port) -> int:

    return unused_tcp_port
