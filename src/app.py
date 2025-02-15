try:
    from factories import factories
    from data.app import get_data

except ModuleNotFoundError:
    from .factories import factories
    from .data.app import get_data


class ProductFactory:
    @staticmethod
    def create_product(type_name: str) -> list:
        item = factories.get(type_name)

        if item is None:
            raise ValueError(f'Unknown Key: {type_name}')

        try:
            data: list[dict] = get_data(name=type_name)

        except Exception as e:
            print(type_name)
            print(e)
            raise

        return [item(**d) for d in data]


if __name__ == '__main__':
    name: str = input('module: ')

    test = ProductFactory.create_product(name)
    print(test[0].model_dump())

