# -*- coding: utf-8 -*-
"""
Script en Python para agregar animaciones dinámicas a todos los iconos
del portal académico "Materias vistas con Mahecha".
Compatible con publicación estática en GitHub Pages.
"""

from pathlib import Path

RUTA_CSS = Path("css/estilos.css")

BLOQUE_ANIMACIONES_CSS = """
/* ==================================
   ANIMACIONES DE ICONOS (GENERADAS CON PYTHON)
================================== */

@keyframes flotarIcono {
    0%, 100% {
        transform: translateY(0) scale(1);
    }
    50% {
        transform: translateY(-6px) scale(1.06);
    }
}

@keyframes pulsoNeon {
    0%, 100% {
        box-shadow: 0 0 15px rgba(0, 229, 255, 0.25), inset 0 0 12px rgba(0, 229, 255, 0.15);
        border-color: rgba(0, 229, 255, 0.45);
    }
    50% {
        box-shadow: 0 0 28px rgba(0, 229, 255, 0.65), inset 0 0 20px rgba(0, 229, 255, 0.35);
        border-color: #00E5FF;
    }
}

@keyframes giroSuaveHover {
    0% {
        transform: scale(1) rotate(0deg);
    }
    35% {
        transform: scale(1.18) rotate(-10deg);
    }
    70% {
        transform: scale(1.18) rotate(8deg);
    }
    100% {
        transform: scale(1.12) rotate(0deg);
    }
}

@keyframes latidoInsignia {
    0%, 100% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.04);
    }
}

/* Logo / Marca superior (MM, L3, AS) */
.brand-mark {
    animation: flotarIcono 3.4s ease-in-out infinite, pulsoNeon 2.8s ease-in-out infinite;
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.35s ease;
}

.brand-row:hover .brand-mark {
    animation: giroSuaveHover 0.65s ease forwards;
    box-shadow: 0 0 35px rgba(0, 229, 255, 0.85), inset 0 0 22px rgba(0, 229, 255, 0.45);
}

/* Iconos de las tarjetas (.card-icon) */
.card-icon {
    animation: flotarIcono 3.8s ease-in-out infinite, pulsoNeon 3.2s ease-in-out infinite;
    transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    will-change: transform, box-shadow;
}

/* Desfase de animación entre tarjetas para efecto ola */
.card:nth-child(1) .card-icon,
.subject-card-btn:nth-child(1) .card-icon {
    animation-delay: 0s;
}

.card:nth-child(2) .card-icon,
.subject-card-btn:nth-child(2) .card-icon {
    animation-delay: 0.45s;
}

.card:nth-child(3) .card-icon {
    animation-delay: 0.9s;
}

/* Reacción animada al pasar el cursor sobre la tarjeta o botón de materia */
.card:hover .card-icon,
.subject-card-btn:hover .card-icon {
    animation: giroSuaveHover 0.6s ease forwards;
    background: linear-gradient(135deg, rgba(0, 229, 255, 0.28), rgba(59, 130, 246, 0.28));
    border-color: var(--acento);
    color: #FFFFFF;
    box-shadow: 0 0 28px rgba(0, 229, 255, 0.7);
}

/* Etiquetas superiores con icono (.eyebrow) */
.eyebrow {
    animation: latidoInsignia 3s ease-in-out infinite;
}
"""


def aplicar_animaciones():
    if not RUTA_CSS.exists():
        raise FileNotFoundError(f"No se encontró el archivo {RUTA_CSS}")

    contenido = RUTA_CSS.read_text(encoding="utf-8")

    marcador = "ANIMACIONES DE ICONOS (GENERADAS CON PYTHON)"
    if marcador not in contenido:
        contenido = contenido.rstrip() + "\n\n" + BLOQUE_ANIMACIONES_CSS.strip() + "\n"
        RUTA_CSS.write_text(contenido, encoding="utf-8")
        print("✅ Animaciones de iconos inyectadas exitosamente en css/estilos.css")
    else:
        print("ℹ️ Las animaciones ya estaban presentes en css/estilos.css")


if __name__ == "__main__":
    aplicar_animaciones()
