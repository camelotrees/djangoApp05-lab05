# Laboratorio 05: Administración de Django

## Descripción
En este laboratorio se desarrolló una aplicación web utilizando Django, aprendiendo a gestionar información mediante el administrador integrado de Django (Django Admin), sin necesidad de programar formularios manualmente.

## Objetivos
- Comprender el funcionamiento del administrador de Django.
- Registrar y gestionar modelos desde Django Admin.
- Crear relaciones entre modelos mediante `ForeignKey`.
- Personalizar la visualización y administración de registros.
- Implementar acciones personalizadas y mejorar la interfaz con Jazzmin.

## Desarrollo del laboratorio

### 1. Administración de modelos
Se utilizó `admin.site.register` para registrar los modelos y un superusuario para agregar, visualizar, editar y eliminar información desde el administrador de Django.

También se implementó el método `__str__` en el modelo `Categoria` para mostrar nombres descriptivos en lugar de referencias como `Categoria object (1)`.

### 2. Creación y relación de modelos
Se trabajó con los siguientes modelos:
- **Categoria:** almacena las categorías de los productos.
- **Producto:** contiene información de los productos y su relación con Categoria mediante `ForeignKey`.
- **Cliente:** registra información de los clientes, utilizando el DNI como `CharField` único.

Se ejecutaron las migraciones correspondientes mediante `makemigrations` y `migrate`.

### 3. Personalización de Django Admin
Se utilizaron las siguientes opciones:
- `list_display`: personalización de las columnas visibles.
- `search_fields`: búsqueda de registros.
- `list_filter`: filtros para organizar la información.
- Acción personalizada para incrementar el stock de los productos en 20 unidades mediante `F('stock') + 20` y `update()`.

Asimismo, se instaló Django Jazzmin para mejorar la apariencia visual del panel administrativo.

### 4. Observaciones y opinión crítica
Durante el desarrollo se identificó un error de copia en la guía, donde se menciona la aplicación encuesta en lugar de tienda. También se observó el uso de una contraseña fija para el administrador, práctica que no es recomendable en proyectos reales por motivos de seguridad.

El laboratorio permitió comprender la utilidad del administrador de Django y cómo facilita la gestión de información, optimizando el tiempo de desarrollo.

## Tecnologías utilizadas
- Python
- Django 6.1.2
- Django Jazzmin 3.0.5
- SQLite
- Git y GitHub

## Instalación y ejecución

1. Clonar el repositorio:

   `git clone https://github.com/camelotrees/djangoApp05-lab05.git`

2. Ingresar a la carpeta del proyecto:

   `cd djangoApp05-lab05`

3. Crear el entorno virtual:

   `python -m venv myvenv`

4. Activar el entorno virtual:

   `.\myvenv\Scripts\Activate.ps1`

5. Instalar las dependencias:

   `pip install -r requirements.txt`

6. Ejecutar las migraciones:

   `python manage.py migrate`

7. Crear un superusuario:

   `python manage.py createsuperuser`

8. Iniciar el servidor:

   `python manage.py runserver`

## Autor
Camelotrees

**Repositorio:** https://github.com/camelotrees/djangoApp05-lab05