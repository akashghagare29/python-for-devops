from fastapi import APIRouter, HTTPException # Importing APIRouter and HTTPException from FastAPI
from services.metrics_services import get_system_metrics  # Importing the service function to get system metrics

router = APIRouter()

@router.get("/metrics", status_code=200)
def get_metrics():
    """
        Endpoint to retrieve system metrics.
    """

    try:
        metrics = get_system_metrics()
        return metrics
    except Exception:
        raise HTTPException(
            status_code=500, 
            detail="Internal Server Error"
        )
