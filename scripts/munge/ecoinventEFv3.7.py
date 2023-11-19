import petl as etl
import typer

def main(input, output):
    etl.tojson(
    etl.fromcsv(input, encoding='utf-8-sig'), 
        output, 
        indent = 2
    )
    return True

if __name__ == '__main__':
    typer.run(main)
