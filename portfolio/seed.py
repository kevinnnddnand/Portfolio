"""Datos iniciales del portfolio.

El seed es idempotente: si ya existe un perfil no vuelve a crear contenido.
Se ejecuta automáticamente en desarrollo (`SEED_ON_START=1`) o mediante
`flask seed-db`.
"""
from __future__ import annotations

from datetime import date

from .extensions import db
from .models import (
    Estudio,
    Experiencia,
    Perfil,
    Proyecto,
    Tecnologia,
    Usuario,
)


def crear_admin(username: str, password: str, nombre: str = "Administrador") -> Usuario:
    """Crea (o actualiza la clave de) la cuenta administradora."""
    usuario = Usuario.query.filter_by(username=username.strip().lower()).first()
    if usuario is None:
        usuario = Usuario(username=username.strip().lower(), nombre=nombre)
        db.session.add(usuario)
    usuario.nombre = nombre
    usuario.activo = True
    usuario.set_password(password)
    db.session.commit()
    return usuario


def _seed_tecnologias() -> dict[str, Tecnologia]:
    datos = [
        ("Python", "Backend", 85, "fa-brands fa-python", "#3776ab"),
        ("Flask", "Backend", 82, "fa-solid fa-flask", "#0f766e"),
        ("HTML5", "Frontend", 90, "fa-brands fa-html5", "#e34f26"),
        ("CSS3", "Frontend", 86, "fa-brands fa-css3-alt", "#1572b6"),
        ("JavaScript", "Frontend", 76, "fa-brands fa-js", "#b58900"),
        ("MySQL", "Base de datos", 78, "fa-solid fa-database", "#00758f"),
        ("Git", "Herramientas", 82, "fa-brands fa-git-alt", "#f05032"),
    ]
    tecnologias: dict[str, Tecnologia] = {}
    for orden, (nombre, categoria, nivel, icono, color) in enumerate(datos, start=1):
        tecnologia = Tecnologia(
            nombre=nombre,
            categoria=categoria,
            nivel=nivel,
            icono=icono,
            color=color,
            orden=orden,
            activo=True,
        )
        db.session.add(tecnologia)
        tecnologias[nombre] = tecnologia
    db.session.flush()
    return tecnologias


