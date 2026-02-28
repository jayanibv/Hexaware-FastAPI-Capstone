import sys
import os
sys.path.append(os.getcwd())

from app.core.database import engine, Base
from app.models.user import User
from app.models.hub import Hub
from app.models.shipment import Shipment
from app.models.tracking import Tracking

print("Dropping all tables...")
Base.metadata.drop_all(bind=engine)
print("Creating all tables...")
Base.metadata.create_all(bind=engine)
print("Database reset complete.")
