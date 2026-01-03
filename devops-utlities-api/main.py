from app.api import app  # Importing the FastAPI application instance
import uvicorn

# Application Entry Point
if __name__ == "__main__":
    # ASGI web server to run the FastAPI application
    uvicorn.run(
        "app.api:app", 
        host="0.0.0.0", # Start the FastAPI application
        port=8000,
        reload=True
    )  