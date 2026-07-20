from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_root_page_uses_static_asset_paths():
    response = client.get("/")

    assert response.status_code == 200
    assert 'src="/static/app.js"' in response.text
    assert 'href="/static/styles.css"' in response.text
