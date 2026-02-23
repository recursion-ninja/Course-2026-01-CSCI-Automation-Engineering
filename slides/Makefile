MD_FILES := $(wildcard *.md)
PDF_FILES := $(MD_FILES:.md=.pdf)

.PHONY: all clean

all: $(PDF_FILES)

%.pdf: %.md
	pandoc --from=gfm --pdf-engine=xelatex -t beamer $< -o $@

clean:
	rm -f $(PDF_FILES)
