import chromadb

client = chromadb.PersistentClient(path="./db")
collection = client.get_or_create_collection("docs")

with open("HUG.txt", "r") as f:
    text = f.read()

collection.add(documents=[text], ids=["HUG"])

print("Embedding stored in Chroma")
