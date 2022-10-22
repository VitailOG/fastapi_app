from fastapi import FastAPI

from src.apps.backend.api.endpoints.student import router
from src.events import init_mongo


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)  # register all endpoints
    application.add_event_handler('startup', init_mongo)  # register startup events
    return application


app = get_application()
