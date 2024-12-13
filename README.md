# Proyecto de Escaneo de Puertos y Resolución DNS en Python

Este proyecto se inspira en el libro **"Python Aplicado a Seguridad y Redes"** de José Manuel Ortega Candel. Aunque se basa en los principios y conceptos expuestos en el libro, el código implementado en este proyecto no es una reproducción directa del mismo. En lugar de eso, se ha adaptado y ampliado para crear herramientas de análisis de redes utilizando Python, orientadas a la seguridad informática.

## Estado del Proyecto

- **Estado:** En desarrollo
- **Objetivo:** Proporcionar herramientas básicas de análisis de redes mediante Python para prácticas de seguridad informática.
- **Tecnologías:** Python, Sockets

## Funcionalidades

El proyecto incluye varios scripts que realizan las siguientes funciones:

1. **Obtención de Información de DNS:**
   - Resolución de nombres de dominio a direcciones IP.
   - Obtención de información sobre una dirección IP y su nombre de host.

2. **Escaneo de Puertos:**
   - Escaneo de puertos en una dirección IP específica para detectar puertos abiertos.
   - Escaneo de puertos en un dominio, con la opción de seleccionar puertos específicos.
   - Escaneo de un rango de puertos de una dirección IP.
   - Escaneo de puertos en un único host o dominio.

3. **Escaneo de Múltiples Puertos en Paralelo:**
   - Utiliza hilos para realizar el escaneo de puertos de manera concurrente, mejorando la eficiencia del proceso.

## Instalación

### Requisitos previos
Para ejecutar este proyecto, necesitas tener Python 3 instalado en tu sistema. Además, se requieren algunos módulos de Python, que puedes instalar ejecutando:

```bash
pip install socket threading optparse
