from fpdf import FPDF

def txt_to_pdf(txt_file, pdf_file):
    # 创建PDF对象
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin = 15)
    pdf.set_font("Arial", size=12)

    # 打开TXT文件并读取内容
    with open(txt_file, 'r', encoding='utf-8') as file:
        for line in file:
            pdf.cell(200, 10, txt=line.encode('latin-1', 'replace').decode('latin-1'), ln=True)

    # 保存为PDF文件
    pdf.output(pdf_file)

if __name__ == "__main__":
    txt_file_path = "tt0120338.txt"  # 输入你的txt文件路径
    pdf_file_path = "tt0120338.pdf"  # 输出PDF文件的路径
    txt_to_pdf(txt_file_path, pdf_file_path)
