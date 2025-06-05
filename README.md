# Stable Diffusion Image Generator

A simple web app to generate stunning AI images from text prompts using **Stable Diffusion** and the **Diffusers** library by Hugging Face. This project uses **Streamlit** as the UI framework for quick prototyping and demo.

---

## Features

- Generate high-quality AI images from any text prompt
- Uses the popular `runwayml/stable-diffusion-v1-5` pre-trained model
- Simple and clean UI with Streamlit
- Save generated images locally

---

## Demo

![Demo Screenshot](/sample_outputs/A_futuristic_samurai_standing_on_a_skyscraper_roof.png)  





![Demo Screenshot](/sample_outputs/cool_output.png)  

---

## Getting Started

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/installation/)

### Installation

### 1. Clone the repo  
   
   git clone https://github.com/zeesh8x/ai-image-generator.git
   cd ai-image-generator

### 2. Create and activate a virtual environment (optional but recommended)

  python -m venv venv
  source venv/bin/activate  # Linux/macOS
  venv\Scripts\activate     # Windows

### 3. Install dependencies

   pip install -r requirements.txt

### 4. Run the app locally
  streamlit run app.py


#### NOTES:
GPU is highly recommended for faster image generation.

Running on CPU will work but will be very slow.

The model and pipeline are loaded from Hugging Face Hub.
