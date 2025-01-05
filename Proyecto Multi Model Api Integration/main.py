import requests
import time


class ModelPipeline:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.models = {}
        self.headers = {"Authorization": f"Bearer {api_key}"}

    def add_model(self, model_name: str, endpoint: str):
        self.models[model_name] = endpoint

    def process(self, model_name: str, inputs) -> dict:
        if model_name not in self.models:
            raise ValueError(f"Model '{model_name}' not found in the pipeline.")

        endpoint = self.models[model_name]

        # Asegurarse de que los datos sean válidos para cada modelo
        if isinstance(inputs, dict):
            inputs = inputs.get("inputs", inputs.get("text", ""))

        if not isinstance(inputs, str):
            raise ValueError(f"Invalid input for model '{model_name}': {inputs}")

        payload = {
            "inputs": inputs,
            "parameters": {"truncation": "only_first"}  # Truncar el texto automáticamente
        }
        print(f"Sending request to {endpoint} with input: {payload}")

        # Reintentos en caso de error 503
        for attempt in range(5):
            response = requests.post(endpoint, headers=self.headers, json=payload)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 503:
                print(f"Model {model_name} is loading. Retrying in 5 seconds...")
                time.sleep(5)
            else:
                break

        # Lanza error si el estado no es 200
        print(f"Error {response.status_code}: {response.text}")
        response.raise_for_status()


    def iterate_models(self, model_sequence: list, initial_input: str) -> dict:
        current_input = initial_input

        for model_name in model_sequence:
            # Convertir salida previa en formato adecuado para el próximo modelo
            if isinstance(current_input, list) and current_input and isinstance(current_input[0], dict):
                if "generated_text" in current_input[0]:
                    current_input = current_input[0]["generated_text"]
                elif "translation_text" in current_input[0]:
                    current_input = current_input[0]["translation_text"]
                elif "summary_text" in current_input[0]:
                    current_input = current_input[0]["summary_text"]
                elif "label" in current_input[0]:
                    current_input = current_input[0]["label"]
            elif isinstance(current_input, dict) and "inputs" in current_input:
                current_input = current_input["inputs"]

            # Procesar la entrada con el modelo actual
            current_input = self.process(model_name, current_input)

        return current_input


if __name__ == "__main__":
    api_key = "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"

    pipeline = ModelPipeline(api_key)

    # Registrar modelos
    pipeline.add_model("text_generation", "https://api-inference.huggingface.co/models/gpt2")
    pipeline.add_model("translation_en_to_fr", "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-fr")
    pipeline.add_model("summarization", "https://api-inference.huggingface.co/models/facebook/bart-large-cnn")
    pipeline.add_model("sentiment_analysis", "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english")

    # Entrada inicial
    input_data = "The weather today is amazing!"

    # Ejecutar secuencia de modelos
    output = pipeline.iterate_models(["text_generation", "translation_en_to_fr", "summarization", "sentiment_analysis"], input_data)

    print("Final Output:", output)
