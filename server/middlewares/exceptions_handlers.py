from fastapi import Request
from fastapi.responses import JSONResponse
from logger import Logger

async def catch_exception_middleware(request:Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        Logger.exception(f"UNHANDLED EXCEPTIONS")
        return JSONResponse(status_code=500, content={"error": str(e)})
    