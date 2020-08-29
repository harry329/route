import os
import unittest
import json
import pytest
from flask_sqlalchemy import SQLAlchemy
from app import getApp
from database.freeway import Freeway
from database.business_entity import BusinessEntity
from database.freeway_business import freeway_business


class RouteTestCase(unittest.TestCase):
    def setUp(self):
        self.app = getApp()
        self.client = self.app.test_client
        self.headers = {
            "Authorization": "Bearer {}".format(
                "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1hYTc1d19xS0lnYW5UcUdHcUNYdCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qdS1sdjZpbS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDExMTk2MTMyMDUwMTIwNTY1NzIiLCJhdWQiOlsiY29tLnJvdXRlLmJ1c2luZXNzIiwiaHR0cHM6Ly9kZXYtanUtbHY2aW0udXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU5ODYyNTMzOSwiZXhwIjoxNTk4NzExNzM5LCJhenAiOiJlS0t4Wkdrcno0b2t6aGxKejFmc0hNMUpLcEt5SDNieSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6YnVzaW5lc3MiLCJhZGQ6cm91dGUiLCJkZWxldGU6YnVzaW5lc3MiLCJkZWxldGU6cm91dGUiLCJyZWFkOmJ1c2luZXNzZXMiLCJyZWFkOnJvdXRlcyIsInVwZGF0ZTpidXNpbmVzcyIsInVwZGF0ZTpyb3V0ZSJdfQ.EMdmPZZwz97kbnqFA3vNJOL61dRwqnru-bRgWmWgWX-aNJvZo3LZ9nKej4IqRGqpJW6y7nt17Er1j_K7hey_n57y1IVyMZArNTuYKsjcaz5WZWvzyNXifhSuTloa8VHo7YAW8ZR6GzJ65bLTaF4GF57G62nLPmIkr_O3WDu1SFN0pi69Ui1riNSNppbT9EYTJzncGh6RvDDUPlvUU9PSnXVwg8TNezA619kCIySMJCqzRJNsEQmYdhrMOLOd9GbJuTLS2fJdAhHrhRooxNQbwF3XyOsADDEwmIEj3R5WEU5i3ic7RCgRrZFtkQCDxfYlcTDKD4c1iNYa_adRMOxV-g"
            )
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_add_route(self):
        res = self.client().post(
            "/route",
            headers=self.headers,
            json={
                "name": "I-76",
                "start_state": "NYC",
                "end_state": "California",
                "length": "660 miles",
            },
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data["success"], True)

    def test_get_routes(self):
        res = self.client().get("/route", headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(data["success"], True)
        self.assertEqual(res.status_code, 200)

    def test_get_route(self):
        res = self.client().get("/route/2", headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(data["success"], True)
        self.assertEqual(res.status_code, 200)

    def test_update_route(self):
        res = self.client().patch(
            "/route/2", headers=self.headers, json={"name": "I-255"}
        )
        data = json.loads(res.data)
        self.assertEqual(data["success"], True)
        self.assertEqual(res.status_code, 200)

    # def test_delete_route(self):
    #     res = self.client().delete("/route/1", headers=self.headers)
    #     data = json.loads(res.data)
    #     self.assertEqual(data["success"], True)
    #     self.assertEqual(res.status_code, 200)

    def test_add_business(self):
        res = self.client().post(
            "/business",
            headers=self.headers,
            json={
                "name": "Harry's  Second Dinner",
                "state": "IL",
                "city": "Chicago",
                "zip": "60601",
                "highways": "I-55",
                "type_of_business": "Restaurant",
                "miles_away": "22 miles",
                "avg_amt": "$ 25",
                "lat": "18",
                "lng": "18",
                "freeway_id": 2,
            },
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data["success"], True)

    def test_get_businesses(self):
        res = self.client().get("/business", headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(data["success"], True)
        self.assertEqual(res.status_code, 200)

    def test_get_business(self):
        res = self.client().get("/business/2", headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(data["success"], True)
        self.assertEqual(res.status_code, 200)

    def test_update_business(self):
        res = self.client().patch(
            "/business/2",
            headers=self.headers, json={"name": "Rupi's Second diner"}
        )
        data = json.loads(res.data)
        self.assertEqual(data["success"], True)
        self.assertEqual(res.status_code, 200)

    # def test_delete_business(self):
    #     res = self.client().delete("/business/1", headers=self.headers)
    #     data = json.loads(res.data)
    #     self.assertEqual(data["success"], True)
    #     self.assertEqual(res.status_code, 200)

    def test_401(self):
        res = self.client().get("/route/1")
        self.assertEqual(res.status_code, 401)

    def test_404(self):
        res = self.client().get("/routes/100")
        self.assertEqual(res.status_code, 404)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
