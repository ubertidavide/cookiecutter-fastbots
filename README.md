# cookiecutter-fastbots
Ready to use project setup for web automated bot or scraper using the fastbots library.  
Make a bot in a faster way, without thinking at webdriver or selenium related code and config.  
Use a driver transparent library, with less boilerplate code.  
Be sure that if the locators of the page change you don't need to touch your code, but just quick adapt the config.  
Chek out docs and settings in the official repo: [fastbots](https://github.com/ubertidavide/fastbots).  

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
    ./run.sh or ./run.bat (linux or windows)
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