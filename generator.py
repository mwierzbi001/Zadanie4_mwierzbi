import json
from jinja2 import Environment, FileSystemLoader


def generate():
    with open('interface.json', 'r') as f:
        config = json.load(f)

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.j2')

    output_code = template.render(config)

    with open('generated_proto.py', 'w') as f:
        f.write(output_code)

    print("Wygenerowano nowe 'generated_proto.py' za pomocą ctypes")


if __name__ == "__main__":
    generate()