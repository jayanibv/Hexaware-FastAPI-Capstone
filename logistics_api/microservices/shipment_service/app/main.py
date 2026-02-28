from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import shipments
from app.core.database import Base, engine

app = FastAPI(title="Shipment Service", root_path="/shipments")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(shipments.router)