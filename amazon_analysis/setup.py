from pathlib import Path

# Define project structure
project_dir = Path("amazon_analysis")
data_dir = project_dir / "data"
raw_data_dir = data_dir / "raw_data"
processed_data_dir = data_dir / "processed_data"
notebooks_dir = project_dir / "notebooks"
src_dir = project_dir / "src"
models_dir = src_dir / "models"
tableau_dir = project_dir / "tableau"

# Create directories
directories = [
    project_dir,
    data_dir,
    raw_data_dir,
    processed_data_dir,
    notebooks_dir,
    src_dir,
    models_dir,
    tableau_dir
]

for directory in directories:
    directory.mkdir(parents=True, exist_ok=True)

# Create empty files
(Path(project_dir) / "requirements.txt").touch()
(Path(project_dir) / "README.md").touch()
(Path(project_dir) / ".gitignore").touch()
(Path(notebooks_dir) / "data_ingestion.ipynb").touch()
(Path(notebooks_dir) / "etl_pipeline.ipynb").touch()
(Path(src_dir) / "config.py").touch()
(Path(src_dir) / "data_ingestion.py").touch()
(Path(src_dir) / "etl_pipeline.py").touch()
(Path(src_dir) / "analysis.py").touch()

# Print structure to verify
for directory in directories:
    print(f"Created directory: {directory}")
