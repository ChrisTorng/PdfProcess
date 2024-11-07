import fitz  # PyMuPDF
from pdf2image import convert_from_path
from PIL import Image, ImageDraw, ImageFont

# 設置更高的 DPI
dpi_value = 200  # 可根據需要調整，300-400dpi 提供較高解析度，實測 200 dpi 已與原稿相當

# 原始裁切範圍（基於 200 DPI），原始寫法為 (0, 150, 830, 500)
# 設定 200 dpi 後為 (0, 400, 2300, 1400)
# (left, upper, right, lower)
base_dpi = 200
base_crop_box = (0, 350, 2300, 1400)

# 根據 DPI 動態調整裁切範圍
scale_factor = dpi_value / base_dpi
crop_box = tuple(int(x * scale_factor) for x in base_crop_box)

# 載入 PDF 檔案
pdf_path = "114ListenExam.pdf"
output_path = "114ListenExamCombined.pdf"
doc = fitz.open(pdf_path)
total_pages = doc.page_count
#total_pages = 3 # for short testing

# 處理每三頁一組，移除浮水印與合併
pages = []
for page_num in range(total_pages):
    print(page_num)
    # # 每頁轉成圖像
    # page = doc.load_page(page_num)
    # pix = page.get_pixmap()
    # # 將該頁儲存成圖像格式
    # img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # 使用 convert_from_path 直接獲取高解析度的圖像
    # Need to install poppler
    images = convert_from_path(pdf_path, dpi=dpi_value, first_page=page_num + 1, last_page=page_num + 1)
    img = images[0]

    # 去除浮水印（這裡假設浮水印位於特定區域，可以用影像處理方法如裁剪或遮蓋）
    img = img.crop(crop_box)  # 假設浮水印位於固定位置

        # 加上頁碼
    draw = ImageDraw.Draw(img)
    
    # 設定字型和大小（可以使用預設字型）
    try:
        font = ImageFont.truetype("arial.ttf", 80)  # 替換為你的字型，或使用 PIL 預設字型
    except IOError:
        font = ImageFont.load_default()
    
    # 頁碼文字
    page_text = f"P. {page_num + 1}"
    
    x_position = 50  # 左邊距離邊緣像素
    y_position = 50  # 上部距離邊緣像素
    
    # 繪製頁碼
    draw.text((x_position, y_position), page_text, font=font, fill="black")

    pages.append(img)

# 將每三頁合併為一頁
combined_pages = []
for i in range(0, total_pages, 3):
    print(i)
    imgs_to_merge = pages[i:i+3]
    widths, heights = zip(*(img.size for img in imgs_to_merge))
    max_width = max(widths)
    total_height = sum(heights)
    
    # 創建新畫布
    combined_img = Image.new("RGB", (max_width, total_height))
    
    # 將三頁影像依序拼接到新畫布上
    y_offset = 0
    for img in imgs_to_merge:
        combined_img.paste(img, (0, y_offset))
        y_offset += img.height

    combined_pages.append(combined_img)

# 將合併的圖像頁面轉存成 PDF
combined_pages[0].save(output_path, save_all=True, append_images=combined_pages[1:])

print(f"合併處理完成，結果儲存於 {output_path}")
