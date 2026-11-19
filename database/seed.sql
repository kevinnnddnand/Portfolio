-- =============================================================================
-- Datos iniciales de demostración (MySQL 8.x)
--
-- IMPORTANTE:
--   * Ejecutar únicamente sobre una base recién creada con schema_mysql.sql.
--   * La aplicación también puede cargar estos datos automáticamente con
--     `flask seed-db` (o al iniciar con SEED_ON_START=1). En ese caso NO es
--     necesario ejecutar este archivo.
--   * Credenciales del administrador definidas aquí:
--       usuario: kevinAdmin
--       contraseña: kevin1504
--     Cambiarlas antes de publicar el sitio desde "Mi cuenta" en el panel.
-- =============================================================================

USE portfolio;

-- ---------------------------------------------------------------------------
-- Usuario administrador
-- El hash corresponde a kevin1504 (Werkzeug scrypt, nunca se guarda la clave).
-- ---------------------------------------------------------------------------
INSERT INTO usuarios (id, username, password_hash, nombre, activo, creado_en)
VALUES (
  1,
  'kevinAdmin',
  'scrypt:32768:8:1$1xKBAXMGkSVqER4K$b75bfc57e02c7cd65f0e99c3800eb06b3ca529f503e8bebdeb69c8f09c2a587e37c5ff6c49f87d7e7227461066723ac5eb2f1a7e6ee592c2e50b757128c17435',
  'Kevin',
  1,
  NOW()
);

-- ---------------------------------------------------------------------------
-- Perfil
-- ---------------------------------------------------------------------------
INSERT INTO perfil (
  id, usuario_id, nombre, apellido, titulo, subtitulo, bio, email, telefono,
  ubicacion, linkedin, github, sitio_web, disponibilidad, cv_resumen,
  avatar_url, actualizado_en
) VALUES (
  1,
  1,
  'Kevin',
  '',
  'Desarrollador Full Stack',
  'Python · Flask · MySQL · Jinja2',
  'Soy desarrollador full stack en formación, enfocado en construir aplicaciones web claras, accesibles y mantenibles. Disfruto convertir ideas en productos funcionales: desde el modelo de datos y la API con Flask hasta una interfaz cuidada con HTML, CSS y JavaScript. Actualmente profundizo mis conocimientos en Python, bases de datos relacionales y buenas prácticas de desarrollo.',
  'kevin@ejemplo.com',
  '+54 11 0000-0000',
  'Villa San Nicolás, Malagueño, Córdoba, Argentina',
  'https://www.linkedin.com/',
  'https://github.com/',
  NULL,
  'Disponible para oportunidades full stack',
  'Desarrollador Full Stack con experiencia en el desarrollo de aplicaciones web utilizando Python, Flask, MySQL y Jinja2. Perfil orientado a la resolución de problemas, el trabajo en equipo y el aprendizaje continuo.',
  'img/avatar.svg',
  NOW()
);

-- ---------------------------------------------------------------------------
-- Estudios
-- ---------------------------------------------------------------------------
INSERT INTO estudios (
  id, institucion, titulo, area, nivel, fecha_inicio, fecha_fin, en_curso,
  descripcion, orden, activo, creado_en
) VALUES
(
  1,
  'Instituto Superior de Formación Técnica',
  'Tecnicatura Superior en Desarrollo de Software',
  'Desarrollo de software',
  'Terciario',
  '2024-03-01',
  NULL,
  1,
  'Formación en algoritmos, estructuras de datos, bases de datos relacionales, desarrollo web y programación orientada a objetos. Proyecto integrador: portfolio full stack con Flask y MySQL.',
  1,
  1,
  NOW()
),
(
  2,
  'Plataforma de educación online',
  'Curso Full Stack con Python y Flask',
  'Desarrollo web',
  'Curso',
  '2023-08-01',
  '2024-03-01',
  0,
  'Desarrollo de aplicaciones web con Flask, Jinja2 y bases de datos MySQL. Autenticación, CRUD, maquetación responsive y despliegue.',
  2,
  1,
  NOW()
),
(
  3,
  'Escuela Secundaria',
  'Bachillerato',
  'Formación general',
  'Secundario',
  '2013-03-01',
  '2019-12-01',
  0,
  'Formación secundaria completa.',
  3,
  1,
  NOW()
);

