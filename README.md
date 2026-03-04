# Stable Diffusion Floral Generator

AI-powered text-to-image generator built using Stable Diffusion v1-5, PyTorch, and Hugging Face Diffusers.

##  Features

- Text-to-image generation
- Prompt engineering with negative prompting
- GPU acceleration (FP16 support)
- High-resolution floral wallpaper output

##  Tech Stack

- Python
- PyTorch
- Hugging Face Diffusers
- Stable Diffusion v1-5

##  Installation
Clone the repository:

```bash
git clone https://github.com/yourusername/stable-diffusion-floral-generator.git
cd stable-diffusion-floral-generator
```

Create virtual environment (recommended):

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

##  Run
```bash
python generate_flowers.py

## Output
The generated image will be saved as:
generated_flower_wallpaper.png
