import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_create_user():
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:
        response = await client.post(
            "/users",
            json={
                "name": "Guru",               
                "email": "guru@example.com"    
            }
        )

    print(response.json())  

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Guru"
    assert data["email"] == "guru@example.com"
    assert "id" in data
