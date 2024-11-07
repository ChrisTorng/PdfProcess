# PdfProcess

## 114 Listen Exam

- `pip install PyMuPDF pdf2image pillow`
- Download [Releases - oschwartz10612/poppler-windows](https://github.com/oschwartz10612/poppler-windows/releases/)
- Unzip, add PATH to the unzipped `poppler-24.08.0\Library\bin` path
- Update `114ListenExam.py`:
```py
output_path = "114ListenExamCombined.pdf"
total_pages = doc.page_count
total_pages = 3 # for short testing
```
- `python 114ListenExam.py`

## get_dpi.py

- `python get_dpi.py` to get pdf image dpi setting