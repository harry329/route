Root url - https://damp-journey-78807.herokuapp.com


There are two resourses in this api - route & business, so there are total of 10 endpoints. 5 for route resourcse and 5 fro business resource.
All the endpoints are protected by authorization and roles assigned to users.

I have added postman collection with appropriate auth tokens for each endpoint( both route & business).
As a reviewer if you want to run the app loclly , set FLASK_APP=app.py and then do flask run to run the app.
If you want to test the points run `python test_app.py` from root folder.
If you want to test against heroku endpoints, just import the postman collection and hit the respective endpoints.
