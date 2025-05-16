# Conv TasNet

This repository is based on [JusperLee's repository](https://github.com/JusperLee/Conv-TasNet).
```
# Running train.py immediately on cloud environment with MUSAN-MAESTRO-v2000-500-500
git clone --branch relative_process --single-branch https://github.com/jbnu-capstone/conv-tasnet-pytorch
pip install pyyaml torchaudio tqdm soundfile
cd conv-tasnet-pytorch; python prepare_data.py; train.py;
```

---

## 0. Requirements
- using conda/miniforge/mamba:
    ```
    conda create --name ctnp
    conda activate ctnp
    conda install pyyaml torchaudio tqdm soundfile matplotlib -y
    ```
- using pip:
    ```
    pip install pyyaml torchaudio tqdm soundfile matplotlib
    ```

---

## 1. Prepare dataset and codes

- `prepare_data.py` downloads MUSAN-MAESTRO dataset from [google drive](https://drive.google.com/file/d/1Sm6fu8vXzRk6PrwFfYEvXGFpKMNPXPzv/), and create scp running `create_scp`.

```
python prepare_data.py
```
   
---

## 2. Run code
The following command will train a model using scp files located in "./dataset/create_scp", which is specified in **train.yml** file.
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
