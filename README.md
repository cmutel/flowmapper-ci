# Mappings between elementary flows

This project uses the [`flowmapper` package](https://github.com/fjuniorr/flowmapper) to generate mappings[^20231119T153832] between elementary flow lists of SimaPro 9.4 and ecoinvent 3.7. 

[^20231119T153832]: [openLCA documentation](https://www.openlca.org/wp-content/uploads/2020/06/General-openLCA-Mapping-Instructions_05182020.pdf) makes a great distinction between the meanings of related words in this context:

    > - __mapping__ – _noun_: A series of correspondences between two flows, a source flow and a target flow.
    > - __mapping__ – _verb_: The process of creating a correspondence between source and target flows.
    > - __flow conversion__ – _verb_: The process of converting one flow to another flow.

## Usage

Elementary flows lists exists in several different serialization formats but `flowmapper-ci` expects a "list of dicts" representation serialized as `json`. To convert the original flowlists stored in `data-raw/*` run[^20231119T160504]:

[^20231119T160504]: After installing the python dependencies with `python -m pip install -r requirements.txt` and [`jq`](https://jqlang.github.io/jq/).

```bash
make clean
```

Now we can run the actual mapper specifying the source and target lists and a [mapping of field names](config/SimaProv9.4-ecoinventEFv3.7.toml):

```bash
python main.py map data/simapro-flows.json \
                   data/ElementaryExchanges-3.7.json \
                   config/simapro-flows-ElementaryExchanges-3.7.toml
```

This will try all the [matching rules](https://github.com/fjuniorr/flowmapper/blob/notebooks-logic/flowmapper/match.py#L105) defined in the [`flowmapper`](https://github.com/fjuniorr/flowmapper) package and generate mappings with the format:

```python
  {
    "source": {
      "name": "1,3-Dioxolan-2-one",
      "categories": [
        "Water",
        "(unspecified)"
      ]
    },
    "target": {
      "uuid": "5b7d620e-2238-5ec9-888a-6999218b6974",
      "name": "1,3-Dioxolan-2-one",
      "context": "water/unspecified",
      "unit": "kg"
    },
    "conversionFactor": 1,
    "comment": "Identical names"
  }
```

The objective is to have a **maintainable, transparent, and reproducible system** which can be applied to new lists as they are released.

The last statistics for the matching `data/simapro-flows.json` and `data/ElementaryExchanges-3.7.json` is:

```bash
57975 unique source flows...
4329 unique target flows...
9121 mappings of 9040 unique source flows (15.59% of total).
```
