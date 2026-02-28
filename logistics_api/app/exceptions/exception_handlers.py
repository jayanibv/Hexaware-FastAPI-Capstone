from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import (
    ShipmentNotFoundException,
    UnauthorizedRoleException,
    HubNotFoundException
)


def register_exception_handlers(app):

    @app.exception_handler(ShipmentNotFoundException)
    async def shipment_not_found_handler(request: Request, exc):
        return JSONResponse(
            status_code=404,
            content={"detail": "Shipment not found"}
        )

    @app.exception_handler(UnauthorizedRoleException)
    async def unauthorized_role_handler(request: Request, exc):
        return JSONResponse(
            status_code=403,
            content={"detail": "Access denied"}
        )

    @app.exception_handler(HubNotFoundException)
    async def hub_not_found_handler(request: Request, exc):
        return JSONResponse(
            status_code=404,
            content={"detail": "Hub not found"}
        )