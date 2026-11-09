def test_dashboard_shows_status_counts_and_all_employees(client):
    html = client.get("/").get_data(as_text=True)

    assert "Bekleyen: <b>4</b>" in html
    assert "Onaylanan: <b>1</b>" in html
    assert "Reddedilen: <b>3</b>" in html
    for name in [
        "Ayse Yilmaz",
        "Mehmet Demir",
        "Zeynep Kaya",
        "Ahmet Celik",
        "Elif Sahin",
    ]:
        assert name in html
