import torch
from diffusers import StableDiffusionPipeline

def main():
    model_id = "runwayml/stable-diffusion-v1-5"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32
    print(f"Using device: {device}")
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=dtype
    )
    pipe = pipe.to(device)
    prompt = """
    Ultra realistic floral wallpaper, tightly packed flowers,
    white daisies with yellow centers,
    peach roses, blush pink roses,
    golden yellow flowers,
    small lavender flowers,
    soft pastel color palette,
    macro photography,
    high detail,
    8k resolution
    """
    negative_prompt = "dark, blurry, low quality, distorted"

    image = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        height=512,
        width=1024,
        num_inference_steps=30,
        guidance_scale=8
    ).images[0]
    output_path = "generated_flower_wallpaper.png"
    image.save(output_path)
    print(f"Image saved as {output_path}")
if __name__ == "__main__":
    main()