-- ---------------------------------------------------------------------------
-- Experiencias
-- ---------------------------------------------------------------------------
INSERT INTO experiencias (
  id, empresa, puesto, ubicacion, modalidad, fecha_inicio, fecha_fin, actual,
  descripcion, logros, orden, activo, creado_en
) VALUES
(
  1,
  'Proyectos propios y clientes freelance',
  'Desarrollador Web Full Stack',
  'Villa San Nicolás, Malagueño, Córdoba, Argentina',
  'Remoto',
  '2024-06-01',
  NULL,
  1,
  'Diseño y desarrollo de aplicaciones web para pequeños negocios y proyectos personales, desde la relevación de necesidades hasta la puesta en producción.',
  'Desarrollé APIs REST con Flask y persistencia en MySQL.\nImplementé interfaces responsive con HTML, CSS y JavaScript.\nAutomaticé tareas de carga de datos con scripts en Python.',
  1,
  1,
  NOW()
),
(
  2,
  'TechSoluciones',
  'Soporte Técnico IT',
  'Villa San Nicolás, Malagueño, Córdoba, Argentina',
  'Híbrido',
  '2022-01-01',
  '2024-05-31',
  0,
  'Atención de incidencias técnicas, configuración de equipos y acompañamiento a usuarios en herramientas digitales.',
  'Resolví más de 200 tickets con seguimiento y documentación.\nDocumenté procedimientos internos que redujeron tiempos de respuesta.\nCapacité a usuarios en el uso de herramientas colaborativas.',
  2,
  1,
  NOW()
);

-- ---------------------------------------------------------------------------
-- Tecnologías
-- ---------------------------------------------------------------------------
INSERT INTO tecnologias (id, nombre, categoria, nivel, icono, color, orden, activo) VALUES
(1, 'Python',     'Backend',        85, 'fa-brands fa-python',     '#3776ab', 1, 1),
(2, 'Flask',      'Backend',        82, 'fa-solid fa-flask',       '#0f766e', 2, 1),
(3, 'HTML5',      'Frontend',       90, 'fa-brands fa-html5',      '#e34f26', 3, 1),
(4, 'CSS3',       'Frontend',       86, 'fa-brands fa-css3-alt',   '#1572b6', 4, 1),
(5, 'JavaScript', 'Frontend',       76, 'fa-brands fa-js',         '#b58900', 5, 1),
(6, 'MySQL',      'Base de datos',  78, 'fa-solid fa-database',    '#00758f', 6, 1),
(7, 'Git',        'Herramientas',   82, 'fa-brands fa-git-alt',    '#f05032', 7, 1);

-- ---------------------------------------------------------------------------
-- Proyectos
-- ---------------------------------------------------------------------------
INSERT INTO proyectos (
  id, titulo, descripcion, repo_url, demo_url, imagen_url, destacado, orden,
  activo, creado_en
) VALUES
(
  1,
  'Portfolio Web Full Stack',
  'Sitio personal con panel de administración, autenticación segura, base de datos relacional y generación dinámica del CV. Construido con Flask, Jinja2, MySQL y POO.',
  'https://github.com/',
  NULL,
  'img/proyecto-portfolio.svg',
  1,
  1,
  1,
  NOW()
),
(
  2,
  'Gestor de Tareas Colaborativo',
  'Aplicación web para organizar tareas por proyecto y responsable, con autenticación, filtros y actualización del estado en tiempo real.',
  'https://github.com/',
  NULL,
  'img/proyecto-tareas.svg',
  1,
  2,
  1,
  NOW()
),
(
  3,
  'Panel de Análisis de Ventas',
  'Dashboard que procesa datos de ventas con Python y MySQL y los presenta en gráficos y tablas resumen para la toma de decisiones.',
  'https://github.com/',
  NULL,
  'img/proyecto-ventas.svg',
  0,
  3,
  1,
  NOW()
);

-- ---------------------------------------------------------------------------
-- Relación N:M proyecto ↔ tecnología
-- ---------------------------------------------------------------------------
INSERT INTO proyecto_tecnologia (proyecto_id, tecnologia_id) VALUES
-- Portfolio Web Full Stack
(1, 1), (1, 2), (1, 3), (1, 6),
-- Gestor de Tareas Colaborativo
(2, 1), (2, 2), (2, 4), (2, 5),
-- Panel de Análisis de Ventas
(3, 1), (3, 3), (3, 5), (3, 6);

-- ---------------------------------------------------------------------------
-- Mensaje de ejemplo para ver el panel de mensajes (opcional)
-- ---------------------------------------------------------------------------
INSERT INTO mensajes (nombre, email, asunto, mensaje, leido, creado_en) VALUES
(
  'María López',
  'maria.lopez@ejemplo.com',
  'Propuesta de colaboración',
  'Hola Kevin, vi tu portfolio y me gustaría conversar sobre un proyecto de desarrollo web. ¿Tenés disponibilidad este mes?',
  0,
  NOW()
);

-- Fin del script.
