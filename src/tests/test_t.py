import pytest
from httpx import AsyncClient
from ..main import app


@pytest.fixture
async def async_app_client():
    async with AsyncClient(app=app, base_url='http://127.0.0.1:8000/') as client:
        return client


@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient() as client:
        r = await client.post('http://127.0.0.1:8000/auth/')
        assert r.status_code == 200
