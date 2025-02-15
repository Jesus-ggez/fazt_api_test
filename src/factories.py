try:
    import models

except ModuleNotFoundError:
    from . import models


raw_models_data = vars(models).items()
models_data: set[type] = {item for _, item in raw_models_data if isinstance(item, type)}

# export
factories: dict = {item.__name__.lower() + 's': item for item in models_data}

for item in models.ignoremodels:
    factories.pop(item + 's')

if __name__ == '__main__':
    print(factories.keys())
