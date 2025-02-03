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
class TestStudent:
    url = "/student"
    
    @pytest.mark.run_this_test
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "input",
        [
            (
                {
                    "name" : "Rita",
                    "lastname" : "Suarez",
                    "age" : "20",
                    "email" : "rita@gmail.com",
                    "extra_activities":"true",
                    "username" : "rita",
                    "course_id" : "d44359a8-9881-4cdf-9336-d233e6ebcdfc"
                }
            ),
        ]
    )
    async def test_create_student(
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

        response = client.get(
            self.url,
            params= {
                "name" : "Rita",
            },
            headers={"Authorization": f"Bearer {access_token}"}
        )
        
        response_json = response.json()
        
        student = response_json.get("0")
        assert student.get('name') == "Rita"
        assert student.get('lastname') == "Suarez"
        assert student.get('age') == 20
        assert student.get('email') == "rita@gmail.com"
        assert student.get('extra_activities') == True
        assert student.get('username') == "rita"
    

       

