from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_unregister_existing_participant():
    activity_name = "Chess Club"
    email = "student@mergington.edu"

    activities[activity_name]["participants"].append(email)

    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]
