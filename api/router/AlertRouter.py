from fastapi import APIRouter, Depends, status
from api.schemas.AlertSchema import AlertInDBBase, AlertCreate, Alert
from database.repositories.AlertRepository import AlertRepository

AlertRouter = APIRouter(
    prefix="/alert"
)

@AlertRouter.get("/", response_model=list[AlertInDBBase])
def list(skip: int = 0, limit: int = 100, alertRepository: AlertRepository = Depends()):
    return alertRepository.list(skip, limit)

@AlertRouter.get("/{id}", response_model=AlertInDBBase)
def get(id: int, alertRepository: AlertRepository = Depends()):
    return alertRepository.get(id)

@AlertRouter.post("/", response_model=Alert, status_code=status.HTTP_201_CREATED)
def create(alert: AlertCreate, alertRepository: AlertRepository = Depends()):
    return alertRepository.create(alert)