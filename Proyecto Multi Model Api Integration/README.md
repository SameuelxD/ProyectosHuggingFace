
# Model Pipeline

## Descripción
Este proyecto implementa una tubería de procesamiento de datos que utiliza múltiples modelos alojados en la API de Hugging Face. La clase `ModelPipeline` permite iterar de un modelo a otro de forma secuencial, transformando las salidas generadas para que sean entradas adecuadas para el siguiente modelo. Esto permite realizar tareas complejas como generación de texto, traducción, resumen y análisis de sentimientos.

---

## Características
- **Manejo de múltiples modelos:** Se pueden registrar y utilizar diferentes modelos alojados en la API de Hugging Face.
- **Iteración entre modelos:** La salida de cada modelo se transforma para ser compatible como entrada del siguiente.
- **Reintentos automáticos:** Si un modelo está cargándose (error 503), el sistema reintenta la petición hasta cinco veces.
- **Validaciones:** Se asegura que las entradas y salidas sean válidas para evitar errores durante la ejecución.

---

## Modelos Utilizados

### 1. **GPT-2 (Text Generation)**
- **Endpoint:** `https://api-inference.huggingface.co/models/gpt2`
- **Funcionalidad:** Genera texto basado en una entrada inicial.
- **Entrada:** Cadena de texto en inglés.
- **Salida:** Cadena de texto generada.

### 2. **Helsinki-NLP/opus-mt-en-fr (Translation EN to FR)**
- **Endpoint:** `https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-fr`
- **Funcionalidad:** Traduce texto del inglés al francés.
- **Entrada:** Cadena de texto en inglés.
- **Salida:** Cadena de texto traducida al francés.

### 3. **BART-Large-CNN (Summarization)**
- **Endpoint:** `https://api-inference.huggingface.co/models/facebook/bart-large-cnn`
- **Funcionalidad:** Resume textos extensos en una versión más corta.
- **Entrada:** Cadena de texto.
- **Salida:** Cadena de texto resumida.

### 4. **DistilBERT (Sentiment Analysis)**
- **Endpoint:** `https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english`
- **Funcionalidad:** Analiza el sentimiento de un texto.
- **Entrada:** Cadena de texto.
- **Salida:** Etiqueta de sentimiento ("positive" o "negative") y puntuación asociada.

---

## Flujo del Proyecto

### Diagrama

```plaintext
[ Input Data ("The weather today is amazing!") ]
            ↓
[ GPT-2 (Generación de Texto) ]
            ↓
[ Helsinki-NLP (Traducción EN → FR) ]
            ↓
[ BART-Large-CNN (Resumen) ]
            ↓
[ DistilBERT (Análisis de Sentimiento) ]
            ↓
[ Output (Sentimiento: Positivo) ]
```

---

## Implementación

### Clase `ModelPipeline`
La clase `ModelPipeline` se encarga de gestionar la interacción con los modelos. Sus principales funcionalidades son:

- **Registrar modelos:** Permite asociar un nombre de modelo con su endpoint en la API.
- **Procesar un modelo:** Envía datos a un modelo y devuelve su salida, manejando errores y reintentos si es necesario.
- **Iterar entre modelos:** Permite pasar la salida de un modelo como entrada para el siguiente en una secuencia predefinida.

#### Métodos Principales

1. `add_model(model_name: str, endpoint: str)`
   - Registra un modelo con su nombre y endpoint asociado.

2. `process(model_name: str, inputs)`
   - Envía una entrada al modelo especificado y devuelve la salida generada.

3. `iterate_models(model_sequence: list, initial_input: str)`
   - Itera a través de una secuencia de modelos, procesando la entrada inicial y transformándola en cada paso.

### Ejemplo de Uso

#### Código Principal
```python
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"

    pipeline = ModelPipeline(api_key)

    # Registrar modelos
    pipeline.add_model("text_generation", "https://api-inference.huggingface.co/models/gpt2")
    pipeline.add_model("translation_en_to_fr", "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-fr")
    pipeline.add_model("summarization", "https://api-inference.huggingface.co/models/facebook/bart-large-cnn")
    pipeline.add_model("sentiment_analysis", "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english")

    # Entrada inicial
    input_data = "The weather today is amazing!"

    # Ejecutar secuencia de modelos
    output = pipeline.iterate_models([
        "text_generation",
        "translation_en_to_fr",
        "summarization",
        "sentiment_analysis"
    ], input_data)

    print("Final Output:", output)
```

#### Ejemplo de Salida
- Entrada inicial: `"The weather today is amazing!"`
- Salida final:  
  ```json
  {
      "label": "positive",
      "score": 0.99
  }
  ```

---

## Requisitos

### Dependencias
- **Python 3.8+**
- **Bibliotecas:**
  - `requests`

### Ejecución
Ejecuta el script principal:
```bash
python main.py
```

---

## Notas
- **Autorización:** Asegúrate de proporcionar una API Key válida de Hugging Face en el código.
- **Errores temporales:** El sistema maneja errores 503 con reintentos automáticos.
- **Flexibilidad:** Puedes añadir más modelos o modificar la secuencia según sea necesario.
