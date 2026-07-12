# tests/test_pipeline.py
import os

def test_raw_data_exists():
    assert os.path.exists("data/raw/churn.csv"), "Raw data faylı tapılmadı!"

def test_dvc_tracker():
    assert os.path.exists("data/raw/churn.csv.dvc"), "DVC faylı izləmir!"