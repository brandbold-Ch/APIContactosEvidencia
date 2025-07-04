from fastapi import FastAPI
from fastapi.responses import JSONResponse
from h11 import Request
from fastapi.middleware.cors import CORSMiddleware
from controllers.contact_controller import contact_controller
from controllers.group_controller import group_controller
from exceptions.exceptions import BaseHTTPException

app = FastAPI(root_path="/api")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(BaseHTTPException)
def exception_handler(
        request: Request,
        exception: BaseHTTPException
):
    return JSONResponse(status_code=exception.http_code,
                        content=exception.to_dict())


app.include_router(contact_controller, tags=["Contacts"])
app.include_router(group_controller, tags=["Groups"])
