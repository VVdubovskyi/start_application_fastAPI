import uvicorn
from fastapi import FastAPI
from api import router as api_router
from core.config import settings
from core.models import db_helper, Base


def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(api_router, prefix=settings.api_prefix.prefix)

if __name__ == "__main__":
    # Base.metadata.create_all(bind=db_helper.engine)
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)
