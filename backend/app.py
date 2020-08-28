from flask import Flask, request, jsonify
from database.db_config import set_up_db
from database.freeway import Freeway
from database.business_entity import BusinessEntity
from database.freeway_business import freeway_business
from auth.auth import requires_auth, AuthError

app = Flask(__name__)
set_up_db(app)


def getApp():
    return app


@app.route("/")
def getApiInfo():
    return "An api to explore route options"


@app.route("/route", methods=["POST"])
@requires_auth("add:route")
def addRoute():
    route = request.get_json()
    freeway = Freeway(
        name=route["name"],
        start_state=route["start_state"],
        end_state=route["end_state"],
        length=route["length"],
    )
    freeway.insert()
    return jsonify({"success": True, "freeway": freeway.format()}), 201


@app.route("/route", methods=["GET"])
@requires_auth("read:routes")
def getRoutes():
    routes = Freeway.query.all()
    formatted_routes = [route.format() for route in routes]
    return jsonify({"success": True, "routes": formatted_routes})


@app.route("/route/<id>", methods=["GET"])
@requires_auth("read:routes")
def getRoute(id):
    route = Freeway.query.get(id).format()
    return jsonify({"success": True, "route": route})


@app.route("/route/<id>", methods=["DELETE"])
@requires_auth("delete:route")
def deleteRoute(id):
    route = Freeway.query.get(id)
    route.delete()
    return jsonify({"success": True, "id": id})


@app.route("/route/<id>", methods=["PATCH"])
@requires_auth("update:route")
def updateRoute(id):
    route = Freeway.query.get(id)
    update_route = request.get_json()
    for value in update_route:
        valToUpdate = update_route[value]
        if value == "name":
            route.name = valToUpdate
        elif value == "start_state":
            route.start_state == valToUpdate
        elif value == "end_state":
            route.end_state = valToUpdate
        elif value == "length":
            route.length = valToUpdate
    route.update()
    print(route.format())
    return jsonify({"success": True, "route": route.format()})


@app.route("/business", methods=["POST"])
@requires_auth("add:business")
def addBusiness():
    req = request.get_json()
    freeway = Freeway.query.get(req["freeway_id"])
    business = BusinessEntity(
        name=req["name"],
        state=req["state"],
        city=req["city"],
        zip=req["zip"],
        highways=req["highways"],
        type_of_business=req["type_of_business"],
        miles_away=req["miles_away"],
        avg_amt=req["avg_amt"],
        lat=req["lat"],
        lng=req["lng"],
    )
    freeway.business_entitys.append(business)
    freeway.insert()

    return jsonify({"success": True, "business_entity": business.format()}), 201


@app.route("/business", methods=["GET"])
@requires_auth("read:businesses")
def getBusinesses():
    businesses = BusinessEntity.query.all()
    formatted_businesses = [business.format() for business in businesses]
    return jsonify({"success": True, "businesses": formatted_businesses})


@app.route("/business/<id>", methods=["GET"])
@requires_auth("read:businesses")
def getBusiness(id):
    business = BusinessEntity.query.get(id)
    return jsonify({"success": True, "business_entity": business.format()})


@app.route("/business/<id>", methods=["DELETE"])
@requires_auth("delete:business")
def deleteBusiness(id):
    business = BusinessEntity.query.get(id)
    business.delete()
    return jsonify({"success": True, "business_id": id})


@app.route("/business/<id>", methods=["PATCH"])
@requires_auth("update:business")
def updateBusiness(id):
    business = BusinessEntity.query.get(id)
    update_business = request.get_json()
    for value in update_business:
        valToUpdate = update_business[value]
        if value == "name":
            business.name = valToUpdate
        elif value == "state":
            business.state == valToUpdate
        elif value == "city":
            business.city = valToUpdate
        elif value == "zip":
            business.zip = valToUpdate
        elif value == "type_of_business":
            business.type_of_business = valToUpdate
        elif value == "miles_away":
            business.miles_away = valToUpdate
        elif value == "avg_amt":
            business.avg_amt = valToUpdate
        elif value == "lat":
            business.lat = valToUpdate
        elif value == "lng":
            business.lng = valToUpdate
    business.update()
    print(business.format())
    return jsonify({"success": True, "route": business.format()})


@app.errorhandler(AuthError)
def unauthorized(error):
    return (
        jsonify(
            {
                "success": False,
                "error": error.status_code,
                "message": error.error,
            }
        ),
        error.status_code,
    )


@app.errorhandler(500)
def unprocessable500(error):
    return (
        jsonify({"success": False, "error": 500, "message": "Something went wrong"}),
        500,
    )


@app.errorhandler(400)
def unprocessable400(error):
    return jsonify({"success": False, "error": 400, "message": "Bad Request"}), 400


@app.errorhandler(404)
def unprocessable404(error):
    return (
        jsonify({"success": False, "error": 404, "message": "Resourse not found"}),
        404,
    )


if __name__ == "__main__":
    print("I am here")
    app.run()
