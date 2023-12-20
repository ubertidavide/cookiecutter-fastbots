# cookiecutter-fastbots

A project template ready to use, tailored for effortless utilization in crafting web automated bots or scrapers, leveraging the fastbots library.

## Usage

Install cookiecutter and generate the project from this template.

```bash
# Install Cookiecutter (if not already installed)
pip install cookiecutter

# Use Cookiecutter to generate a project using this template
cookiecutter gh:ubertidavide/cookiecutter-fastbots
```
For more details on the cookiecutter usage see [it's documentation](https://cookiecutter.readthedocs.io/en/stable/README.html).

### Standard Usage

To run the project using the standard approach, follow these steps:

#### Install Dependencies

Ensure Poetry is installed on your system. If not, you can install it by following the instructions on the [official Poetry installation page](https://python-poetry.org/docs/).

Install the project dependencies using Poetry. Navigate to the root folder of the project and run:

```bash
poetry install
```

#### Configure Browser

Ensure that you have the desired web browser installed on your system. 

#### Run the Project

After installing the dependencies and configuring the browser:

Run the **main.py** script from the root folder of the project:
```bash
    ./run.sh or ./run.bat (linux or windows)
```
This script will execute the automation tasks specified in the main.py file.

### Dockerized

If you prefer to run the project using Docker:

Ensure that [Docker](https://docs.docker.com/get-docker/) is installed on your machine.

The entrypoint **main.py** is required in the root of the project.

Run the following command to start the project using Docker Compose:

```bash
docker-compose up
```
This command will build the Docker image and start the containerized environment.

Please note that the Dockerized approach provides a self-contained environment with all dependencies pre-configured, making it easy to run the project consistently across different systems.

## Structure

The Cookiecutter template follows a specific structure to organize various components of your project:

- **/core**: This folder contains all the custom global configs declared for all the project, loaded from the settings.ini.

- **/pages**: This folder contains all the Page models. Pages are likely representations of web pages or components in your application.

- **/tasks**: In this folder, you'll find all the available Task modules. Tasks represent the specific actions or functionalities that your automation framework can perform.

- **main.py**: This is the main entry point for your project. It calls the task that needs to be executed, serving as the starting point for your automation workflow.

- **locators.ini**: This file holds all the settings related to locators. Locators are typically used to identify and interact with elements on web pages.

- **settings.ini**: The settings file contains configuration parameters and options for your automation framework. Users can customize these settings based on their specific requirements.

- **preferences.json**: This JSON file includes all the driver's preferences. It could store preferences for the web driver, such as browser options or other settings.

## Additional Information

For more detailed documentation and information about using this automation library, please refer to the [fastbots official documentation](https://github.com/ubertidavide/fastbots). The library documentation will provide further guidance on how to leverage the features and capabilities of the framework.