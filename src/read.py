from pathlib import Path

def read_texts_from_folder(folder_path):
    texts = []
    for file in Path(folder_path).glob("*.txt"):
        texts.append(file.read_text(encoding="utf-8"))
    return texts