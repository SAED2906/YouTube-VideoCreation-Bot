@echo off
color b
cls

for /l %%x in (1, 1, 20) do (
    color b
    python main.py
)

python youtubeUploader.py
python cleaner.py
