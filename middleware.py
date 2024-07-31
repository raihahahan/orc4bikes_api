from fastapi import FastAPI, Request, HTTPException, Response, status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response, JSONResponse
from access_token import check_token

class AccessTokenMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Logic before the request is processed
        if request.headers.get("AccessToken") is None:
            return JSONResponse(status_code=401, content={"Message": "Access token not found."})

        token = request.headers.get("AccessToken")

        if not check_token(token):
            return JSONResponse(status_code=403, content={"Message": "Invalid token."})

        # Process the request
        response = await call_next(request)
        
        # Logic after the request is processed
        
        return response