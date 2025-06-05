import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import os

st.set_page_config(page_title="Neon Image Generator", layout="centered")
st.title("Neon Image Generator with Stable Diffusion")

prompt = st.text_input("Enter your prompt", "A biker in a neon city, 4k, highly detailed")

if "pipe" not in st.session_state:
    with st.spinner("Loading model (first time only)..."):
        st.session_state.pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16
        ).to("cuda")

if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        image = st.session_state.pipe(prompt).images[0]
        os.makedirs("sample_outputs", exist_ok=True)
        filename = f"sample_outputs/{prompt.replace(' ', '_')[:50]}.png"
        image.save(filename)

        st.image(image, caption="Generated Image", use_container_width=True)
        with open(filename, "rb") as file:
            st.download_button("Download Image", file, file_name=os.path.basename(filename), mime="image/png")
