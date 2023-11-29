from motor import motor_asyncio


MONGO_URI = "mongodb://localhost:27017/"
client = motor_asyncio.AsyncIOMotorClient(MONGO_URI)

# hack: entrega um objeto que já aponta para o DB
mongo = client.ite