from fastapi.testclient import TestClient
import pytest
import uuid
from backend.main_test import app
import requests
from fastapi.testclient import TestClient
class TestTeacher:
    url = "/teacher"
    client = TestClient(app)

    @pytest.mark.run_this_test
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "input",
        [
            (
                {
                    "name" :"Marcos",
                    "lastname":"Gonzales",
                    "username":"marquitos",
                    "specialty" : "python",
                    "contract_type":"undefined",
                    "experience" :20,
                    "email":"marquitos@gmail.com",
                    "list_of_subjects" :[],
                    "salary" : 8000,
                }
            ),
        ]
    )
    async def test_create_teacher(
        self, 
        client,
        input: dict,
    ):
        response = self.client.post(
                self.url,
                json=input,
                headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsdWlzYSIsInVzZXJfaWQiOiJlYzA0NDVmOC1mZDI1LTRiMjYtYjA1ZS1iNzcwNjdmZmJlZTkiLCJyb2xlcyI6WyJzZWNyZXRhcnkiXSwidHlwZSI6InNlY3JldGFyeSIsImV4cCI6MTczODU3NzM5Nn0.3euffT0m8VmQd93di9gx9RPwMOEXEhWOvlt9EP4UuHE"}
            )
        
        print(response.json())
        response_json = response.json()
        assert response.status_code == 201
        assert response_json['email'] == input['email']

    