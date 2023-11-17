# cookiecutter-fastbots
An example bot cookiecutter template made with the fastbots library.

## Requirements

### Standard:
- Python (3.11 or above)
- Poetry
- Firefox or Chrome

### Dockerized:
- Docker

## Usage

### Standard
Install all the dependencies and then run the main.py form the root folder of the project.
```bash
    poetry install
    ./run.sh
```

### Dockerized:
In order to run with docker, the entrypoint main.py is required in the root of the project.

```bash
    docker-compose up
```

## Structure
- **/pages**: Folder that contains all the Pages models.
- **/tasks**: Folder that contains all the Task availables.
- **main.py**: Call the task needed to be executed.
- **locators.ini**: File that contains all the locators settings.
- **settings.ini**: File that contains all the settings.
- **preferences.json**: File that contains all the driver's preferences.
**Checkout the library docs** in the readme of the official repo: [fastbots](https://github.com/ubertidavide/fastbots)