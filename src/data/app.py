import importlib

def get_data(name: str) -> list:
    absolute: str = 'src.data.' + name
    try:
        module= importlib.import_module(
            name=absolute,
        )

        if not hasattr(module, 'data'):
            raise ValueError('Module not found')

        return module.data

    except ModuleNotFoundError:
        raise ValueError('Module not found')

