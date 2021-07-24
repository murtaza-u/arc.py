# ARC
> Assignments R Cruel

![Example](./assets/example.png)

# A short tale
From the time I got into University I have been burdened with shitload of assignments. Every other day out of nowhere a new assignment pops up. You might think these assignments involve complex computer science problems and impossible math equations. No! Most of the time all I need to do is simply copy down contents of a pdf file(provided by the Professor) on to sheets of paper and send a soft copy to the respective Prof. These assignments provide no substantial growth to the student and are a mere waste of time. My solution -> arc.py

# What is arc.py
arc.py is a simple python script that takes a pdf file as an input and generates a pdf file that looks like it was hand written.

# Install
```bash
git clone https://github.com/Murtaza-Udaipurwala/arc.py
cd arc.py/
pip install -r requirements.txt
```

### OS dependencies(taken from [pdftotext](https://pypi.org/project/pdftotext/))
Debian, Ubuntu, and friends
```bash
sudo apt install build-essential libpoppler-cpp-dev pkg-config python3-dev
```

Fedora, Red Hat, and friends
```bash
sudo yum install gcc-c++ pkgconfig poppler-cpp-devel python3-devel
```

macOS
```bash
brew install pkg-config poppler python
```

Windows
Currently tested only when using conda:
Install the Microsoft Visual C++ Build Tools
Install poppler through conda:
```bash
conda install -c conda-forge poppler
```

# Usage
```bash
python arc.py <path/to/input.pdf>
```

# Example
Check [example](https://github.com/Murtaza-Udaipurwala/arc.py/tree/master/test)

# PS
> I hope my Professor doesn't find this
