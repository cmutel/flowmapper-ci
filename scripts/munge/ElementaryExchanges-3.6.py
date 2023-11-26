import json
import xmltodict
import typer

def main(input, output):
    with open(input) as fs:
        ei_xml = xmltodict.parse(fs.read())['validElementaryExchanges']['elementaryExchange']

    with open(output, 'w') as fs:
        json.dump(ei_xml, fs, indent=2)
    return True

if __name__ == '__main__':
    typer.run(main)
