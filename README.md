# CT-X700/X800/CDP-S350 RBK File Editor

## Requirements:
- [Python 3.9](https://www.python.org/downloads/) (server runtime)
- [Pip](https://pip.pypa.io/en/stable/cli/pip_install/) (Python package manager)

## Optional nice-to-haves:
- Rust (latest stable build)
- Tauri (latest stable)
- Node.js

## To run this app:
1. open a Terminal or Command Prompt window
2. navigate to any folder (this will be where the project lives on your device)
3. call `git clone https://github.com/olmigs/flaskapp.git`
4. navigate to folder `flaskapp/` (e.g. `cd flaskapp/`) and call `python3 server.py`
5. open a second Terminal or Command Prompt window
6. navigate to folder `flaskapp/client/` and call `yarn dev`
7. open a browser window and type `localhost:5000` into the address bar

Okay, at this point you have managed to (a) run the Python server that handles importing and exporting RBK files and (b) run the Javascript development server that updates the application UI automatically. You should now be ready for testing in a web browser. If you want to compile and run the app in development mode (using Tauri/Rust):

8. navigate to folder `flaskapp/client/` and call `yarn tauri dev`

*Note: Please ensure that all RBK files are in the folder `flaskapp/file/`.*

## Known issues:
- handling missing files; as of `06/22/21`, the app will do nothing if the file does not exist
- updates to `casio_rbk` library are not automatically included; to get the latest, will need to go to the [Casio-Registrations github page](https://github.com/michgz/casio-registrations)