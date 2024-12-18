from filefastapi.routes import post, get

from filefastapi import app
from mangum import Mangum



handler = Mangum(app)
