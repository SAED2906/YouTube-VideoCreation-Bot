@echo off
color b
cls

for /l %%x in (1, 1, 5) do (
    color b
    python main.py
)