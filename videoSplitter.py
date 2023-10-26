import os
from moviepy.editor import VideoFileClip


def split_video(input_file, output_dir, interval):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    video = VideoFileClip(input_file)
    video_duration = int(video.duration)
    aspect_ratio = 9 / 16

    for i in range(0, video_duration, interval):
        start = i
        end = i + \
            interval if (i + interval) <= video_duration else video_duration
        output_file = os.path.join(
            output_dir, f"ShortTemplate_{i // interval + 1+41}.mp4")
        print(f"Processing part {i // interval + 1}: {start}s to {end}s")
        subclip = video.subclip(start, end)

        # Crop the subclip to 9:16 aspect ratio
        width, height = subclip.size
        new_width = int(height * aspect_ratio)
        crop_width = (width - new_width) // 2
        cropped_subclip = subclip.crop(x1=crop_width, x2=width-crop_width)

        cropped_subclip.write_videofile(
            output_file, codec='libx264', audio_codec='aac')


input_file = "main3.mp4"
output_dir = "input"
interval = 58

split_video(input_file, output_dir, interval)
