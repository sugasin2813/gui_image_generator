import flet as ft
from image_generator import ImageGenerator
from utils import get_device

def main(page: ft.Page):
    page.title = "Image Generator"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    device = get_device()
    generator = ImageGenerator(device=device)
    generated_image = ft.Image(fit=ft.ImageFit.CONTAIN, width=256, height=256, src_base64=None)
    prompt_text = ft.TextField(label="Enter your prompt")

    def generate_image(e):
        if not prompt_text.value or prompt_text.value.strip() == "":
            return
        image_base64 = generator.generate(prompt_text.value)
        generated_image.src_base64 = image_base64
        prompt_text.value = ""
        page.update()

    return_button = ft.ElevatedButton("Generate Image", on_click=generate_image)

    page.add(
        ft.Text("Welcome to the Image Generator!", size=30, weight="bold"),
        ft.Row(
            controls=[prompt_text, return_button],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        generated_image,
    )

if __name__ == "__main__":
    ft.app(target=main)