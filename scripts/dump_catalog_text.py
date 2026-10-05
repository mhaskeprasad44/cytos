import pypdf

files = ['cytos_newcatalog2026_with BG.pdf', 'cytos_newprofile1 2026.pdf']

with open('catalog_extracted_data.txt', 'w', encoding='utf-8') as out:
    for fname in files:
        out.write(f"\n{'='*60}\nFILE: {fname}\n{'='*60}\n")
        try:
            reader = pypdf.PdfReader(fname)
            out.write(f"Total Pages: {len(reader.pages)}\n")
            for i, p in enumerate(reader.pages):
                out.write(f"\n--- PAGE {i+1} ---\n")
                text = p.extract_text()
                if text:
                    out.write(text.strip() + "\n")
                else:
                    out.write("[EMPTY / IMAGE-ONLY]\n")
        except Exception as e:
            out.write(f"Error reading {fname}: {e}\n")

print("Finished extracting catalog data.")
