# Text-to-Video Generation using Allegro and Stable Diffusion
![Generated Video Preview](generated_video.mp4)

## Overview
This project generates a video from user-provided text prompts using Allegro for text generation and Stable Diffusion for image generation. The images are then compiled into a video.

## Example Video
<video src="https://user-images.githubusercontent.com/ndeekshith/Text2Video/raw/main/Text2Video/generated_video.mp4" controls="controls" style="max-width: 730px;">
</video>
## Installation
To run this project, install the necessary dependencies:
```sh
pip install transformers torch moviepy diffusers accelerate
```

## Usage
1. **Run the script** and enter your text prompt when prompted.
2. **Generated text** will be created using Allegro.
3. **Stable Diffusion** will generate images based on the text.
4. **A video** will be created from the generated images.
5. **The final video** will be saved as `generated_video.mp4`.

## Code Workflow
1. **Text Generation**: Allegro generates a descriptive text from user input.
2. **Image Generation**: Stable Diffusion creates multiple frames based on the text.
3. **Video Creation**: MoviePy converts images into a video.

## Output
- Generated text based on the input.
- A series of images representing frames of a video.
- A final video file (`generated_video.mp4`).

## Notes
- Ensure you have a GPU available for faster processing.
- The video frame rate can be adjusted in the script.

Enjoy creating AI-generated videos! 🚀

