from fastapi.testclient import TestClient
import pytest
import uuid
from backend.main import app

class TestTeacher:
    url = "/teacher"

    @pytest.mark.run_this_test
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "input",
        [
            (
                {
                    "name" :"Tipo",
                    "fullname":"Serio",
                    "username":"l",
                    "specialty" : "python",
                    "contract_type":"undefined",
                    "experience" :"20",
                    "email":"l@gmail.com",
                    "list_of_subjects" :[],
                    "salary" : 8000
                }
            ),
        ]
    )
    async def test_create_teacher(
        self, 
        client : TestClient,
        input: dict,
    ):
        response = client.post(
                self.url,
                json=input,
                headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsdWlzYSIsInR5cGUiOiJzZWNyZXRhcnkiLCJleHAiOjE3MzgxMzI1OTd9.QAv_mboyLJJb0i_uiPl0uKVdIY21fox0Huigpy2OkxU"}
            )
        
        response_json = response.json()
        assert response.status_code == 201
        assert response_json['email'] == input['email']

    