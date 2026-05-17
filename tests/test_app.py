import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

# Test Case 1: Menampilkan semua task
def test_get_tasks(client):
    rv = client.get("/tasks")
    assert rv.status_code == 200
    assert "tasks" in rv.get_json()

# Test Case 2: Sukses membuat task baru
def test_create_task_success(client):
    rv = client.post("/tasks", json={"title": "Membeli Buku"})
    assert rv.status_code == 201
    assert rv.get_json()["title"] == "Membeli Buku"

# Test Case 3: Gagal membuat task karena tidak ada title
def test_create_task_invalid(client):
    rv = client.post("/tasks", json={})
    assert rv.status_code == 400

# Test Case 4: Filter task berdasarkan status Pending
def test_filter_tasks_pending(client):
    rv = client.get("/tasks/filter?status=Pending")
    assert rv.status_code == 200
    assert len(rv.get_json()["filtered_tasks"]) >= 1

# Test Case 5: Filter task berdasarkan kata kunci pencarian
def test_filter_tasks_search(client):
    rv = client.get("/tasks/filter?search=DevOps")
    assert rv.status_code == 200
    assert len(rv.get_json()["filtered_tasks"]) == 1