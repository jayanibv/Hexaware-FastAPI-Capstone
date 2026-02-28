from fastapi import FastAPI
from app.routes import tracking
from app.core.database import Base, engine

app = FastAPI(title="Tracking Service", root_path="/tracking")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(tracking.router)