import json

houseItems = {
    "item": "Xbox One",
    "Description": "Microsoft Xbox One Edition.",
    "Color": "Black"
}

makeJson = json.dumps(houseItems)

print(makeJson)
