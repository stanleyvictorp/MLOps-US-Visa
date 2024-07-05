import os
from pathlib import Path

project = "us_visa"

folders = [
    f"{project}/__init__.py",
    f"{project}/components/__init__.py",
    f"{project}/components/data_ingestion.py",
    f"{project}/components/data_validation.py",
    f"{project}/components/data_transformation.py",
    f"{project}/components/model_trainer.py",
    f"{project}/components/model_evaluation.py",
    f"{project}/components/model_pusher.py",
    f"{project}/configuration/__init__.py",
    f"{project}/constant/__init__.py",
    f"{project}/entity/__init__.py",
    f"{project}/entity/config_entity.py",
    f"{project}/entity/artifact_entity.py",
    f"{project}/exception/__init__.py",
    f"{project}/logger/__init__.py",
    f"{project}/pipeline/__init__.py",
    f"{project}/pipeline/training_pipeline.py",
    f"{project}/pipeline/prediction_pipeline.py",
    f"{project}/utils/__init__.py",
    f"{project}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml"
]

for filepath in folders:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"File already present:{filepath}" )
