import pdftotext
from fpdf import FPDF
import os
import sys
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=argparse.FileType('r'),
                        help='provide path to pdf')
    args = parser.parse_args()
    return args


def load_pdf(fname):
    with open(fname, "rb") as fhand:
        pdf = pdftotext.PDF(fhand)
    text = "\n\n".join(pdf)
    return text


def write_to_txt(fname, text):
    with open(fname, 'w') as fhand:
        fhand.writelines(text)


def write_to_pdf(base_name):
    pdf = FPDF(format="A4")
    pdf.add_page()
    pdf.add_font('LiuJianMaoCao', '', os.path.join("fonts", "LiuJianMaoCao.ttf"), uni=True)
    pdf.set_font("LiuJianMaoCao", size=15)
    pdf.set_text_color(1, 16, 85)  # set text color to blue
    with open(base_name + ".txt", "r", encoding="utf-8", errors="ignore") as fhand:
        for x in fhand:
            pdf.cell(100, 7, txt=x, ln=1, align='L')

    # write to a pdf file
    pdf.output(base_name + "_handwritten.pdf")


def clean_up(base_name):
    os.remove(base_name + '.txt')


if __name__ == "__main__":
    args = parse_arguments()
    flag = False
    with args.filename as fhand:
        if fhand.name.endswith('.pdf'):
            base_name = fhand.name.split('.')[0]
            flag = True
        else:
            print("File must have an extension .pdf")
            sys.exit()

    if flag:
        # Load your PDF
        text = load_pdf(base_name + ".pdf")

        # write to txt
        write_to_txt(base_name + ".txt", text)

        # write to pdf
        write_to_pdf(base_name)

        # clean up
        clean_up(base_name)
