import json

houseItems = {
    "item": "Xbox One",
    "Description": "Microsoft Xbox One Edition.",
    "Color": "Black",
    "Edition": "1Tb"
}

makeJson = json.dumps(houseItems)

print(makeJson)
