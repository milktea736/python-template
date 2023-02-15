from fastapi import FastAPI

from restful.api.routes import router


def get_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app


app = get_app()
