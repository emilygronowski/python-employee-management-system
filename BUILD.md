[Home](README.md) > Building the Employee Management System project

# Building the Employee Management System project
This document provides instructions for installing required dependencies and building the development container.

## Prerequisites
1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) and ensure it is running on your system.
1. Install [Visual Studio Code](https://code.visualstudio.com/).
1. Launch Visual Studio Code.
1. Select the "Extensions" tab within Visual Studio Code.
1. Search and install the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.
1. If prompted after installation, relaunch Visual Studio Code.
1. Select "File" within Visual Studio Code.
1. Select "Open Folder..." and choose the `python-employee-management-system` project folder to open the project within Visual Studio Code.

## Setup Instructions
1. Ensure the [Prerequisites](#prerequisites) section has been successfully completed.
1. Follow one of the below subsection approaches to build the Dev Container.

### Opening a Remote Window
1. On the bottom-left of Visual Studio Code, there will be a `><` button underneath the "Manage" gear tab. Click the button.
1. In the provided menu, select "Reopen in Container". You can track the progress by clicking the "Connecting to Dev Container (show log)" link in the bottom-right notification.

### Using Command Palette
1. Open the **Command Palette** by selecting "View" then "Command Palette..." or using the shortcuts `CTRL+SHIFT+P` or `F1`.
1. Type and select `Dev Containers: Reopen in Container`.
1. Standby for the container to build. You can track the progress by clicking "Connecting to Dev Container (show log)" link in the bottom-right notification. Visual Studio Code will open a new window with the `python-employee-management-system` project within the Dev Container.

### Exiting the Dev Container
If you are completely finished working in the `python-employee-management-system` project, you may simply close Visual Studio Code. This will stop the running Dev Container in Docker.

If you wish to reopen your project locally when finished working within the Dev Container, click the "Dev Container: Python Dev Container @ desktop-linux" at the bottom-left (may be blue-in-color depending on your system) and select the "Reopen Folder Locally" option in the provided menu.

## Quality Assurance
1. Ensure [Setup Instructions](#setup-instructions) section has been successfully completed.
1. Use the following commands to run linting checks and tests:
    ```bash
    ruff check .
    ruff format --check .
    pyright
    pytest
    ```

### Modifying the Code Coverage Threshold
1. Open the [pyproject.toml](pyproject.toml) file.
1. View line 38 for the `addopts` setting.
1. Locate the `--cov-fail-under=90` argument on line 41.
1. Change "90" to your preferred percentage.

## Troubleshooting
1. I tried to reopen my container in Visual Studio Code but received the following error:  
    > **Docker returned an error.**
    >
    > Make sure the Docker daemon is running.
    
    > **Corrective Action**: You have received this error because Docker Desktop is not running on your system at the time you attempted to open the `python-employee-management-system` project in a Dev Container.
    >
    > Relaunch Docker Desktop on your system, ensure it is running successfully and reattempt opening the `python-employee-management-system` project in a Dev Container.

[Back to Top](#building-the-employee-management-system-project)
