FIGURES_SATURATIONS = \
	figures/FF-saturation-0mA.pdf \
	figures/FF-saturation-0mA.png \
	figures/FF-saturation-0pV.pdf \
	figures/FF-saturation-0pV.png \
	figures/FF-saturation-1mT-long.pdf \
	figures/FF-saturation-1mT-long.png \
	figures/FF-saturation-1mT-perp.pdf \
	figures/FF-saturation-1mT-perp.png \
	figures/FF-saturation-1mV-long.pdf \
	figures/FF-saturation-1mV-long.png \
	figures/FF-saturation-1mV-perp.pdf \
	figures/FF-saturation-1mV-perp.png \
	figures/FF-saturation-1pA-long.pdf \
	figures/FF-saturation-1pA-long.png \
	figures/FF-saturation-1pA-perp.pdf \
	figures/FF-saturation-1pA-perp.png \
	figures/FF-saturation-1pT5-long.pdf \
	figures/FF-saturation-1pT5-long.png \
	figures/FF-saturation-1pT5-perp.pdf \
	figures/FF-saturation-1pT5-perp.png

FIGURES = \
	figures/CKM-comparison-Vcs-nominal.pdf \
	figures/CKM-comparison-Vcs-nominal.png \
	figures/CKM-comparison-Vcs-scale-factor.pdf \
	figures/CKM-comparison-Vcs-scale-factor.png \
	figures/CKM-comparison-Vcs-D-to-K-l-nu.pdf \
	figures/CKM-comparison-Vcs-D-to-K-l-nu.png \
	figures/CKM-comparison-Vcs-scenarios.pdf \
	figures/CKM-comparison-Vcs-scenarios.png \
	figures/FF-D-to-K-fp.pdf \
	figures/FF-D-to-K-fp.png \
	figures/FF-D-to-K-fz.pdf \
	figures/FF-D-to-K-fz.png \
	figures/FF-D-to-K-ft.pdf \
	figures/FF-D-to-K-ft.png \
	figures/PDF-D0-to-K-e-nu.pdf \
	figures/PDF-D0-to-K-e-nu.png \
	figures/PDF-Dp-to-K-e-nu.pdf \
	figures/PDF-Dp-to-K-e-nu.png \
	figures/PDF-D0-to-K-mu-nu.pdf \
	figures/PDF-D0-to-K-mu-nu.png \
	$(FIGURES_SATURATIONS) \
	figures/WET-all.pdf \
	figures/WET-all.png \
	figures/WET-all-rescaled.pdf \
	figures/WET-all-rescaled.png

TABLES = \
	tables/GOF-table.tex \
	tables/CKM-table.tex

PREDICTIONS = \
	data/TH-all/pred-PDF-D0-to-K-e-nu/description.yaml \
	data/TH-all/pred-PDF-Dp-to-K-e-nu/description.yaml \
	data/TH-all/pred-PDF-D0-to-K-mu-nu/description.yaml

.PHONY: all figures predictions

all: predictions figures tables

figures: $(FIGURES)

tables: $(TABLES)

predictions: $(PREDICTIONS)

figures/%.pdf: scripts/%.yaml
	eos-plot $< $@

figures/%.png: scripts/%.yaml
	eos-plot $< $@

figures/WET-all.pdf figures/WET-all.png: scripts/WET-all.py
	python3 $<

figures/WET-all-rescaled.pdf figures/WET-all-rescaled.png: scripts/WET-all-rescaled.py
	python3 $<

$(FIGURES_SATURATIONS): scripts/FF-saturations.py
	python3 $<

tables/%.tex: scripts/%.py
	python $< > $@