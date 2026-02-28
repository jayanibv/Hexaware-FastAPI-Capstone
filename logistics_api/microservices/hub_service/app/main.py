from fastapi import FastAPI
from app.routes import hubs
from app.core.database import Base, engine

app = FastAPI(title="Hub Service", root_path="/hubs")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(hubs.router)