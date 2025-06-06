import pytest
import zipfile
from pathlib import Path


@pytest.fixture(scope="session")
# собираем файлы в один архив
def zip_path():
    resources_dir = Path("resources")
    files = [
        resources_dir / "file_example_XLSX_50.xlsx",
        resources_dir / "Python Testing with Pytest (Brian Okken).pdf",
        resources_dir / "wheel-spin-report-2025-03-28 14_14_48.csv"
    ]
    zip_path = resources_dir / "test_archive.zip"
    if not zip_path.exists():
        with zipfile.ZipFile(zip_path, "w") as archive:
            for file in files:
                archive.write(file, file.name)
    return zip_path
