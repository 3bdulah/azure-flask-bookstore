from flask import Flask
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)

    cosmosdb_uri = os.getenv("AZURE_COSMOSDB_CONNECTION_STRING")

    try:
        if cosmosdb_uri:
            client = MongoClient(cosmosdb_uri, serverSelectionTimeoutMS=5000)
            client.server_info()
            app.db = client["ain3003"]
            print("Connected to Cosmos DB (Mongo API).")
        else:
            raise RuntimeError("AZURE_COSMOSDB_CONNECTION_STRING is not set.")
    except Exception as cosmosdb_error:
        print(f"CosmosDB connection failed: {cosmosdb_error}")
        app.db = None

    if app.db is None:
        print("No database connection could be established.")

    # Register Blueprints
    from app.routes import blueprint
    app.register_blueprint(blueprint)

    return app