from pathlib import Path


def test_activity_card_renders_participants_list():
    app_js = Path("src/static/app.js").read_text()

    assert "participants-list" in app_js
    assert "Participants:" in app_js
