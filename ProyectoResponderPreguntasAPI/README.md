
# API de Respuesta a Preguntas - FastAPI & Hugging Face

## Descripción

Esta API permite a los usuarios hacer preguntas sobre un contexto textual y obtener respuestas generadas utilizando un modelo de *question-answering* de Hugging Face. El modelo utilizado es `bert-large-uncased-whole-word-masking-finetuned-squad`, que está optimizado para encontrar respuestas dentro de un contexto específico.

La API está desarrollada con **FastAPI**, un framework rápido y moderno para construir APIs con Python 3.6+ basado en **Starlette** y **Pydantic**. Utiliza el modelo preentrenado de **Hugging Face** para tareas de *question-answering*, lo que permite a los usuarios obtener respuestas precisas y contextuales a partir de un texto proporcionado.

## Características

- Responde preguntas basadas en un contexto textual utilizando el modelo `bert-large-uncased-whole-word-masking-finetuned-squad`.
- Fácil de integrar con otros sistemas a través de una API RESTful.
- Rápida y eficiente, diseñada para ser ejecutada en producción.

## Modelo Usado

- **Modelo de Hugging Face:** `bert-large-uncased-whole-word-masking-finetuned-squad`
- **Descripción del Modelo:** Este modelo es una variante más grande y refinada de BERT, entrenada específicamente para tareas de *question-answering*. Utiliza un mecanismo de atención para encontrar las respuestas más relevantes dentro de un contexto dado. El modelo es robusto para preguntas directas sobre hechos presentados en textos.

### Detalles del modelo:

- **Tarea:** *Question-Answering*
- **Framework:** PyTorch (`pt`)
- **Tamaño del Modelo:** Grande, optimizado para obtener respuestas dentro de un contexto largo.
- **Entrenamiento:** Finetuning sobre el dataset SQuAD (Stanford Question Answering Dataset).

## Instalación

### Requisitos

Este proyecto requiere Python 3.6+ y las siguientes dependencias. Puedes instalar las dependencias utilizando **pip**.

1. Clona el repositorio o descarga el código fuente.

2. Instala las dependencias:

   ```bash
   pip install fastapi uvicorn transformers torch pydantic
   ```

### Ejecutar el Servidor

Para ejecutar la API de manera local, usa **Uvicorn**, que es un servidor ASGI recomendado para FastAPI.

1. Inicia el servidor:

   ```bash
   uvicorn app:app --reload
   ```

2. El servidor estará corriendo en `http://localhost:8000`. Puedes acceder a la documentación interactiva de la API utilizando [Swagger UI](http://localhost:8000/docs).

## Uso de la API

### Endpoint Raíz

#### `GET /`

Verifica si la API está en funcionamiento.

**Respuesta exitosa:**

```json
{
  "message": "API de Respuesta a Preguntas está en ejecución"
}
```

### Endpoint de Pregunta

#### `POST /ask`

Permite al usuario enviar una pregunta y un contexto y obtener una respuesta generada por el modelo.

**Solicitud:**

Envía un cuerpo JSON con los campos `question` (pregunta) y `context` (contexto). Ejemplo de solicitud:

```json
{
  "question": "¿Quién es el presidente de los Estados Unidos?",
  "context": "Joe Biden es el presidente de los Estados Unidos desde enero de 2021."
}
```

**Respuesta:**

La respuesta será un objeto JSON que contiene la `answer` (respuesta generada) y el `score` (puntuación de confianza). Ejemplo de respuesta:

```json
{
  "answer": "Joe Biden",
  "score": 0.98
}
```

**Detalles de la respuesta:**

- `answer`: La respuesta generada por el modelo.
- `score`: La puntuación de confianza del modelo para la respuesta dada, entre 0 y 1.

### Ejemplo de flujo completo:

1. Realiza una solicitud `POST` al endpoint `/ask` con el siguiente JSON:

   ```json
   {
     "question": "¿Cuál es la capital de Francia?",
     "context": "París es la capital de Francia y una de las principales ciudades de Europa."
   }
   ```

2. La respuesta sería:

   ```json
   {
     "answer": "París",
     "score": 0.99
   }
   ```

### Errores comunes

- **400 Bad Request**: Si la solicitud no contiene los campos `question` o `context`, o si hay un error al procesar los datos.
- **500 Internal Server Error**: Si el modelo no puede procesar la solicitud debido a un error interno.

## Consideraciones de rendimiento

El modelo `bert-large-uncased-whole-word-masking-finetuned-squad` es un modelo grande y puede requerir una cantidad significativa de memoria y poder de procesamiento, especialmente en entornos con múltiples solicitudes simultáneas. Para optimizar el rendimiento, considera el uso de un servidor con suficiente capacidad de hardware (por ejemplo, GPUs para cargas pesadas) o el uso de modelos más pequeños si el rendimiento es un factor crítico.

