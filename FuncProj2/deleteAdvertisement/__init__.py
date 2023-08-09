import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://faruqcosmodbaccount:SWaChivtxnmUCI48Mz5XEMVxwcT9elPkNdvSyWaevnv6yz9DdoZno3mDzbKa5AhKjxztE8i51sj0ACDbvmeBYg==@faruqcosmodbaccount.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@faruqcosmodbaccount@"
            client = pymongo.MongoClient(url)
            database = client['FunApp01DB']
            collection = database['AdvCollection01']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
