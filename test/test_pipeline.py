import os
import pytest

@pytest.fixture(autouse=True)
def setup_test_environment():
    """Testdən əvvəl data qovluğunu və saxta faylı yaradır, test bitəndə silir."""
    # Data qovluqlarını yaradırıq
    os.makedirs("data/raw", exist_ok=True)
    
    # Keçici bir saxta churn.csv faylı yaradırıq
    with open("data/raw/churn.csv", "w") as f:
        f.write("customer_id,churn\n1,0\n2,1")
        
    # Həmçinin DVC faylını simulyasiya edirik
    with open("data/raw/churn.csv.dvc", "w") as f:
        f.write("outs:\n- md5: mock_hash\n  path: churn.csv")

def test_raw_data_exists():
    assert os.path.exists("data/raw/churn.csv"), "Raw data faylı tapılmadı!"

def test_dvc_tracker():
    assert os.path.exists("data/raw/churn.csv.dvc"), "DVC faylı izləmir!"