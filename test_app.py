from application import app

# def test_quick():
#   a = "jeff"
#   greeting = greet(a)
#   assert greeting == "Hi jeff"

def test_home_page():
    response = app.test_client().get('/')
    assert response.status_code == 200
    
def test_json_data(app.test_client()):
    response = app.test_client().post("/graphql", json={
        "query": """
            query User($id: String!) {
                user(id: $id) {
                    name
                    theme
                    picture_url
                }
            }
        """,
        variables={"id": 2},
    })
    assert response.json["data"]["user"]["name"] == "Flask"
