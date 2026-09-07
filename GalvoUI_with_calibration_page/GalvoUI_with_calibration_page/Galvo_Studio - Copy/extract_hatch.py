import PyPDF2

pdf_path = r'd:\TeamDev\DLL_Galvo\Galvo_Scribing\Galvo_Studio - Copy\Galvo_info\Ezcad2.14.9_EN_Manual.pdf'
with open(pdf_path, 'rb') as f:
    reader = PyPDF2.PdfReader(f)
    text = ""
    for i in range(len(reader.pages)):
        page_text = reader.pages[i].extract_text()
        if page_text and 'Hatch' in page_text:
            text += f'\n--- Page {i+1} ---\n'
            text += page_text

with open('hatch_info.txt', 'w', encoding='utf-8') as f:
    f.write(text)
print("Extraction complete.")
