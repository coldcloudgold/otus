from dataclasses import dataclass
from enum import StrEnum
from random import randint

from blacksheep import Application, get
from blacksheep.server.openapi.v3 import OpenAPIHandler
from openapidocs.v3 import Info

app = Application()


docs = OpenAPIHandler(info=Info(title="Lesson 10 API", version="0.0.1"))
docs.bind_app(app)


class Status(StrEnum):
    OK = "OK"
    ERROR = "ERROR"


@dataclass(slots=True, kw_only=True)
class HealthStatus:
    status: Status


@get("/health/")
async def health() -> HealthStatus:
    # status = Status.OK if randint(0, 1) else Status.ERROR
    status = Status.OK

    return HealthStatus(status=status)
