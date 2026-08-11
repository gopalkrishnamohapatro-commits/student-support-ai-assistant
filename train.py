import json

with open("intents.json", "r") as f:
    data = json.load(f)

print("Training data loaded successfully.")

for intent in data["intents"]:
    print("Intent:", intent["tag"])

print("Model training preparation completed.")
