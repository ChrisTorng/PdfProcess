from pdf2image import convert_from_path

# 將 PDF 第一頁轉換為影像，不設定 dpi 以使用預設值
pdf_path = "114ListenExam.pdf"
image = convert_from_path(pdf_path, first_page=1, last_page=1)[0]

# 打印影像尺寸 (像素)
width, height = image.size
print(f"影像寬度: {width} 像素, 高度: {height} 像素")

# 若知道 PDF 的物理尺寸（例如寬度和高度以英吋為單位），可以估算 DPI
# 常見的 PDF 尺寸，例如 A4 大小為 8.27 x 11.69 英吋
# pdf_width_inch = 8.27  # A4 寬度英吋
# pdf_height_inch = 11.69  # A4 高度英吋
pdf_width_inch =  11.69 # A4 橫印寬度英吋
pdf_height_inch = 8.27  # A4 橫印高度英吋

# 計算 DPI
dpi_width = width / pdf_width_inch
dpi_height = height / pdf_height_inch

print(f"估計 DPI (寬度): {dpi_width}, DPI (高度): {dpi_height}")
