# https://github.com/devcontainers/images/tree/main/src/python
FROM mcr.microsoft.com/devcontainers/python:3.13@sha256:9b2f0d8e2ac7c17aec218f98877ba045bb5d0c785b693bdc499fcc4d417f7b89
# Set up X11 and OpenGL libraries
RUN apt-get update && apt-get install -y x11-apps libgl1 libglx-mesa0 libegl1 libxkbcommon0 libxcb1 libxcb-cursor0 libxcb-icccm4 libxcb-keysyms1 libxcb-render-util0 libfontconfig1 libfreetype6 libdbus-1-3 libxkbcommon-x11-0 libx11-6 libx11-xcb1 libxcursor1 libxcb-shape0 libxcb-xfixes0 && rm -rf /var/lib/apt/lists/*
