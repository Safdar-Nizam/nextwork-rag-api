import requests

def test_hug_query():
    response = requests.post("http://127.0.0.1:8000/query?q=What is Hug?")
    
    if response.status_code != 200:
        raise Exception(f"Server returned {response.status_code}: {response.text}")
    
    answer = response.json()["answer"]

    # Check for key concepts
    assert "non-profit" in answer.lower(), "Missing 'non-profit' keyword"
    assert "community" in answer.lower(), "Missing 'community' keyword"

    print("✅ HUG query test passed")

if __name__ == "__main__":
    test_hug_query()
    print("All semantic tests passed!")
