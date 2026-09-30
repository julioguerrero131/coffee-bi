<div align="center">
  <h1>🎨 Coffee BI - Interfaz de Usuario (Frontend)</h1>
  <p><strong>El Dashboard Analítico para Coffee BI</strong></p>
  
  [![Angular](https://img.shields.io/badge/Angular-21-DD0031?style=for-the-badge&logo=angular&logoColor=white)]()
  [![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4.1-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)]()
  [![TypeScript](https://img.shields.io/badge/TypeScript-5.9-3178C6?style=for-the-badge&logo=typescript&logoColor=white)]()
</div>

<br />

## 📖 Descripción General

Este directorio contiene el frontend del proyecto **Coffee BI**, una aplicación de página única (SPA) desarrollada con **Angular 21**. Proporciona una experiencia de usuario rica, reactiva y moderna para visualizar los datos del negocio, revisar las transacciones recientes y analizar gráficos detallados que ayudan a los dueños de la cafetería a tomar decisiones informadas.

## 🛠️ Tecnologías Utilizadas

- **[Angular 21](https://angular.dev/):** El framework principal utilizado para construir la estructura de la aplicación y la reactividad.
- **[Tailwind CSS (v4)](https://tailwindcss.com/):** Framework de CSS utilitario utilizado para estilizar y dar un diseño moderno y responsivo al dashboard rápidamente.
- **[TypeScript](https://www.typescriptlang.org/):** Tipado estricto para un desarrollo más seguro, mantenible y escalable.
- **[RxJS](https://rxjs.dev/):** Para programación reactiva y manejo del flujo de datos asincrónico (ej. peticiones a la API).

## 📂 Estructura del Proyecto

```text
frontend/
├── src/
│   ├── app/
│   │   ├── components/  # Componentes reutilizables (tarjetas, gráficos, tablas)
│   │   ├── pages/       # Vistas completas de la aplicación (ej. home dashboard)
│   │   ├── app.routes.ts # Configuración del enrutamiento de la aplicación
│   │   └── app.ts       # Componente raíz
│   ├── public/          # Archivos estáticos como imágenes y fuentes
│   └── index.html       # Archivo HTML principal
├── angular.json         # Configuración del workspace de Angular
├── package.json         # Dependencias y scripts de NPM
└── tailwind.config.js   # Configuración de los estilos y diseño de Tailwind (si aplica)
```

## 🚀 Requisitos Previos

Asegúrate de tener instalados los siguientes componentes antes de comenzar:
- **[Node.js](https://nodejs.org/):** Versión LTS (recomendado 18.x o superior) si no usas Docker.
- **npm:** Gestor de paquetes de Node (viene por defecto con Node.js).
- *Opcional:* Angular CLI (`npm install -g @angular/cli`).
- *Opcional:* **Docker** (recomendado para un despliegue unificado).

## 🐳 Ejecución con Docker

Este directorio contiene su propio `Dockerfile` diseñado para el entorno de desarrollo, habilitando el *hot-reloading* de Angular dentro del contenedor. La mejor forma de ejecutarlo es utilizando **Docker Compose** desde la raíz de todo el proyecto:

```bash
# Desde la raíz de coffee-bi/
docker-compose up -d --build frontend
```

La aplicación quedará expuesta en `http://localhost:4200/`.

## ⚙️ Instalación y Configuración (Local Manual)

Si decides no usar Docker, sigue estos pasos para configurar tu entorno de desarrollo local manualmente:

1. **Navegar al directorio del frontend:**
   ```bash
   cd frontend
   ```

2. **Instalar las dependencias de NPM:**
   ```bash
   npm install
   ```

## 🏃‍♂️ Ejecución del Servidor de Desarrollo

Para correr la aplicación en un servidor de desarrollo local, ejecuta:

```bash
npm start
# O alternativamente, si tienes instalado el CLI globalmente:
# ng serve
```

La aplicación estará disponible automáticamente en: `http://localhost:4200/`. El navegador recargará la página por sí solo cada vez que modifiques o guardes un archivo del código fuente.

## 📦 Construcción para Producción

Para compilar el proyecto en una versión lista y optimizada para la producción, utiliza:

```bash
npm run build
# o 'ng build'
```

Los artefactos de compilación se almacenarán en el directorio `dist/`. Estos archivos están minimizados, optimizados para un rendimiento rápido y listos para ser desplegados en plataformas como Vercel, Netlify o cualquier servidor web.

## 🧪 Pruebas (Testing)

Para ejecutar la batería de pruebas unitarias usando el motor de Vitest (o Karma/Jasmine por defecto de Angular), corre:

```bash
npm run test
```

---
*Para volver a la raíz del proyecto, haz clic [aquí](../README.md).*
