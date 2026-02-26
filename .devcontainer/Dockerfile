# https://github.com/devcontainers/images/tree/main/src/python
FROM mcr.microsoft.com/devcontainers/python:3.13@sha256:cc1d6663fe31263b15a0ed5d89170d63900986c4b92ecbf25a0286082087da96
# Set up X11 and OpenGL libraries
RUN apt-get update && apt-get --no-install-recommends install -y \
    # OpenGL / EGL
    x11-apps \
    libgl1 \
    libglx-mesa0 \
    libegl1 \
    \
    # X11 Core
    libx11-6 \
    libx11-xcb1 \
    libxkbcommon0 \
    libxkbcommon-x11-0 \
    \
    # XCB
    libxcb1 \
    libxcb-cursor0 \
    libxcb-icccm4 \
    libxcb-keysyms1 \
    libxcb-render-util0 \
    libxcursor1 \
    libxcb-shape0 \
    libxcb-xfixes0 \
    \
    # Fonts / DBUS
    libfontconfig1 \
    libfreetype6 \
    libdbus-1-3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
