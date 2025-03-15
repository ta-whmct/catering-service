from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

main_router = APIRouter(prefix="/api/v1")


@main_router.get("/health")
async def health() -> JSONResponse:
    return JSONResponse(
        content={"The application's status": "work"}, status_code=status.HTTP_204_NO_CONTENT
    )
