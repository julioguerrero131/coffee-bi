<div align="center">
  <h1>☕ Coffee BI</h1>
  <p><strong>Business Intelligence Dashboard para Cafeterías</strong></p>
  
  [![Frontend](https://img.shields.io/badge/Frontend-Angular%2021-DD0031?style=for-the-badge&logo=angular)](./frontend)
  [![Backend](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi)](./backend)
  [![Database](https://img.shields.io/badge/Database-MongoDB-47A248?style=for-the-badge&logo=mongodb)](./backend)
</div>

<br />

## 📖 Sobre el Proyecto

**Coffee BI** es una plataforma moderna de Business Intelligence (BI) diseñada específicamente para la gestión y análisis de datos de cafeterías. Este proyecto full-stack permite a los dueños de negocios visualizar métricas clave de rendimiento (KPIs), analizar las ventas por producto y supervisar el historial de transacciones a través de un panel de control interactivo.

El proyecto está diseñado siguiendo las mejores prácticas de desarrollo de software, separando el frontend y el backend en servicios independientes para garantizar escalabilidad y fácil mantenimiento.

## 🏗️ Arquitectura del Sistema

El proyecto está dividido en dos aplicaciones principales:

1. **[Frontend (Angular)](./frontend/)**: Una interfaz de usuario moderna, reactiva y responsiva construida con Angular 21 y Tailwind CSS. Encargada de mostrar gráficos interactivos y tablas de datos.
2. **[Backend (FastAPI)](./backend/)**: Una API RESTful rápida y robusta construida con Python y FastAPI. Encargada de la lógica de negocio, la ingesta de tickets de ventas y el cálculo de métricas agregadas desde MongoDB.

## 📂 Estructura del Repositorio

```text
coffee-bi/
├── backend/               # Código fuente de la API (Python / FastAPI)
│   ├── app/               # Lógica de la aplicación, rutas y modelos
│   ├── tests/             # Pruebas unitarias
│   └── README.md          # Documentación específica del Backend
└── frontend/              # Código fuente del cliente web (Angular)
    ├── src/               # Componentes, servicios y vistas
    └── README.md          # Documentación específica del Frontend
```

## 🚀 Cómo Empezar

Para desplegar este proyecto en tu entorno local, deberás configurar y ejecutar tanto el backend como el frontend.

Por favor, consulta las instrucciones detalladas en cada uno de los directorios:

- 👉 **[Guía de Configuración del Backend](./backend/README.md)**
- 👉 **[Guía de Configuración del Frontend](./frontend/README.md)**

## ✨ Características Principales

- **Dashboard Interactivo:** Visualización de ventas totales, transacciones y productos más vendidos.
- **Gráficos Dinámicos:** Integración de gráficos para análisis visual de las ventas en el tiempo.
- **API Rápida y Segura:** Endpoints optimizados con FastAPI y validación de datos estricta usando Pydantic.
- **Diseño Responsivo:** Interfaz adaptada a cualquier tamaño de pantalla gracias a Tailwind CSS.

## 🤝 Contribución

Si deseas contribuir a este proyecto, por favor realiza un "fork" del repositorio, crea una nueva rama para tus características o correcciones de errores, y envía un "pull request". Toda contribución es bienvenida.

---
*Diseñado y desarrollado para demostrar habilidades de desarrollo web Full-Stack.*
