import ebooklib, os, re
from ebooklib import epub
from bs4 import BeautifulSoup

epub_path = r"E:\Users\zht19\Downloads\学会如何学习：120堂认知升级课.epub"
out_path = r"E:\Vibe Coding\coding\WorkBuddy_workspace\学会如何学习-skills-repo\.darwin\book_full.txt"

book = epub.read_epub(epub_path)
chunks = []
for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
    soup = BeautifulSoup(item.get_content(), "html.parser")
    text = soup.get_text(separator="\n")
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    if text:
        chunks.append(text)

full = "\n\n".join(chunks)
with open(out_path, "w", encoding="utf-8") as f:
    f.write(full)

lines = full.split("\n")
print(f"提取完成: {len(full)} 字符, {len(lines)} 行")
print(f"保存到: {out_path}")
