import argparse
import importlib.util
import sys
from jinja2 import Template

def import_from_path(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def main(args):
    parser = argparse.ArgumentParser(
        prog="OpenWRT_GenConfig",
        description="Takes a python config and uses that to generate yaml configs to be uploaded to home assistant.",
    )
    parser.add_argument("config", help="config file to generate yamls from")
    args = parser.parse_args(args)
    
    # Dynamically import config file
    config = import_from_path("config", args.config) 

    files = ["openwrt.yaml.j2", "lovelace.yaml.j2"]
    for f in files:
        out_filename = args.config.rpartition(".")[0]+"-"+f.rpartition(".")[0]
        print(f"Generating {out_filename}")
        with open(f) as file:
            template = Template(file.read())
        output = template.render(**config.config)
        with open(out_filename, "w") as file:
            file.write(output)


if __name__ == "__main__":
    main(sys.argv[1:])
