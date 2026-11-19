# Portfolio Web Full Stack — Proyecto Integrador

Aplicación web full stack desarrollada con **Python, Flask, MySQL, Jinja2 y POO** que funciona como portfolio personal y como sistema administrable. Incluye panel privado con autenticación, base de datos relacional, API JSON, generación dinámica del CV en PDF y una interfaz responsive con animaciones.

> **Estado:** el desarrollo y las pruebas están completos. La publicación en Clever Cloud y la subida a GitHub quedan pendientes de las credenciales del alumno (ver [Despliegue](#despliegue-en-clever-cloud)).

---

## Índice

- [Características](#características)
- [Stack tecnológico](#stack-tecnológico)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Instalación local](#instalación-local)
- [Configuración de MySQL](#configuración-de-mysql)
- [Ejecución](#ejecución)
- [Acceso al panel](#acceso-al-panel)
- [Pruebas](#pruebas)
- [Documentación](#documentación)
- [Despliegue en Clever Cloud](#despliegue-en-clever-cloud)
- [Git y GitHub](#git-y-github)
- [Seguridad](#seguridad)
- [Mapeo de requisitos](#mapeo-de-requisitos)
- [Solución de problemas](#solución-de-problemas)

---

## Características

### Sitio público
- Hero animado con typewriter, avatar, disponibilidad y estadísticas.
- Secciones de **Sobre mí, Estudios, Experiencia, Tecnologías, Proyectos, Ubicación y Contacto**.
- Líneas de tiempo, tarjetas de tecnologías con barras de nivel y proyectos con etiquetas.
- Mapa embebido de OpenStreetMap (**iframe** requerido).
- Formulario de contacto con CSRF, validación del servidor y honeypot anti-spam.
- **CV descargable en PDF**, generado en el momento con los datos actuales de la base.
- API pública de solo lectura: `GET /api/portfolio`.
- Metadatos SEO y Open Graph, favicon y logo SVG locales.
- Iconos FontAwesome, Google Fonts y diseño responsive (móvil, tablet y escritorio).
- Animaciones con CSS y JavaScript nativo, respetando `prefers-reduced-motion`.

### Panel privado
- Login con Flask-Login, contraseña hasheada (Werkzeug scrypt) y protección CSRF.
- Dashboard con métricas y últimos mensajes.
- CRUD completo de estudios, experiencias, tecnologías y proyectos.
- Edición del perfil, avatar, redes y resumen del CV.
- Relación **N:M** entre proyectos y tecnologías mediante selección múltiple.
- Bandeja de mensajes con estado leído/no leído y eliminación.
- Cambio de nombre de usuario y contraseña con verificación de la clave actual.
- Visibilidad por registro (`activo`) y orden personalizable.

---

## Stack tecnológico

| Capa | Tecnología |
| --- | --- |
| Backend | Python 3.12+, Flask 3, Flask-SQLAlchemy, Flask-Login, Flask-WTF |
| Base de datos | MySQL 8 en producción, SQLite en desarrollo local |
| ORM / driver | SQLAlchemy + PyMySQL |
| Frontend | Jinja2, HTML5, CSS3, JavaScript ES6 |
| PDF | ReportLab (CV y documentación) |
| Pruebas | pytest |
| Producción | Gunicorn + Clever Cloud |
| Recursos | FontAwesome 6.7.2, Google Fonts (Fraunces, Inter) |

---

## Estructura del proyecto

```text
portfolio2/
├── app.py                  # Entrada de desarrollo
├── wsgi.py                 # Entrada WSGI para producción
├── config.py               # Configuración y URI de la base
├── requirements.txt
├── Procfile                # Arranque alternativo con gunicorn
├── pytest.ini
├── .env.example            # Plantilla de variables de entorno
├── portfolio/
│   ├── __init__.py         # Application factory, filtros, CLI, errores
│   ├── extensions.py       # db, login_manager, csrf
│   ├── models.py           # POO (4 pilares) y tablas del modelo relacional
│   ├── forms.py            # Formularios Flask-WTF
│   ├── seed.py             # Datos de demostración
│   ├── pdf.py              # Generación del CV
│   ├── routes/
│   │   ├── public.py       # Portfolio, contacto, CV, API, salud
│   │   ├── auth.py         # Login y logout
│   │   └── admin.py        # Panel CRUD protegido
│   ├── templates/          # Jinja2: público, admin, auth y errores
│   └── static/             # CSS, JS e imágenes SVG
├── database/
│   ├── schema_mysql.sql    # Diseño físico MySQL
│   └── seed.sql            # Datos iniciales en SQL
├── docs/
│   ├── Documentacion_Preliminar_Portfolio.pdf
│   └── Guia_Despliegue.md
├── scripts/
│   └── generar_documentacion.py
└── tests/                  # 36 pruebas automatizadas
```

---

## Instalación local

### Requisitos
- Python 3.12 o superior (probado con 3.14 en Windows).
- MySQL 8 (opcional en desarrollo; sin MySQL se usa SQLite).
- Git (para el versionado).

### Pasos

```powershell
# 1. Crear el entorno virtual
python -m venv .venv

# 2. Activarlo (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Si PowerShell bloquea la ejecución:
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

# 3. Instalar dependencias
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# 4. Crear el archivo de configuración
copy .env.example .env

# 5. Ejecutar
python app.py
```

Abrir <http://127.0.0.1:5000>.

Sin `DATABASE_URL`, la aplicación crea automáticamente `instance/portfolio.db` (SQLite) y carga los datos de demostración. Esto permite ejecutar y evaluar el proyecto sin instalar MySQL.

---

## Configuración de MySQL

### Opción A — Scripts SQL incluidos

```bash
mysql -u root -p < database/schema_mysql.sql
mysql -u root -p < database/seed.sql
```

- `database/schema_mysql.sql`: crea la base `portfolio`, las 8 tablas, claves foráneas, índices y restricciones.
- `database/seed.sql`: carga el perfil, estudios, experiencias, tecnologías, proyectos, la relación N:M y un mensaje de ejemplo.

Ambos scripts se pueden ejecutar también desde phpMyAdmin, MySQL Workbench o DBeaver.

### Opción B — Comandos de Flask

```powershell
$env:DATABASE_URL="mysql+pymysql://root:tu_clave@localhost:3306/portfolio?charset=utf8mb4"
.\.venv\Scripts\flask --app wsgi init-db
.\.venv\Scripts\flask --app wsgi seed-db
```

### Variables de entorno

| Variable | Descripción |
| --- | --- |
| `SECRET_KEY` | Clave para firmar sesiones y CSRF. Obligatoria en producción. |
| `FLASK_CONFIG` | `development` (por defecto) o `production`. |
| `DATABASE_URL` | URI completa de MySQL. Tiene prioridad. |
| `MYSQL_ADDON_URI` | URI inyectada por el add-on MySQL de Clever Cloud. |
| `MYSQL_ADDON_HOST/USER/PASSWORD/PORT/DB` | Construcción alternativa de la URI. |
| `ADMIN_USERNAME` | Usuario inicial del panel. |
| `ADMIN_PASSWORD` | Contraseña inicial del panel. |
| `ADMIN_NOMBRE` | Nombre visible del administrador. |
| `SITE_NAME` | Nombre del sitio en metadatos. |
| `SITE_URL` | URL pública para canonical y Open Graph. |
| `CONTACT_EMAIL` | Email mostrado en el pie del sitio. |
| `SEED_ON_START` | `1` carga datos de ejemplo al iniciar si la base está vacía. |
| `SESSION_COOKIE_SECURE` | `true` en producción con HTTPS. |

> El archivo `.env` está excluido por `.gitignore`. Nunca subir claves reales al repositorio.

---

## Ejecución

```powershell
# Desarrollo
python app.py

# Producción local (Linux/macOS o WSL)
gunicorn wsgi:app --bind 0.0.0.0:8000
```

Rutas útiles:

| Ruta | Descripción |
| --- | --- |
| `/` | Portfolio completo |
| `/cv` | Descarga del CV en PDF |
| `/api/portfolio` | Contenido en JSON |
| `/salud` | Health check |
| `/login` | Acceso al panel |
| `/admin/` | Panel de administración |

---

## Acceso al panel

Credenciales iniciales:

```text
Usuario:    kevinAdmin
Contraseña: kevin1504
```

> **Cambiar la contraseña antes de publicar** desde *Panel → Mi cuenta*. También se pueden definir otras credenciales iniciales con `ADMIN_USERNAME` y `ADMIN_PASSWORD` antes del primer arranque.

Desde el panel se puede:

1. Editar el perfil y el resumen del CV.
2. Crear, editar, ocultar o eliminar estudios y experiencias.
3. Administrar tecnologías con su nivel, icono y color.
4. Crear proyectos y asociarles varias tecnologías.
5. Leer y eliminar mensajes del formulario de contacto.
6. Cambiar el usuario y la contraseña.

Todos los cambios se reflejan de inmediato en el sitio público y en el CV.

---

## Pruebas

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Resultado esperado:

```text
36 passed
```

La suite cubre:

- Render de las secciones públicas, iframe, recursos y cabeceras de seguridad.
- API JSON, descarga del CV y páginas de error.
- Login válido/inválido, redirección segura, logout y protección del panel.
- CRUD de estudios, experiencias, tecnologías, proyectos y perfil.
- Relación N:M y validaciones de formularios.
- Contacto, honeypot y validación de email/longitud.
- Modelos: hash de contraseña, encapsulamiento, polimorfismo, fechas y serialización.

---

## Documentación

- **Documentación preliminar (PDF):** `docs/Documentacion_Preliminar_Portfolio.pdf`
  Incluye planificación, objetivos, arquitectura, modelo lógico y físico, POO, seguridad, responsive, animaciones, pruebas, despliegue, checklist y DDL completo.
- **Guía de despliegue:** `docs/Guia_Despliegue.md`
- **Regenerar la documentación:**

```powershell
.\.venv\Scripts\python.exe scripts\generar_documentacion.py
```

---

## Despliegue en Clever Cloud

La guía detallada está en [`docs/Guia_Despliegue.md`](docs/Guia_Despliegue.md). Resumen:

1. Crear una aplicación **Python** en Clever Cloud.
2. Agregar el add-on **MySQL**.
3. Configurar las variables de entorno:

```text
CC_PYTHON_MODULE=wsgi:app
CC_PYTHON_BACKEND=gunicorn
CC_PYTHON_VERSION=3.12
SECRET_KEY=<clave aleatoria larga>
ADMIN_USERNAME=kevinAdmin
ADMIN_PASSWORD=<contraseña segura>
SITE_URL=https://<tu-app>.cleverapps.io
SITE_NAME=Kevin | Portfolio
SEED_ON_START=1
SESSION_COOKIE_SECURE=true
```

4. Vincular el repositorio de GitHub y desplegar.
5. Verificar `https://<tu-app>.cleverapps.io/salud`.
6. Abrir el sitio, iniciar sesión y cambiar la contraseña.
7. Reemplazar los datos de ejemplo (email, teléfono, redes y URLs de proyectos).
8. Descargar el CV y verificar que refleje los datos reales.

> Clever Cloud inyecta automáticamente `MYSQL_ADDON_URI` y las variables `MYSQL_ADDON_*` al vincular el add-on. La aplicación detecta esas variables sin configuración adicional.

---

## Git y GitHub

```bash
git init
git add .
git commit -m "Proyecto integrador: portfolio full stack Flask + MySQL"
git branch -M main
git remote add origin https://github.com/USUARIO/portfolio2.git
git push -u origin main
```

El repositorio incluye `.gitignore` para excluir `.venv`, `.env`, `instance/`, cachés y archivos temporales.

> En este equipo Git no está instalado actualmente. Instalarlo desde <https://git-scm.com/download/win> y reiniciar la terminal antes de ejecutar los comandos.

---

## Seguridad

- Contraseñas con hash **scrypt** (Werkzeug); nunca se guardan en texto plano.
- **CSRF** en todos los formularios y operaciones POST (Flask-WTF).
- **Flask-Login** protege todo el blueprint `/admin` mediante `before_request`.
- Validación del servidor con WTForms (tipos, longitudes, emails, URLs, fechas y rangos).
- Consultas parametrizadas por SQLAlchemy (sin concatenar SQL).
- Autoescape de Jinja2 y escape de texto en los PDF.
- Redirección `next` validada para evitar *open redirect*.
- Mensaje genérico ante credenciales incorrectas (sin enumerar usuarios).
- Honeypot anti-spam en el formulario público.
- Cookies `HttpOnly`, `SameSite=Lax` y `Secure` configurable.
- Cabeceras `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy` y `Permissions-Policy`.
- `/admin` bloqueado en `robots.txt` y con `noindex, nofollow`.

**Checklist antes de publicar:**

- [ ] `SECRET_KEY` aleatoria y privada.
- [ ] Contraseña del administrador cambiada.
- [ ] `SESSION_COOKIE_SECURE=true` y HTTPS.
- [ ] Datos personales reales cargados.
- [ ] `SITE_URL` con el dominio final.
- [ ] `.env` fuera del repositorio.
- [ ] Base de datos con backup o plan de respaldo.

---

## Mapeo de requisitos

| Requisito | Implementación |
| --- | --- |
| Datos personales, estudios, experiencia, tecnologías y contenido extra | Secciones públicas + proyectos, mapa y contacto |
| Backend Python/Flask | `portfolio/__init__.py`, `portfolio/routes/` |
| Frontend Jinja2 | `portfolio/templates/` |
| MySQL en Clever Cloud | `config.py`, `database/schema_mysql.sql` |
| Login usuario/contraseña | `routes/auth.py`, Flask-Login |
| Contraseña hasheada + Flask-WTF | `models.Usuario`, `forms.py` |
| Iframe | Mapa OpenStreetMap en `index.html` |
| Iconos FontAwesome | CDN en `base.html` y `admin/base.html` |
| Google Fonts | `base.html` + `styles.css` |
| Favicon y logo | `static/img/favicon.svg`, `logo.svg` |
| POO con 4 pilares | `portfolio/models.py` (comentarios por pilar) |
| Responsive | Breakpoints `1024px`, `820px`, `560px` en `styles.css` |
| Animaciones | `main.js` (typewriter, reveal, contadores) y `styles.css` (chips flotantes, pulse, hover) |
| Modelo relacional y físico | Sección 5 del PDF + `database/schema_mysql.sql` |
| CV en PDF | `portfolio/pdf.py`, ruta `/cv` |
| Documentación PDF | `docs/Documentacion_Preliminar_Portfolio.pdf` |
| Git/GitHub y publicación | Pendiente de credenciales (ver estado) |

La tabla completa de trazabilidad está en el PDF de documentación.

---

## Solución de problemas

**`ModuleNotFoundError` al ejecutar**
Verificar que el entorno virtual esté activo y las dependencias instaladas:
```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

**Error de conexión a MySQL**
Revisar `DATABASE_URL`, que el servidor MySQL esté iniciado y que la base exista. Para probar sin MySQL, dejar `DATABASE_URL` vacío y usar SQLite.

**`CSRF token missing`**
El formulario debe enviarse desde la página (incluye `hidden_tag()`), no con una petición manual sin token. En pruebas, `TestingConfig` desactiva CSRF.

**La contraseña inicial no funciona**
Si la base ya existía, el seed no se vuelve a ejecutar. Crear/actualizar el administrador:
```powershell
.\.venv\Scripts\flask --app wsgi create-admin --username admin
```

**El CV no refleja los cambios**
El PDF se genera en cada descarga. Verificar que los cambios estén guardados y que el perfil tenga los datos actualizados.

**Git no se reconoce**
Instalar Git y reiniciar la terminal. Luego verificar con `git --version`.

---

## Autor

**Kevin** — Desarrollador Full Stack en formación
Proyecto Integrador · Tecnicatura Superior en Desarrollo de Software · Noviembre de 2026

- Portfolio: pendiente de publicación
- GitHub: pendiente de publicar
- Contacto: `kevin@ejemplo.com` (reemplazar por el email real)
