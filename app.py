from flask import Flask, jsonify,render_template,request, Response
import final
import json
import pymongo
from bson.objectid import ObjectId
app = Flask(__name__)


try:
    mongo = pymongo.MongoClient(
        host= "localhost",
        port= 27017,
        serverSelectionTimeoutMS= 1000
    )
    mongo.server_info()  #trigger exception if cannot connect to the database


    db= mongo.crowdSource

except:
    print("ERROR - cannot connect to the database")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/createTask',methods=["GET"])
def get_tasks():
    try:
        data = list(db.tasks.find())
        # print(data)
        for user in data:
            user["_id"] = str(user["_id"])

        return {"data":data}
        # return render_template('requestors.html', lis=list_data)
    except Exception as ex:
        print(ex)
        return Response(
            response = json.dumps(
                {"message":"cannot read tasks",}),
            status=500,
            mimetype="application/json"
        )


@app.route('/createTask',methods=["POST"])
def create_task():
    try:
        # newtask= {"tName":"climate-task", 
        #             "tDescribe":"how is the climate?",
        #             "TAmount": 100,
        #             }
        walletAddress = request.form['wAddress']
        taskName= request.form['tName']
        taskDescription = request.form['tDescription']
        tAmount = request.form['tAmount']
        # final.createTask(taskName,taskDescription,tAmount)
        newtask={"requestorAddress" : walletAddress,
                "tName":taskName,
                "tDescription": taskDescription,
                "tAmount":int(tAmount),
                "reportIDs":[],
                "reportSubmitterAddress":[]
                }
        dbResponse= db.tasks.insert_one(newtask)
        print(newtask)
        # for attr in dir(dbResponse):
        #     print(attr)
        # return render_template('allTasks.html',"task created")
        return Response(
            response = json.dumps(
                {"message":"task created",
                "id":f"{dbResponse.inserted_id}"
                }),
            status=200,
            mimetype="application/json"
        )
    
    except Exception as ex:
        print(ex)

# def updateReportIDinTasks(reportID):
#     filter={'_id':task_id}
#     newvalues = { "$push": { "reportIDs": reportID } }
#     db.tasks.updateOne(filter,newvalues)

@app.route('/addReport/<tid>',methods=["POST"])
def addReport(tid):
    try:
        walletAddress = request.form['wAddress']
        reportName=request.form['rName']
        reportContent= request.form['rContent']
        # final.addReport(walletAddress,reportName,reportContent)
        newReport={"workerAddress" : walletAddress,
                "rName":reportName,
                "rContent": reportContent,
                "task_id":tid,
                "reviewIDs":[],
                }
        print('------------------')
        print(db.reports["workerAddress"])
        print('------------')
        worker_found = db.reports.find_one({"workerAddress": walletAddress, 
                                          "task_id": tid  })
        if worker_found:
            print(worker_found)
            return render_template('index.html',msg="you have already submitted the report")
        dbResponse= db.reports.insert_one(newReport)
        # updateReportIDinTasks(dbResponse.inserted_id)
        print(newReport["workerAddress"])
        if dbResponse:
            print(tid)
            r=db.tasks.update_one({'_id':ObjectId(tid)},
                                    { "$push": { 
                                            "reportIDs": dbResponse.inserted_id,
                                            "reportSubmitterAddress":newReport["workerAddress"]
                                    } })
            print('updated is ', r)

        print(dbResponse.inserted_id)
        print(type(dbResponse.inserted_id))
        # for attr in dir(dbResponse):
        #     print(attr)
        # return render_template('reviews.html')
        return Response( 
            response = json.dumps(
                {"message":"report created",
                "id":f"{dbResponse.inserted_id}"
                }),
            status=200,
            mimetype="application/json"
        )
    
    except Exception as ex:
        print(ex)

