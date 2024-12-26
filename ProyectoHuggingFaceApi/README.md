
# Ejecución Local de Modelos con DETR

Este proyecto demuestra cómo ejecutar localmente el modelo DETR (DEtection TRansformer) para realizar detección de objetos en una imagen. Incluye una implementación funcional que utiliza la librería Transformers de Hugging Face. Además, se proporciona un ejemplo práctico, detalles de configuración y una descripción del aprendizaje adquirido sobre transformers.

## Requisitos para la Ejecución

### Requisitos de Hardware
- Sistema con capacidad para ejecutar PyTorch (CPU o GPU recomendado para un mejor rendimiento).

### Requisitos de Software
- Python 3.8 o superior.

### Librerías requeridas
- `torch`
- `transformers`
- `Pillow`
- `matplotlib`

Puedes instalar todas las dependencias ejecutando:

```bash
pip install torch transformers Pillow matplotlib
```

## Tutorial de Uso e Instalación

### 1. Clonar el Repositorio

Descarga o clona el código en tu máquina local:

```bash
git clone <URL_DEL_REPOSITORIO>
cd <CARPETA_DEL_PROYECTO>
```

### 2. Asegúrate de Tener las Dependencias

Instala las librerías requeridas como se describe en los "Requisitos de Software".

### 3. Proveer una Imagen de Entrada

En la carpeta images agrega una imagen en el directorio del proyecto. Por ejemplo, una imagen llamada `city.jpg`.

### 4. Ejecutar el Script

Ejecuta el código Python para realizar la detección de objetos en la imagen de entrada:

```bash
python main.py
```

### Qué Hace el Script
- Detecta objetos en la imagen proporcionada.
- Genera una versión de la imagen con las detecciones resaltadas.
- Imprime en consola los objetos detectados, sus niveles de confianza y las coordenadas de las cajas delimitadoras.

## Ejemplos de Ejecución

### Entrada:
- Imagen: `city.jpg` (una imagen de ejemplo con varios objetos).

### Salida:
1. Una versión modificada de la imagen con los objetos detectados resaltados (se muestra en pantalla).
2. Información de los objetos detectados en consola, como:

```plaintext
Objetos detectados:
- car (Confianza: 0.85) en Caja: [x_min, y_min, x_max, y_max]
- person (Confianza: 0.78) en Caja: [x_min, y_min, x_max, y_max]
```

## Aprendizaje sobre Transformers y Ejecución Local

### DETR (DEtection TRansformer)
DETR es un modelo de detección de objetos basado en transformers desarrollado por Facebook AI. Combina la arquitectura de transformers con una red convolucional para realizar detección y clasificación de objetos en una única etapa. La clave de su funcionamiento radica en:

1. Utilizar un codificador-transformador para procesar la imagen como secuencia.
2. Generar representaciones de alta calidad para cada región de la imagen.

### Implementación Local
En esta implementación:
- **Procesamiento de la Imagen:** Se utiliza `DetrImageProcessor` para preparar la imagen de entrada.
- **Predicción:** El modelo DETR (`facebook/detr-resnet-101`) realiza la detección.
- **Post-procesamiento:** Se filtran resultados basados en un umbral de confianza (70%).
- **Visualización:** Se dibujan las cajas delimitadoras y etiquetas en la imagen.

### Lo Aprendido
1. **Uso de Transformers:** Aprendí a utilizar modelos preentrenados de Hugging Face para tareas de detección de objetos.
2. **Personalización de Resultados:** Implementé filtros y visualizaciones personalizadas para mejorar la interpretabilidad de las predicciones.
3. **Ejecución Local:** Entendí cómo integrar modelos avanzados en proyectos locales, optimizando el rendimiento para diferentes entornos.

---

Este proyecto sirve como una excelente base para explorar técnicas avanzadas de visión por computadora y puede ampliarse para incluir funcionalidades como:
- Detección en tiempo real.
- Aplicaciones en video.
- Análisis adicional de las predicciones.
