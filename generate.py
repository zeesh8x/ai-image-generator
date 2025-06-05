# generate.py

from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import os

class ImageGenerator:
    def __init__(self, model_name="runwayml/stable-diffusion-v1-5", use_cuda=True):
        self.device = "cuda" if torch.cuda.is_available() and use_cuda else "cpu"
        self.pipe = StableDiffusionPipeline.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
        ).to(self.device)

    def generate_image(self, prompt: str, save_path: str = None) -> Image.Image:
        print(f"Generating image for prompt: {prompt}")
        image = self.pipe(prompt).images[0]

        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            image.save(save_path)
            print(f"Image saved to {save_path}")

        return image
