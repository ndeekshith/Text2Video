from moviepy.editor import VideoFileClip

video_path = "generated_video.mp4"
gif_path = "generated_video.gif"

clip = VideoFileClip(video_path)
clip = clip.resize(0.5)  # Resize to reduce file size if needed
clip.write_gif(gif_path)