def seed_database(admin_username: str, admin_password: str, admin_nombre: str = "Kevin") -> bool:
    """Crea el contenido de demostración si la base está vacía.

    Devuelve True cuando insertó datos y False si ya existía un perfil.
    """
    if Perfil.query.first() is not None:
        return False

    admin = Usuario.query.filter_by(username=admin_username.strip().lower()).first()
    if admin is None:
        admin = Usuario(username=admin_username.strip().lower(), nombre=admin_nombre)
        db.session.add(admin)
        admin.set_password(admin_password)
    db.session.flush()

    perfil = Perfil(
        usuario_id=admin.id,
        nombre="Kevin",
        apellido="",
        titulo="Desarrollador Full Stack",
        subtitulo="Python · Flask · MySQL · Jinja2",
        bio=(
            "Soy desarrollador full stack en formación, enfocado en construir "
            "aplicaciones web claras, accesibles y mantenibles. Disfruto convertir "
            "ideas en productos funcionales: desde el modelo de datos y la API con "
            "Flask hasta una interfaz cuidada con HTML, CSS y JavaScript. "
            "Actualmente profundizo mis conocimientos en Python, bases de datos "
            "relacionales y buenas prácticas de desarrollo."
        ),
        ubicacion="Villa San Nicolás, Malagueño, Córdoba, Argentina",
        disponibilidad="Disponible para oportunidades full stack",
        cv_resumen=(
            "Desarrollador Full Stack con experiencia en el desarrollo de "
            "aplicaciones web utilizando Python, Flask, MySQL y Jinja2. "
            "Perfil orientado a la resolución de problemas, el trabajo en equipo "
            "y el aprendizaje continuo."
        ),
        avatar_url="img/avatar.svg",
    )
    perfil.email = "kevin@ejemplo.com"
    perfil.telefono = "+54 11 0000-0000"
    perfil.linkedin = "https://www.linkedin.com/"
    perfil.github = "https://github.com/"
    perfil.sitio_web = ""
    db.session.add(perfil)

    estudios = [
        Estudio(
            institucion="Instituto Superior de Formación Técnica",
            titulo="Tecnicatura Superior en Desarrollo de Software",
            area="Desarrollo de software",
            nivel="Terciario",
            fecha_inicio=date(2024, 3, 1),
            en_curso=True,
            descripcion=(
                "Formación en algoritmos, estructuras de datos, bases de datos "
                "relacionales, desarrollo web y programación orientada a objetos. "
                "Proyecto integrador: portfolio full stack con Flask y MySQL."
            ),
            orden=1,
        ),
        Estudio(
            institucion="Plataforma de educación online",
            titulo="Curso Full Stack con Python y Flask",
            area="Desarrollo web",
            nivel="Curso",
            fecha_inicio=date(2023, 8, 1),
            fecha_fin=date(2024, 3, 1),
            descripcion=(
                "Desarrollo de aplicaciones web con Flask, Jinja2 y bases de datos "
                "MySQL. Autenticación, CRUD, maquetación responsive y despliegue."
            ),
            orden=2,
        ),
        Estudio(
            institucion="Escuela Secundaria",
            titulo="Bachillerato",
            area="Formación general",
            nivel="Secundario",
            fecha_inicio=date(2013, 3, 1),
            fecha_fin=date(2019, 12, 1),
            descripcion="Formación secundaria completa.",
            orden=3,
        ),
    ]
    db.session.add_all(estudios)

    experiencias = [
        Experiencia(
            empresa="Proyectos propios y clientes freelance",
            puesto="Desarrollador Web Full Stack",
            ubicacion="Villa San Nicolás, Malagueño, Córdoba, Argentina",
            modalidad="Remoto",
            fecha_inicio=date(2024, 6, 1),
            actual=True,
            descripcion=(
                "Diseño y desarrollo de aplicaciones web para pequeños negocios y "
                "proyectos personales, desde la relevación de necesidades hasta la "
                "puesta en producción."
            ),
            logros=(
                "Desarrollé APIs REST con Flask y persistencia en MySQL.\n"
                "Implementé interfaces responsive con HTML, CSS y JavaScript.\n"
                "Automaticé tareas de carga de datos con scripts en Python."
            ),
            orden=1,
        ),
        Experiencia(
            empresa="TechSoluciones",
            puesto="Soporte Técnico IT",
            ubicacion="Villa San Nicolás, Malagueño, Córdoba, Argentina",
            modalidad="Híbrido",
            fecha_inicio=date(2022, 1, 1),
            fecha_fin=date(2024, 5, 31),
            descripcion=(
                "Atención de incidencias técnicas, configuración de equipos y "
                "acompañamiento a usuarios en herramientas digitales."
            ),
            logros=(
                "Resolví más de 200 tickets con seguimiento y documentación.\n"
                "Documenté procedimientos internos que redujeron tiempos de respuesta.\n"
                "Capacité a usuarios en el uso de herramientas colaborativas."
            ),
            orden=2,
        ),
    ]
    db.session.add_all(experiencias)

    tecnologias = _seed_tecnologias()

    proyectos = [
        Proyecto(
            titulo="Portfolio Web Full Stack",
            descripcion=(
                "Sitio personal con panel de administración, autenticación segura, "
                "base de datos relacional y generación dinámica del CV. Construido "
                "con Flask, Jinja2, MySQL y POO."
            ),
            repo_url="https://github.com/",
            demo_url="",
            imagen_url="img/proyecto-portfolio.svg",
            destacado=True,
            orden=1,
            tecnologias=[
                tecnologias["Python"], tecnologias["Flask"],
                tecnologias["MySQL"], tecnologias["HTML5"],
            ],
        ),
        Proyecto(
            titulo="Gestor de Tareas Colaborativo",
            descripcion=(
                "Aplicación web para organizar tareas por proyecto y responsable, "
                "con autenticación, filtros y actualización del estado en tiempo real."
            ),
            repo_url="https://github.com/",
            demo_url="",
            imagen_url="img/proyecto-tareas.svg",
            destacado=True,
            orden=2,
            tecnologias=[
                tecnologias["Python"], tecnologias["Flask"],
                tecnologias["JavaScript"], tecnologias["CSS3"],
            ],
        ),
        Proyecto(
            titulo="Panel de Análisis de Ventas",
            descripcion=(
                "Dashboard que procesa datos de ventas con Python y MySQL y los "
                "presenta en gráficos y tablas resumen para la toma de decisiones."
            ),
            repo_url="https://github.com/",
            demo_url="",
            imagen_url="img/proyecto-ventas.svg",
            destacado=False,
            orden=3,
            tecnologias=[
                tecnologias["Python"], tecnologias["MySQL"],
                tecnologias["JavaScript"], tecnologias["HTML5"],
            ],
        ),
    ]
    db.session.add_all(proyectos)
    db.session.commit()
    return True


def seed_inicial(config) -> bool:
    """Helper usado por la app y por la CLI."""
    return seed_database(
        admin_username=config.get("ADMIN_USERNAME", "kevinAdmin"),
        admin_password=config.get("ADMIN_PASSWORD", "kevin1504"),
        admin_nombre=config.get("ADMIN_NOMBRE", "Kevin"),
    )
