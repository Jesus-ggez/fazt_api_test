# Proyecto FastAPI

Este proyecto utiliza **FastAPI** como única dependencia para crear una API dinámica y extensible. A continuación, se detallan los pasos para configurar y extender la funcionalidad del proyecto.

## Instalación

1. Clona el repositorio:
```bash
   ### ssh
   git clone git@github.com:Jesus-ggez/fazt_api_test.git

   ### https
   git clone https://github.com/Jesus-ggez/fazt_api_test.git
´´´

2. Navega al directorio del repositorio e instala las dependencias:
```bash

   cd fazt_api_test

   pip install requirements.txt

```
3. Ejecuta la aplicacion:
```bash
   ### python
   python main.py

   ### uvicorn
   uvicorn main:app --reload
```

Para extender la funcionalidad deberas seguir estas instrucciones:

## Teoria
esta cosa utiliza generadores basados en la metaprogramacion de python
por lo que sera algo complejo mover la infraestructura sin embargo puedes
extender la funcionalidad relativamente facil


## Extension

1. Crea un modelo

    en principio es facil.
    abre el archivo models.py dentro de src

    `vim src/models.py`

    despues dentro agrega la clase que quieras
    Ejemplo:
```python
    class MyModel(BaseModel):
        ...
```

    lo recomendable es heredar de BaseModel
    para parsear mas facilmente

    ahora ya teniendo tu modelo toca crear la data

    dirigete hacia `src/data/` y alli crea un documento

    #### Importante
    el documento debe llamarse igual al modelo creado anteriormente pero con terminacion "s.py"

    `
    touch src/data/<filename>s.py
    `

    dentro de este documento siempre debe existir 
    `
    data: list = [...]
    `

    este es el punto clave para usar la aplicacion

    deberia quedar asi:

    // src/models.py
    ```python
    class MyExtensionApi(BaseModel):
        extends_data: str

    ```

    // src/data/<myextensionapi>s.py
    ```python
    data: list[dict] = []
    ```


    terminado esto puedes hacer uso de todas las funciones de el api sin configurar tanta cosa


