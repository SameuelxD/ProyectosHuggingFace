from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel

# Crear instancia de FastAPI
app = FastAPI()

# Inicializar el pipeline de question-answering usando un modelo más grande
qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad", framework="pt")

# Modelo para la solicitud
class QuestionAnswerRequest(BaseModel):
    question: str
    context: str

# Ruta raíz para verificar que el API está corriendo
@app.get("/")
async def root():
    return {"message": "API de Respuesta a Preguntas está en ejecución"}

# Endpoint para procesar preguntas
@app.post("/ask")
async def ask_question(request: QuestionAnswerRequest):
    try:
        # Obtener respuesta del modelo
        result = qa_pipeline(question=request.question, context=request.context)
        return {"answer": result["answer"], "score": result["score"]}
    except Exception as e:
        return {"error": str(e)}

# Si deseas ejecutar el servidor localmente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
