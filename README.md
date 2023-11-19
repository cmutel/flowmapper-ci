# Mappings between elementary flows

This project uses the [`flowmapper` package](https://github.com/fjuniorr/flowmapper) to generate mappings[^20231119T153832] between elementary flow lists of SimaPro 9.4 and ecoinvent 3.7. 

[^20231119T153832]: [openLCA documentation](https://www.openlca.org/wp-content/uploads/2020/06/General-openLCA-Mapping-Instructions_05182020.pdf) makes a great distinction between the meanings of related words in this context:

    > - __mapping__ – _noun_: A series of correspondences between two flows, a source flow and a target flow.
    > - __mapping__ – _verb_: The process of creating a correspondence between source and target flows.
    > - __flow conversion__ – _verb_: The process of converting one flow to another flow.

## Usage

Elementary flows lists exists in several different serialization formats but `flowmapper-ci` expects a "list of dicts" representation serialized as `json`. To convert the original flowlists stored in `data-raw/*` run:

```bash
make clean
```

Now we can run[^20231119T160504] the actual mapper specifying the source and target lists and a [mapping of field names](config/SimaProv9.4-ecoinventEFv3.7.toml):

[^20231119T160504]: After installing the dependencies from `requirements.txt`.

```bash
python main.py map data/SimaProv9.4.json \
                   data/ecoinventEFv3.7.json \
                   config/SimaProv9.4-ecoinventEFv3.7.toml \
                   --output-file SimaProv9.4-ecoinventEFv3.7.json
```

This will try all the [matching rules](https://github.com/fjuniorr/flowmapper/blob/notebooks-logic/flowmapper/match.py#L105) defined in the [`flowmapper`](https://github.com/fjuniorr/flowmapper) package and generate mappings with the format:

```python
  {
    "source": {
      "Flow UUID": "90004354-71D3-47E8-B322-300BA5A98F7B",
      "Flowable": "Actinium",
      "Context": "Raw materials"
    },
    "target": {
      "FlowUUID": "7781bd84-0ca4-5bf1-8fc5-15cdc1fb0796"
    },
    "conversionFactor": 1,
    "MemoMapper": "Resources with suffix in ground"
}
```

The objective is to have a **maintainable, transparent, and reproducible system** which can be applied to new lists as they are released.