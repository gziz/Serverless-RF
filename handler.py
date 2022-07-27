import json
import pickle

def predict_rf(data):
    loaded_rf = pickle.load(open("./models/random_forest.pkl", 'rb') )
    predictions = loaded_rf.predict(data)

    return predictions


def handler(event, context):
    try:
        body = json.loads(event['body'])
        purple_data = [[x] for x in body['purple']]
        
        print(purple_data)

        preds = list(predict_rf(purple_data))

        return {
            "statusCode": 200,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True

            },
            "body": json.dumps({'AireNL': preds,
                                'mybody': body})
        }

    except Exception as e:
        print(repr(e))
        return {
            "statusCode": 500,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True
            },
            "body": json.dumps({"error": repr(e)})
        }
