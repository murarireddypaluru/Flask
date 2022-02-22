from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = [{
    "id":1,
    "Contact":u"9464947549",
    "Name":u"Murari",
    "done":False
},
{
    "id":2,
    "Contact":u"3474875743",
    "Name":u"Ms.Anmol, My Coding Teacher",
    "done":False 
},
{
    "id":3,
    "Contact":u"2937844852",
    "Name":u"My Mom, Mamatha Paluru",
    "done":False 
},
{
    "id":4,
    "Contact":u"2643982374",
    "Name":u"My Dad, Madhu Paluru",
    "done":False 
}]
@app.route("/add-data", methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide data"
        },400)
    task = {
        "id":tasks[-1]["id"]+1,
        "Contact":request.json["Contact"],
        "Name":request.json.get("Name", ""),
        "done": False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"tasks added successfully"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })

if(__name__ == "__main__") :
    app.run(debug = True)