@app.route('/addReport',methods=["GET"])
def getReport():
    try:
        data = list(db.reports.find())
        print(data)
        for user in data:
            user["_id"] = str(user["_id"])

        return {"data":data}
        # return render_template('requestors.html', lis=list_data)
    except Exception as ex:
        print(ex)
        return Response(
            response = json.dumps(
                {"message":"cannot read tasks",}),
            status=500,
            mimetype="application/json"
        )    


@app.route('/alltasks')
def allTasks():
    tasks_data = get_tasks()["data"]
    # reports_data = getReport()["data"]
    # print(tasks_data)
    # for task in tasks_data:
    #     print('task is ', task)
    #     for report in reports_data:
    #         print('report is', report)
            

    return render_template('allTasks.html', lis=tasks_data)
    
@app.route('/requestors')
def requestors():
    return render_template('requestors.html')

@app.route('/workers/<_id>/<tName>', methods=['GET','POST'])
def workers(_id,tName):
    task_name= tName
    global task_id
    task_id=_id
    return render_template('workers.html', tid=task_id, tname=task_name)

@app.route('/allreports',methods=["GET","POST"])
def allReports():
    tasks_data = get_tasks()["data"]
    list_data = getReport()["data"]
    # print(list_data)
    return render_template('allReports.html', reports=list_data, tasks= tasks_data)

@app.route('/viewReport/<_id>/<tName>', methods=['GET','POST'])
def viewReport(_id,tName):
    task_name= tName
    global task_id
    task_id=_id
    list_data = getReport()["data"]

    return render_template('viewReport.html',reports=list_data,tid=task_id, tname=task_name)


# @app.route('/addReview/{{rid}}', methods=['GET','POST'])
# def createReviews(rid):
#     try:
#         reportId = rid
#         reportRating=request.form['rRating']
#         reportComment= request.form['rComment']
#         reviwerAddress = request.form['wAddress']

#         newReview={
#                 "reportId":reportId,
#                 "reportRating": reportRating,
#                 "reportComment":reportComment,
#                 "reviewSubmitterAddress": reviwerAddress
#                 }
#         dbResponse= db.reviews.insert_one(newReview)
#         # updateReportIDinTasks(dbResponse.inserted_id)
#         if dbResponse:
#             r=db.reports.update_one({'_id':ObjectId(rid)},
#                                     { "$push": { 
#                                             "reportIDs": dbResponse.inserted_id
#                                     } })
#             print('updated is ', r)

#         print(dbResponse.inserted_id)
#         print(type(dbResponse.inserted_id))
#         # for attr in dir(dbResponse):
#         #     print(attr)
#         # return render_template('reviews.html')
#         return Response( 
#             response = json.dumps(
#                 {"message":"review created",
#                 "id":f"{dbResponse.inserted_id}"
#                 }),
#             status=200,
#             mimetype="application/json"
#         )
    
#     except Exception as ex:
#         print(ex)

# @app.route('/requestors')
# def requestors():
#     list_data = get_tasks()["data"]
#     print(list_data)
#     return render_template('requestors.html', lis=list_data)

# @app.route('/home',methods=['POST'])
# def home():
#     if request.method == "POST":
#         taskName= request.form.get('tName')
#         taskDescription = request.form.get('tDescription')
#         tAmount = request.form.get('tAmount')
#     # final.createTask(taskName,taskDescription,tAmount)
#     return render_template('home.html',n=taskName,d=taskDescription,a=tAmount)
#     # return render_template('home.html', m=msg)



# @app.route('/requestors',methods=['GET','POST'])
# def requestors():
#     # return render_template('requestors.html')
#     if request.method == "POST":
#         taskName= request.form.get('tName')
#         taskDescription = request.form.get('tDescription')
#         tAmount = request.form.get('tAmount')
#     print(taskName,taskDescription,tAmount)
#     return render_template('requestors.html')
    # return render_template('requestors.html', n=taskName,d=taskDescription,a=tAmount)

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(port=80,debug=True)