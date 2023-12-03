# Mappings between elementary flows

This project uses the [`flowmapper` package](https://github.com/fjuniorr/flowmapper) to generate mappings[^20231119T153832] between elementary flow lists of SimaPro 9.4 and ecoinvent 3.7. 

[^20231119T153832]: [openLCA documentation](https://www.openlca.org/wp-content/uploads/2020/06/General-openLCA-Mapping-Instructions_05182020.pdf) makes a great distinction between the meanings of related words in this context:

    > - __mapping__ – _noun_: A series of correspondences between two flows, a source flow and a target flow.
    > - __mapping__ – _verb_: The process of creating a correspondence between source and target flows.
    > - __flow conversion__ – _verb_: The process of converting one flow to another flow.

## Usage

Elementary flows lists exists in several different serialization formats but `flowmapper` expects a "list of dicts" representation serialized as `json`. To convert the original flowlists stored in `data-raw/*` run[^20231119T160504]:

[^20231119T160504]: After installing the python dependencies with `python -m pip install -r requirements.txt` and [`jq`](https://jqlang.github.io/jq/).

```bash
make clean
```

You can see flowmapper version and help page with:

```bash
flowmapper --version # flowmapper, version 0.0.0.post9001
flowmapper map --help
# Usage: flowmapper map [OPTIONS] SOURCE TARGET

#   Generate mappings between elementary flows lists

# Arguments:
#   SOURCE  Path to source flowlist  [required]
#   TARGET  Path to target flowlist  [required]

# Options:
#   --fields PATH                   Relationship between fields in source and
#                                   target flowlists  [required]
#   --output-dir PATH               Directory to save mapping and diagnostics
#                                   files  [default: .]
#   --format [all|glad|randonneur]  Mapping file output format  [default: all]
#   --unmatched-source / --no-unmatched-source
#                                   Write original source unmatched flows into
#                                   separate file?  [default: unmatched-source]
#   --unmatched-target / --no-unmatched-target
#                                   Write original target unmatched flows into
#                                   separate file?  [default: unmatched-target]
#   --matched-source / --no-matched-source
#                                   Write original source matched flows into
#                                   separate file?  [default: no-matched-source]
#   --matched-target / --no-matched-target
#                                   Write original target matched flows into
#                                   separate file?  [default: no-matched-target]
#   --help                          Show this message and exit.
```

To run the actual mapper specifying the source and target lists and a [mapping of field names](config/SimaProv9.4-ecoinventEFv3.7.toml):

```bash
flowmapper map --fields config/simapro-ecoinvent.toml \
               --output-dir mappings \
               data/industry-2.0-biosphere.json \
               data/ecoinvent-3.7-biosphere.json
```

This will try all the [matching rules](https://github.com/fjuniorr/flowmapper/blob/notebooks-logic/flowmapper/match.py#L105) defined in the [`flowmapper`](https://github.com/fjuniorr/flowmapper) package and generate mappings with [`randonneur`](https://github.com/brightway-lca/randonneur) and [`glad`](https://github.com/UNEP-Economy-Division/GLAD-ElementaryFlowResources) formats. By default it will also write the original unmatched flows into a file.

The objective is to have a **maintainable, transparent, and reproducible system** which can be applied to new lists as they are released.
