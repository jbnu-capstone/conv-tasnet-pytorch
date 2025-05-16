# Conv TasNet

This repository is based on [JusperLee's repository](https://github.com/JusperLee/Conv-TasNet).

---

## 0. Requirements
- using conda/miniforge/mamba:
    ```
    conda install yaml torchaudio tqdm -y
    ```
- using pip:
    ```
    pip install yaml torchaudio tqdm -y
    ```

---

## 1. Prepare dataset and codes
- Dataset must be located in the exact directory: **'/Users/data/musanmaestro'**. If not, many parts of code will need to be modified to match your dataset path.
    ```
    git clone https://github.com/jbnu-capstone/musanmaestro.git /Users/data/musanmaestro
    git clone https://github.com/jbnu-capstone/conv-tasnet-pytorch
    cd conv-tasnet-pytorch
    ```
   
---

## 2. Run code
The following command will train a model using scp files located in "/Users/data/musanmaestro/create_scp", which is specified in **train.yml** file.
```
python train.py
```

---

## 3. Inference
The following command will separate **"train.wav"** file located in the working directory into 2 stems: piano and others. You can specify the name or directory of the target file or model. 
```
python Separation_wav.py -mix_wav train.wav -model ./models/best.pt
```
- other options: `-gpuid`, `-yaml`, `-save_path`