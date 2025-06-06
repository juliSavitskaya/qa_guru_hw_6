from pypdf import PdfReader

import zipfile
import io
import pandas as pd
import csv


def test_read_pdf_from_zip(zip_path):
    with zipfile.ZipFile(zip_path) as archive:
        pdf_bytes = archive.read('Python Testing with Pytest (Brian Okken).pdf')
        pdf_file = io.BytesIO(pdf_bytes)
        pdf_reader = PdfReader(pdf_file)
        assert len(pdf_reader.pages) == 256
        first_page_text = pdf_reader.pages[1].extract_text()
        assert "pytest" in first_page_text


def test_read_csv_from_zip(zip_path):
    with zipfile.ZipFile(zip_path) as archive:
        csv_bytes = archive.read('wheel-spin-report-2025-03-28 14_14_48.csv').decode('utf-8')
        csv_file = io.StringIO(csv_bytes)
        reader = csv.DictReader(csv_file)
        first_row = next(reader)
        expected = {
            'Wheel ID': '663281675124331944',
            'Wheel Name': 'Wheel 123',
            'Spin Received': '2025-03-28 09:56:09',
            'Spin Expiration Time': '2025-03-29 09:56:09',
            'Manager Email': 'ysavickayaa@marfa-tech.com',
            'Status': 'deleted',
            'Prizes Won': '',
            'Comments': 'test'
        }
        assert first_row == expected


def test_read_xlsx_from_zip(zip_path):
    with zipfile.ZipFile(zip_path) as archive:
        xlsx_bytes = archive.read('file_example_XLSX_50.xlsx')
        xlsx_file = io.BytesIO(xlsx_bytes)
        df = pd.read_excel(xlsx_file)
        expected_columns = [0, "First Name", "Last Name", "Gender", "Country", "Age", "Date", "Id"]
        assert list(df.columns) == expected_columns, "Столбцы не совпадают"

