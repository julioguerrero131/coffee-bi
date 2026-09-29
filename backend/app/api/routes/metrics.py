from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_metrics():
    """
    Retrieve metrics data.
    """
    return {"status": "success", "metrics": {}}
