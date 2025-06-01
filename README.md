# Conv TasNet

This repository is based on [JusperLee's repository](https://github.com/JusperLee/Conv-TasNet).

## Quick Start

runs on Linux 

```
git clone https://github.com/jbnu-capstone/conv-tasnet-pytorch
cd conv-tasnet-pytorch
conda env create -f environment.yml; conda activate ctnp

python prepare_data.py
python train.py
```

## Requirements
- python = 3.7
- tqdm
- pyyaml
- torchaudio
- soundfile
- matplotlib

---


## Inference
```
python Separation_wav.py -mix_wav train.wav -model ./models/best.pt
```
- other options: `-gpuid`, `-yaml`, `-save_path`


## Using Custom Data

Should have a structure like following:

```
data/
├── cv/
│   ├── mix/
│   ├── s1/
│   └── s2/
├── tr/
│   ├── mix/
│   ├── s1/
│   └── s2/
└── tt/
    ├── mix/
    ├── s1/
    └── s2/
```
