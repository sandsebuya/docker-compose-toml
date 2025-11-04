import tomllib
import yaml
import sys
import subprocess
from string import Template
import os


def read_toml() -> dict:
    with open("docker-compose.toml", "rb") as f:
        data = tomllib.load(f)
        return data


def generate_yaml(data: dict):
    if len(sys.argv) == 1:
        yaml_str = Template(
            yaml.dump(data, allow_unicode=True, default_flow_style=False)
        )
        print(yaml_str.substitute(os.environ))
    with open("docker-compose.yaml", "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False)


def run_compose():
    if len(sys.argv) == 1:
        raise SystemExit()
    try:
        sys_arg = sys.argv[1:]
        sys_arg.insert(0, "compose")
        sys_arg.insert(0, "docker")
        process = subprocess.Popen(
            sys_arg, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
        )

        for line in process.stdout:
            print(line, end="")

        process.wait()
        print(f"Команда завершилась с кодом: {process.returncode}")
    except KeyboardInterrupt:
        print("Pressed Ctrl+C, killing process...")
        process.terminate()
        process.wait()


if __name__ == "__main__":
    parsed_toml = read_toml()
    generate_yaml(parsed_toml)
    run_compose()
