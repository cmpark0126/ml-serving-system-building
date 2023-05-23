# TODO: need to update to latest version
FROM nvcr.io/nvidia/tritonserver:22.04-py3

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3.8 python3-pip python-is-python3

RUN pip install --upgrade pip
RUN pip install torch==1.13.1 pillow

# prepare model repository

CMD ["tritonserver", "--model-repository", "models", "--allow-metrics", "true", "--allow-gpu-metrics", "true" ]