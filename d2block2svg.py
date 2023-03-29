import logging
import os


def explore_directory(doc_folder, func):
    for file in os.listdir(doc_folder):
        path = f'{doc_folder}/{file}'
        if os.path.isfile(path):
            if file.endswith('.md'):
                func(path, file)
        elif os.path.isdir(path):
            explore_directory(path, func)


def changeD2toSVG(file: str, filename: str):
    markdown_content = ""
    with open(file) as f:
        inside_d2_block = False
        for line in f.readlines():
            if line.strip().startswith("```d2"):
                inside_d2_block = True
                markdown_content += f"![[{filename.replace('.md', '.svg')}]]\n\n"

            if not inside_d2_block:
                markdown_content += line

            if inside_d2_block and line.strip() == "```":
                inside_d2_block = False

    with open(file, "w") as f:
        f.write(markdown_content)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Change D2 block in all .md in "doc" folder
    explore_directory("doc", changeD2toSVG)

