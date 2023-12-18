from flowmapper.utils import read_field_mapping, read_flowlist
from flowmapper.flowmap import Flowmap
from flowmapper.flow import Flow
import io
import csv
from jinja2 import Environment, FileSystemLoader
import tiktoken

def count_tokens(string, encoding_name = "cl100k_base"):
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def render_prompt(template, data):
    loader = FileSystemLoader("templates")
    env = Environment(loader=loader, autoescape=False)
    template = env.get_template(template)
    result = template.render(data = data)
    return result

def prompt_by_context(context, flowmap):
    flows = []

    for flow in flowmap.target_flows:
        if flow.context == context:
            tmp = {"name": flow.name.value, "synonyms": '; '.join(flow.synonyms.value)}
            flows.append(tmp)

    output = io.StringIO()

    fieldnames = ['name', 'synonyms']
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(flows)
    result = render_prompt("prompt.txt.j2", output.getvalue())
    print(f"Tokens of context {context.value}: {count_tokens(result)}")
    return result

fields = read_field_mapping('config/simapro-ecoinvent.py')
source_flows = [Flow.from_dict(flow, fields['source']) for flow in read_flowlist('data/sp-biosphere-1.json')]
target_flows = [Flow.from_dict(flow, fields['target']) for flow in read_flowlist('data/ecoinvent-3.7-biosphere.json')]

flowmap = Flowmap(source_flows, target_flows)

flowmap.statistics()

contexts = list({flow.context for flow in flowmap.unmatched_source})
prompts = {context.value:prompt_by_context(context, flowmap) for context in contexts}

# Tokens of context water/ground-: 2198
# Tokens of context water: 2012
# Tokens of context soil/forestry: 309
# Tokens of context natural resource/in ground: 4025
# Tokens of context water/ocean: 1795
# Tokens of context air: 2924
# Tokens of context natural resource/in air: 177
# Tokens of context air/urban air close to ground: 2798
# Tokens of context natural resource/land: 2113
# Tokens of context natural resource/biotic: 203
# Tokens of context water/surface water: 2416
# Tokens of context air/non-urban air or from high stacks: 2926
# Tokens of context soil: 367
# Tokens of context natural resource/in water: 267
# Tokens of context water/ground-, long-term: 1713
# Tokens of context soil/agricultural: 11106

for context in contexts:
    flows = [flow.name.value for flow in flowmap.unmatched_source if flow.context == context]
    context_path = context.value.replace('/', '_')
    with open(f'prompts/{context_path}-prompt.txt', 'w') as fs:
        fs.write(prompts[context.value])
    with open(f'prompts/{context_path}-flows.txt', 'w') as fs:
        fs.write(str(flows))
