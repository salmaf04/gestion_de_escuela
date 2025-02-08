from fastapi.testclient import TestClient
import pytest
import uuid
from backend.main_test import app
import requests
from fastapi.testclient import TestClient
from .conftest import SecretaryFactory
from backend.presentation.utils.auth import create_access_token
from sqlalchemy import ARRAY
from backend.domain.models.tables import Roles
class TestTeacher:
    url = "/teacher"
    
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
                    "subjects" :[],
                    "salary" : 8000,
                }
            ),
        ]
    )
    async def test_create_teacher(
        self, 
        client,
        input: dict
    ):
        access_token = create_access_token(
        data={
            "sub": "luisafer",
            "user_id" : "64080f97-db1a-4f30-a8f6-b29a096e44b7",
            "roles": "[secretary]",
            "type": 'secretary'
        }
        )

        response = client.post(
                self.url,
                json=input,
                headers={"Authorization": f"Bearer {access_token}"}
            )
        
        response_json = response.json()
        assert response.status_code == 201
        assert response_json['email'] == input['email']
        assert response_json['name'] == input['name']
        assert response_json['lastname'] == input['lastname']
        assert response_json['username'] == input['username']
        assert response_json['specialty'] == input['specialty']
        assert response_json['contract_type'] == input['contract_type']
        assert response_json['experience'] == input['experience']
        assert response_json['salary'] == input['salary']

        response = client.get(
            self.url,
            params= {
                "name" : "Marcos",
            },
            headers={"Authorization": f"Bearer {access_token}"}
        )

        assert response.status_code == 200
        assert response.json()[0]['name'] == "Marcos"

       

