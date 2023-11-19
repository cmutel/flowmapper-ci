.PHONY: clean

OUTPUT_FILES := $(addsuffix .json,$(addprefix data/, $(basename $(notdir $(wildcard data-raw/*)))))

clean: ${OUTPUT_FILES}

data/%.json: data-raw/%.csv scripts/munge/%.py
	python scripts/munge/$*.py $< $@

data/%.json: data-raw/%.xlsx scripts/munge/%.py
	python scripts/munge/$*.py $< $@

data/%.json: data-raw/%.json scripts/munge/%.py
	python scripts/munge/$*.py $< $@

data/%.json: data-raw/%.xml scripts/munge/%.py
	python scripts/munge/$*.py $< $@
