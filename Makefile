FIGURES_YAML = \
	figures/FF-fp2-I1-all.pdf \
	figures/FF-fp2-I1-all.png \
	figures/FF-arg-fp-I1-timelike.pdf \
	figures/FF-arg-fp-I1-timelike.png

FIGURES_PYTHON = \
	figures/rho-mass-width.pdf \
	figures/rho-mass-width.png \
	figures/FF-arg-fp-I1-timelike-with-data.pdf \
	figures/FF-arg-fp-I1-timelike-with-data.png

TABLES = \
	tables/fit-diagnostics.tex

.PHONY: all figures tables

all: figures tables

figures: $(FIGURES_YAML) $(FIGURES_PYTHON)

tables: $(TABLES)

figures/rho-mass-width.pdf figures/rho-mass-width.png: scripts/rho-mass-width.py
	python $<

figures/FF-arg-fp-I1-timelike-with-data.pdf figures/FF-arg-fp-I1-timelike-with-data.png: scripts/FF-arg-fp-I1-timelike-with-data.py
	python $<

figures/%.pdf: scripts/%.yaml
	eos-plot $< $@

figures/%.png: scripts/%.yaml
	eos-plot $< $@

tables/%.tex: scripts/%.py
	python $< > $@
