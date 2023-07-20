# goblin-lab

## How to Start Dev

make sure you have python installed

`python -m venv myvenv`

```
python -m venv myvenv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

OR use conda (Either Miniconda or Anaconda would work)
`conda create --name goblin -c conda-forge python=3.11`

```
conda activate goblin
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```


## How to Test

```
# pytest is easy, but not required
python -m install pytest
pytest test
```
