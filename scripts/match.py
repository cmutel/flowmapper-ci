from tqdm import tqdm
import logging
import json
from pathlib import Path
from flowmapper.cas import CAS
from flowmapper.match import match_rules, match
from flowmapper.flow import Flow
from flowmapper.utils import read_field_mapping
from scripts.utils import read_flowlist

logger = logging.getLogger(__name__)

def main(source_filepath: Path, target_filepath: Path, fields, output_file: Path = Path('mapping.json')):
    fields = read_field_mapping(fields)
    source_flows = [Flow.from_dict(flow, fields['source']) for flow in read_flowlist(source_filepath)]
    target_flows = [Flow.from_dict(flow, fields['target']) for flow in read_flowlist(target_filepath)]

    mappings = match(source_flows, target_flows)

    with open(output_file, 'w') as fs:
        json.dump(mappings, fs, indent=2)
