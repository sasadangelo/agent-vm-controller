# IBM Cloud VM Controller

**IBM Cloud VM Controller** is an agentic tool to manage Virtual Server Instances (VSIs) in IBM Cloud.
It supports essential DevOps operations such as **start**, **stop**, and **list** of virtual machines using IBM Cloud's VPC API.

---

## 🧱 Project Architecture

See [docs/architecture.md](docs/architecture.md) for a detailed explanation of the project’s structure, design patterns, and class relationships.

---

## ✅ Prerequisites

Make sure the following tools are installed:

- [Poetry](https://python-poetry.org/docs/) — for Python dependency and environment management
- [pyenv](https://github.com/pyenv/pyenv) — to manage and install Python versions
- Python ≥ **3.13** — recommended to install with `pyenv install 3.13.0`

---

## ⚙️ Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-org/ibm-cloud-vm-controller.git
   cd ibm-cloud-vm-controller
   ```

2. **Set your Python version using pyenv**:

    ```bash
    pyenv local 3.13.0
    ```

3. **Install dependencies using Poetry**:

    ```bash
    poetry install
    ```

4. **Print the path of the virtual environment (optional, for manual activation)**:

    ```bash
    poetry env info --path
    ```

5. **Then activate the environment manually**:

    ```bash
    source $(poetry env info --path)/bin/activate
    ```

6. **Set your IBM Cloud API key in a .env file**:

Rename the file `.env-sample` in `.env` and add your IBM Cloud API Key:

    ```bash
    API_KEY="<your_ibm_cloud_api_key>"
    ```

## ▶️ Usage

Run the controller from the terminal:

    ```bash
    python3 main.py
    ```

This script will:

- List all Virtual Server Instances (VSIs)
- Start a specific VSI by name
- Stop that same VSI

You can customize main.py or integrate the VSI class and command modules in your own workflows or agent frameworks.

## 🧪 Running Unit Tests

To run the included unit tests:

    ```bash
    PYTHONPATH=src python -m unittest tests/test_vsi_controller.py
    ```

Make sure the `.env` file is properly configured and that a valid VSI exists in your IBM Cloud account for full integration test coverage.