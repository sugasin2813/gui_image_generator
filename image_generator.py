import base64
import cv2
import numpy as np
from diffusers import DiffusionPipeline

class ImageGenerator:
    def __init__(self, model_name="gsdf/Counterfeit-V2.5", device="mps"):
        self.pipe = DiffusionPipeline.from_pretrained(model_name)
        self.pipe = self.pipe.to(device)
        self.pipe.enable_attention_slicing()

    def generate(self, prompt: str, size=(256, 256)) -> str:
        image = self.pipe(prompt).images[0]
        image = np.array(image, dtype=np.uint8)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image = cv2.resize(image, size)
        _, image_encoded = cv2.imencode('.png', image)
        return base64.b64encode(image_encoded).decode('utf-8')