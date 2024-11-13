FIGURES_YAML =

FIGURES_PYTHON = \
	figures/BR-comparison.pdf \
	figures/BR-comparison.png \
	figures/BR-corner-WET-1.pdf \
	figures/BR-corner-WET-1.png \
	figures/BR-corner-WET-2.pdf \
	figures/BR-corner-WET-2.png \
	figures/BR-corner-WET-3.pdf \
	figures/BR-corner-WET-3.png \
	figures/BR-corner-WET-4.pdf \
	figures/BR-corner-WET-4.png \
	figures/lifetime-comparison.pdf \
	figures/lifetime-comparison.png \
	figures/likelihood.pdf \
	figures/likelihood.png \
	figures/WET-1.pdf \
	figures/WET-1.png \
	figures/WET-2.pdf \
	figures/WET-2.png \
	figures/WET-3.pdf \
	figures/WET-3.png \
	figures/WET-4.pdf \
	figures/WET-4.png

TABLES = \
	tables/GOF-table-SM.tex \
	tables/GOF-table-WET.tex

.PHONY: all figures tables

all: figures tables

figures: $(FIGURES_YAML) $(FIGURES_PYTHON)

tables: $(TABLES)

figures/BR-corner-WET-1.pdf figures/BR-corner-WET-1.png figures/BR-corner-WET-2.pdf figures/BR-corner-WET-2.png figures/BR-corner-WET-3.pdf figures/BR-corner-WET-3.png figures/BR-corner-WET-4.pdf figures/BR-corner-WET-4.png: scripts/BR-corner.py
	python $<

figures/%.pdf figures/%.png: scripts/%.py
	python $<

figures/%.pdf: scripts/%.yaml
	eos-plot $< $@

figures/%.png: scripts/%.yaml
	eos-plot $< $@

tables/%.tex: scripts/%.py
	python $< > $@
