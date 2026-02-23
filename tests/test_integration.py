import pytest

@pytest.mark.asyncio
async def test_create_user(client):
    response = await client.post(
        "/users",
        params={"email": "test@mail.com"}
    )
    assert response.status_code == 201
    assert response.json()["email"] == "test@mail.com"




 @pytest.mark.asyncio
async def test_get_user(client):
    response = await client.get("/users/1")
    assert response.status_code == 200

