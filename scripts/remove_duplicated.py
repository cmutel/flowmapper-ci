from flowmapper.utils import read_field_mapping, read_flowlist
from flowmapper.flow import Flow
import json
import typer

def main(input, output):
    fields = read_field_mapping('config/simapro-ecoinvent.py')
    source_flows = [Flow.from_dict(flow, fields['source']) for flow in read_flowlist(input)]

    result = [flow.raw for flow in set(source_flows)]

    with open(output, 'w') as fs:
        json.dump(result, fs, indent=2)

    return True

if __name__ == '__main__':
    typer.run(main)
