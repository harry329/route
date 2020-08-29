Root url - https://damp-journey-78807.herokuapp.com
To run locally set - `export FLASK_APP="app.py"` and then do `flask run`

There are two resourses in this api - route & business, so there are total of 10 endpoints. 5 for route resourcse and 5 fro business resource.
All the endpoints are protected by authorization and roles assigned to users.

I have added postman collection with appropriate auth tokens for each endpoint( both route & business).
As a reviewer if you want to run the app loclly , set FLASK_APP=app.py and then do flask run to run the app.
If you want to test the points run `python test_app.py` from root folder.
If you want to test against heroku endpoints, just import the postman collection and hit the respective endpoints.


There are three roles defined for this app & corresponding permissions with each role which described following -

1) admin -   "permissions": ["add:business","add:route","delete:business","delete:route","read:businesses","read:routes","update:business","update:route"]
   admin role has all the permissons for all the endpoits.
2) route-admin  -   "permissions": ["add:route","delete:route","read:routes","update:route"]
   route-admin has permission only for /route endpoints
3) business-admin  -   "permissions": ["add:business","delete:business","read:businesses","update:business"]
   business-admin role has permissions only for /business endpoints
