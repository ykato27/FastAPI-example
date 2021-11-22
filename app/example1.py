from typing import Optional
from fastapi import FastAPI

app = FastAPI()

# パスパラメータ
# @app.get("/")
# async def index():
#     return {"message": "Hello World"}

# パスパラメータ
# @app.get("/countries/{country_name}")
# async def country(country_name: str):
#     return {"country_name": country_name}

# クエリーパラメータ
# @app.get("/countries/")
# async def country(country_name: str = "japan", country_no: int = 1):
#     return {
#         "country_name": country_name,
#         "country_no": country_no,
#         }

# クエリーパラメータ
# @app.get("/countries/{country_name}")
# async def country(country_name: str = "japan", city_name: str = "tokyo"):
#     return {
#         "country_name": country_name,
#         "city_name": city_name,
#         }

# オプションパラメータ
@app.get("/countries/")
async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
    return {
        "country_name": country_name,
        "country_no": country_no,
        }