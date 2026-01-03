from fastapi import APIRouter, HTTPException # Importing APIRouter and HTTPException from FastAPI
from services.aws_service import get_bucket_info  # Importing the service function to get S3 bucket information
# from services.aws_service import get_ec2_info  # Importing the service function to get EC2 instance information

router = APIRouter()

@router.get("/s3", status_code=200)
def get_s3_buckets():
    """
        Endpoint to retrieve S3 bucket information.
    """

    try:
        buckets = get_bucket_info()
        return buckets
    except Exception:
        raise HTTPException(
            status_code=500, 
            detail="Internal Server Error"
        )
    
@router.get("/ec2", status_code=200)
def get_ec2_instances():
    """
        Endpoint to retrieve EC2 instance information.
    """
    return {"message": "EC2 instance retrieval not implemented yet."}

    # try:
    #     instances = get_ec2_info()
    #     return instances
    # except Exception:
    #     raise HTTPException(
    #         status_code=500, 
    #         detail="Internal Server Error"
    #     )
