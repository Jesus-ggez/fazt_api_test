import os

prohibids: set = {
    ('nombre', 'name'),
    ('descripcion', 'description'),
    ('precio', 'price'),
    ('moneda', 'currency'),
    ('url_imagen', 'url_image'),
    ('categoria', 'category'),
    ('marca', 'brand'),
    ('talla', 'size'),
    ('material', 'material'),
    ('disponibilidad', 'availible')
}

def re_define(raw: str) -> str:
    for item in prohibids:
        if raw.replace(' ', '').startswith(f'"{item[0]}"'):
            return raw.replace(
                f'"{item[0]}"',
                f'"{item[1]}"',
                1
            )

    return raw


def doc_reader(name: str) -> list:
    document: list = []

    with open(name, 'r') as rawdoc:
        for line in rawdoc:
            document.append(
                re_define(
                    raw=line,
                )
            )

    return document



def main() -> None:
    os.chdir('data')
    docs: list = os.listdir()

    for item in docs:
        if os.path.isdir(item):
            continue

        new: list[str] = doc_reader(item)

        with open(item, 'w') as doc:
            doc.writelines(new)



if __name__ == '__main__':
    main()
    ...
