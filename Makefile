.PHONY: clean

clean: data/simapro-unknown-biosphere-all.json data/agribalyse-3.1.1-biosphere.json data/industry-2.0-biosphere.json data/simapro-unknown-biosphere.json data/ecoinvent-3.6-biosphere.json data/ecoinvent-3.7-biosphere.json data/ecoinvent-3.8-biosphere.json data/ecoinvent-3.9-biosphere.json data/ecoinvent-3.10-biosphere.json

data/simapro-unknown-biosphere-all.json: data-raw/agribalyse-3.1.1-biosphere.json data-raw/industry-2.0-biosphere.json data-raw/simapro-flows.json
	jq -s 'add' $^ > $@

data/agribalyse-3.1.1-biosphere.json: data-raw/agribalyse-3.1.1-biosphere.json
	cp $< $@

data/industry-2.0-biosphere.json: data-raw/industry-2.0-biosphere.json
	cp $< $@

data/simapro-unknown-biosphere.json: data-raw/simapro-flows.json
	cp $< $@

data/ecoinvent-%-biosphere.json: data-raw/ElementaryExchanges-%.xml scripts/ecoinvent.py
	python scripts/ecoinvent.py $< $@
