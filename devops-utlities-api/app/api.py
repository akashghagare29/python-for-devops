from fastapi import FastAPI # Application Entry Point, Importing FastAPI Class
from routers import metrics, aws  # Importing Routers for Metrics and AWS

app = FastAPI(   # Creating FastAPI Application Instance
    title="DevOps Utilities API",
    description="API for various DevOps utilities",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")  # Defining a GET endpoint at /
def hello():
    """
        Simple endpoint to test the API.
    """

    return {"message": "Hello Dosto, DevOps Utilities API!"}

app.include_router(metrics.router) # Including the metrics router
app.include_router(aws.router, prefix="/aws") # Including the AWS router