<div align="center">
  <h1>⚙️ Coffee BI - API REST (Backend)</h1>
  <p><strong>El motor de datos para el Dashboard de Coffee BI</strong></p>
  
  [![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
  [![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)]()
  [![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)]()
</div>

<br />

## 📖 Descripción General

Este es el backend oficial del proyecto **Coffee BI**. Es una API RESTful construida con **FastAPI** que sirve como puente entre el cliente web y la base de datos de MongoDB. Su objetivo principal es recibir los tickets de ventas, procesarlos y proveer endpoints que calculen las métricas y los datos agregados que alimentan los gráficos y tablas del frontend.

## 🛠️ Tecnologías Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/):** Framework web moderno y de alto rendimiento para construir APIs en Python.
- **[Pydantic](https://docs.pydantic.dev/):** Validación de datos y gestión de configuraciones utilizando anotaciones de tipo de Python.
- **[PyMongo](https://pymongo.readthedocs.io/):** Controlador de Python para interactuar con bases de datos MongoDB.
- **[Uvicorn](https://www.uvicorn.org/):** Servidor web ASGI para Python de alto rendimiento.

## 📂 Estructura del Proyecto

```text
backend/
├── app/
│   ├── api/          # Controladores y rutas de la API REST (routers)
│   │   └── routes/   # Endpoints específicos (ej. sales.py, metrics.py)
│   ├── core/         # Configuraciones globales, conexión a DB y variables de entorno
│   ├── schemas/      # Modelos de validación de datos de Pydantic
│   └── main.py       # Punto de entrada y configuración de la aplicación FastAPI
├── tests/            # Directorio para pruebas unitarias e integración
├── .env.example      # Plantilla de variables de entorno requeridas
└── requirements.txt  # Lista de dependencias del proyecto
```

## 🚀 Requisitos Previos

Asegúrate de tener instalado en tu sistema:
- Python 3.11 o superior.
- Una instancia de MongoDB ejecutándose localmente o una URI de MongoDB Atlas.

## ⚙️ Instalación y Configuración

Sigue estos pasos para configurar el entorno de desarrollo local:

1. **Navegar al directorio del backend:**
   ```bash
   cd backend
   ```

2. **Crear y activar un entorno virtual (recomendado):**
   ```bash
   python -m venv .venv
   
   # En Windows:
   .venv\Scripts\activate
   # En macOS/Linux:
   source .venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar las variables de entorno:**
   - Copia el archivo `.env.example` y renómbralo a `.env`.
   - Modifica los valores dentro de `.env` para que apunten a tu base de datos MongoDB.
   ```bash
   cp .env.example .env
   ```

## 🏃‍♂️ Ejecución del Servidor

Para iniciar el servidor de desarrollo en modo "hot-reload", ejecuta:

```bash
uvicorn app.main:app --reload
```

La API estará disponible por defecto en: `http://127.0.0.1:8000`

### 📚 Documentación Interactiva

FastAPI genera automáticamente documentación interactiva para la API basada en la especificación OpenAPI. Una vez que el servidor esté en ejecución, puedes acceder a:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

## 🔗 Endpoints Principales

- `POST /api/v1/sales/` - Ingresa un nuevo ticket de venta a la base de datos.
- `GET /api/v1/metrics/...` - (Ejemplo) Retorna las métricas agregadas del negocio para el dashboard.

---
*Para volver a la raíz del proyecto, haz clic [aquí](../README.md).*
