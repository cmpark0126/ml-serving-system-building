apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC
apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y python3.8 python3-pip python-is-python3

pip install torch==1.13.1 pillow

git clone https://github.com/triton-inference-server/tutorials.git
python tutorials/Quick_Deploy/PyTorch/export.py
mkdir models
mkdir models/resnet50
mkdir models/resnet50/1
mv tutorials/Quick_Deploy/PyTorch/config.pbtxt models/resnet50/config.pbtxt
mv model.pt models/resnet50/1/model.pt

tritonserver --model-repository models --allow-metrics --allow-gpu-metrics

# -------
pip install torchvision tritonclient[http]
wget  -O img1.jpg "https://www.hakaimagazine.com/wp-content/uploads/header-gulf-birds.jpg"
python tutorials/Quick_Deploy/PyTorch/client.py 

curl localhost:8002/metrics