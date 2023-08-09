import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://faruqcosmodbaccount:SWaChivtxnmUCI48Mz5XEMVxwcT9elPkNdvSyWaevnv6yz9DdoZno3mDzbKa5AhKjxztE8i51sj0ACDbvmeBYg==@faruqcosmodbaccount.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@faruqcosmodbaccount@"
        client = pymongo.MongoClient(url)
        database = client['FunApp01DB']
        collection = database['AdvCollection01']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

