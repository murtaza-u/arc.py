import pdftotext
from fpdf import FPDF
import os
import sys
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--pdf', type=argparse.FileType('r'),
                        help='provide path to pdf file')
    parser.add_argument('-t', '--text', type=argparse.FileType('r'),
                        help='provide path to text file')
    parser.add_argument('-l', '--linespacing', type=int,
                        help='spacing after each line')
    args = parser.parse_args()
    return args


def load_pdf(input_file):
    with open(input_file, "rb") as fhand:
        pdf = pdftotext.PDF(fhand)
    text = "\n\n".join(pdf)
    return text


def write_to_txt(txt_file, text):
    with open(txt_file, 'w') as fhand:
        fhand.writelines(text)


def write_to_pdf(txt_file, pdf_file, line_spacing=7):
    pdf = FPDF(format="A4")
    pdf.add_page()
    pdf.add_font('LiuJianMaoCao', '', os.path.join("fonts", "LiuJianMaoCao.ttf"), uni=True)
    pdf.set_font("LiuJianMaoCao", size=15)
    pdf.set_text_color(1, 16, 85)  # set text color to blue
    with open(txt_file, "r", encoding="utf-8", errors="ignore") as fhand:
        for x in fhand:
            pdf.cell(h=line_spacing, txt=x, ln=1, align='L')

    # write to a pdf file
    pdf.output(pdf_file)


def clean_up(*files):
    for file in files:
        os.remove(file)


if __name__ == "__main__":
    args = parse_arguments()
    flag = False

    line_spacing = args.linespacing if args.linespacing else 7
    if args.pdf:
        with args.pdf as fhand:
            if fhand.name.endswith('.pdf'):
                base_name = fhand.name.split('.')[0]
                flag = "PDF"
            else:
                print("File must have an extension .pdf")
                sys.exit()
    elif args.text:
        with args.text as fhand:
            fname = fhand.name
            base_name = fhand.name.split('.')[0]
            flag = "TEXT"

    if flag == "PDF":
        # Load PDF
        text = load_pdf(base_name + ".pdf")

        # write to txt file
        write_to_txt(base_name + ".txt", text)

        # write to pdf file
        write_to_pdf(base_name + ".txt", base_name + "_handwritten.pdf", line_spacing=line_spacing)

        # clean up
        clean_up(base_name + '.txt')
    elif flag == "TEXT":
        write_to_pdf(fname, base_name + "_handwritten.pdf")
    else:
        print("-h for help")
