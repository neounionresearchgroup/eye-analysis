FROM ubuntu:22.04
RUN apt update && apt upgrade -y && apt install -y vim curl wget python3 python3-pip build-essential
RUN pip install jupyterlab voila polars numpy matplotlib opencv-python pip-licensess
RUN pip uninstall -y opencv-python opencv-contrib-python && pip install --no-cache-dir opencv-python-headless
