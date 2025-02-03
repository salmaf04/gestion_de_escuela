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
        input: dict
    ):
        secretary = SecretaryFactory.create()
        
        access_token = create_access_token(
        data={
            "sub": "luisafer",
            "user_id" : "e06236c5-6639-4b48-8942-1acc6319e392",
            "roles": "[secretary]",
            "type": 'secretary'
        }
        )

        response = self.client.post(
                self.url,
                json=input,
                headers={"Authorization": f"Bearer {access_token}"}
            )
        
    
        
        print(response.json())
        response_json = response.json()
        assert response.status_code == 201
        assert response_json['email'] == input['email']

    