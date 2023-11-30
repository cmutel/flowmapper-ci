import logging
import json
from pathlib import Path
from flowmapper.flow import Flow
from flowmapper.utils import read_field_mapping, read_flowlist
from flowmapper.flowmap import Flowmap

logger = logging.getLogger(__name__)

def main(source_filepath: Path, target_filepath: Path, fields, output_file: Path = Path('mapping.json')):
    fields = read_field_mapping(fields)
    source_flows = [Flow.from_dict(flow, fields['source']) for flow in read_flowlist(source_filepath)]
    target_flows = [Flow.from_dict(flow, fields['target']) for flow in read_flowlist(target_filepath)]

    flowmap = Flowmap(source_flows, target_flows)
    flowmap.match()
    result = flowmap.to_randonneur()

    with open(output_file, 'w') as fs:
        json.dump(result, fs, indent=2)
