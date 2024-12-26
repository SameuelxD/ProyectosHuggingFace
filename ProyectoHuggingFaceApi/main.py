from transformers import DetrImageProcessor, DetrForObjectDetection
from PIL import Image, ImageDraw, ImageFont
import torch
import matplotlib.pyplot as plt

# Cargar el procesador y el modelo DETR de Hugging Face
processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-101")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-101")

# Función para procesar y detectar objetos
def detect_objects(image_path, confidence_threshold=0.7):
    # Cargar imagen
    image = Image.open(image_path).convert("RGB")
    
    # Preprocesar la imagen
    inputs = processor(images=image, return_tensors="pt")
    
    # Realizar detección con el modelo
    outputs = model(**inputs)
    
    # Obtener resultados de detección
    target_sizes = torch.tensor([image.size[::-1]])  # (alto, ancho)
    results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=confidence_threshold)[0]
    
    # Preparar imagen para dibujar resultados
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    
    detected_objects = []
    
    # Dibujar resultados
    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        score = round(score.item(), 2)
        label_id = label.item()
        label_name = model.config.id2label[label_id]
        box = [round(i, 2) for i in box.tolist()]  # Coordenadas de la caja

        # Solo considerar detecciones con confianza suficiente
        if score >= confidence_threshold:
            detected_objects.append({"label": label_name, "score": score, "box": box})
            
            
            draw.rectangle(box, outline="red", width=3)
            text = f"{label_name} ({score})"
            
            
            text_bbox = draw.textbbox((0, 0), text, font=font)
            text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
            text_position = (box[0], box[1] - text_height if box[1] - text_height > 0 else box[1])
            
            draw.rectangle([text_position, (text_position[0] + text_width, text_position[1] + text_height)], fill="red")
            draw.text(text_position, text, fill="white", font=font)

    return image, detected_objects

# Ruta de la imagen
image_path = "images/city1.jpg"  

# Detectar objetos
image_with_detections, detected_objects = detect_objects(image_path, confidence_threshold=0.7)

# Mostrar resultados gráficos
plt.imshow(image_with_detections)
plt.axis("off")
plt.show()

# Imprimir objetos detectados
print("\nObjetos detectados:")
for obj in detected_objects:
    print(f"- {obj['label']} (Confianza: {obj['score']}) en Caja: {obj['box']}")
