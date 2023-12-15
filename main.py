from flowmapper import Flowmap
from flowmapper.utils import read_flowlist, read_field_mapping
from flowmapper.flow import Flow
import pandas as pd
from deepdiff import DeepDiff
import json
from rich import print as rprint
from pprint import pprint

fields = read_field_mapping('config/simapro-ecoinvent.py')

flows39 = read_flowlist("data/ecoinvent-3.9-biosphere.json")

flows39 = [Flow.from_dict(flow, fields['target']) for flow in flows39]

flows39 = pd.DataFrame([
    {"id": flow.id,
     "uuid": flow.uuid,
     "name": flow.name.raw_value,
     "context": flow.context.raw_value,
     "unit": flow.unit.raw_value}
    for flow in flows39
])

flows39.to_excel('data/ecoinvent-3.9-biosphere.xlsx', index=False)



flows310 = read_flowlist("data/ecoinvent-3.10-biosphere.json")

flows310 = [Flow.from_dict(flow, fields['target']) for flow in flows310]

flows310 = pd.DataFrame([
    {"id": flow.id,
     "uuid": flow.uuid,
     "name": flow.name.raw_value,
     "context": flow.context.raw_value,
     "unit": flow.unit.raw_value}
    for flow in flows310
])

flows310.to_excel('data/ecoinvent-3.10-biosphere.xlsx', index=False)


with open('data/39.json') as fs:
    flow39 = json.load(fs)

with open('data/310.json') as fs:
    flow310 = json.load(fs)


diff = DeepDiff(flow39['name'], flow310['name'])
diff = DeepDiff(flow39['synonym'], flow310['synonym'])
diff = DeepDiff(flow39['property'], flow310['property'])

flow310['property'][3]

print(diff.pretty())

rprint(diff)