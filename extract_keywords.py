#coding: utf-8

input_file = "A-TIG keywords.txt"
output_file = "keywords_clean.txt"  

def extract_keywords(input_file, output_file):
    with open(input_file, encoding='utf-8') as fin, open(output_file, "w", encoding='utf-8') as fout:
        current_keywords = []
        for line in fin:
            line = line.strip()
            if line.startswith("DE "):
                keywords = line[3:]
                current_keywords.append(keywords)
                continue
            if line.startswith("ID "):
                keywords = line[3:]
                current_keywords.append(keywords)
                continue
            if (line.startswith("   ") or line.startswith("\t")) and current_keywords:
                current_keywords[-1] += " " + line.strip()
                continue
            if line == "ER":
                if current_keywords:
                    joined = "; ".join([kw.strip(" ;") for kw in current_keywords if kw.strip()])
                    if joined:
                        fout.write(joined + "\n")
                    current_keywords = []
        if current_keywords:
            joined = "; ".join([kw.strip(" ;") for kw in current_keywords if kw.strip()])
            if joined:
                fout.write(joined + "\n")

if __name__ == "__main__":
    extract_keywords(input_file, output_file)
    print("Zrobione! Słowa kluczowe zapisane w", output_file) 