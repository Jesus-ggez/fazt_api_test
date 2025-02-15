from fastapi import FastAPI

#~>
from src.factories import factories
from src.app import ProductFactory

app: FastAPI = FastAPI()


@app.get('/')
def home() -> list:
    return list(factories.keys())



for name in factories.keys():
    @app.get(f'/{name}')
    def item(name: str = name) -> list:
        return ProductFactory.create_product(name)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        port=8000,
        app=app,
    )

