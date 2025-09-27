Simple utility that can convert .toml file to .yaml to use in docker-compose.

# Building
Create venv, install all packages from req.txt

Build it


``
pyinstaller --onefile main.py
``

If you want to install it system-wide just put /dist/main to /bin directory

``sudo mv dist/main /bin/docker-compose-toml``


# Valid docker-compose.toml example file

[Click here](docker-compose.toml.sample)