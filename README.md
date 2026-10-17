# DevSecOps Lab

A hands-on DevSecOps learning project focused on Python application development, automated testing, CI pipelines, and containerization.

The goal is to progressively build a secure software delivery workflow using practical tools and industry-relevant practices.

## Current Features

- **Python application:** Generates structured security events in JSON format.
- **Unit testing:** Uses Python's built-in `unittest` framework to validate application behavior.
- **CI automation:** GitHub Actions automatically runs checks on pushes and pull requests.
- **Static security analysis:** Bandit scans Python code for potentially insecure patterns.
- **Dependency auditing:** `pip-audit` checks declared Python dependencies for known vulnerabilities.
- **Docker containerization:** Packages the application into a Docker image.
- **Automated Docker build:** GitHub Actions builds the Docker image as part of the CI workflow.

## Tech Stack

- Python 3.13
- Git and GitHub
- GitHub Actions
- Docker
- Bandit
- pip-audit
- YAML

## Project Structure

```text
DevSecOps-Lab/
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── app/
│   ├── main.py
│   └── test_main.py
├── docs/
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Raresney/DevSecOps-Lab.git
cd DevSecOps-Lab
```

### 2. Run the application

```bash
python app/main.py
```

The application generates a JSON event containing a timestamp, event type, and severity.

### 3. Run unit tests

```bash
python -m unittest discover -s app -p "test_*.py" -v
```

### 4. Build the Docker image

Make sure Docker Desktop is running, then execute:

```bash
docker build -t devsecops-app:1.0 .
```

### 5. Run the container

```bash
docker run --rm devsecops-app:1.0
```

The application executes inside the container and prints the generated JSON event.

## CI Pipeline

The workflow is defined in `.github/workflows/python-tests.yml`.

It runs automatically on pushes and pull requests.

### Current workflow stages

1. **Checkout:** Retrieves the repository contents.
2. **Python setup:** Configures Python 3.13.
3. **Unit tests:** Validates the application's expected behavior.
4. **Bandit scan:** Checks the Python source code for potentially insecure patterns.
5. **Dependency audit:** Uses `pip-audit` to check dependencies declared in `requirements.txt` against known vulnerabilities.
6. **Docker build:** Builds the application image in the GitHub Actions runner.

The test and Docker build jobs currently run independently and may execute in parallel.

## Learning Objectives

This project is designed to develop practical skills in:

- CI/CD fundamentals and Git workflows
- Automated testing
- Secure coding and static analysis
- Python dependency security
- Docker images and containers
- Security checks integrated into CI pipelines
- Building toward cloud security and DevSecOps practices

## Roadmap

- [ ] Integrate container image vulnerability scanning with Trivy
- [ ] Add secret scanning
- [ ] Improve dependency management
- [ ] Add Docker security best practices
- [ ] Introduce build and release controls
- [ ] Explore deployment to a test environment
- [ ] Explore cloud infrastructure security and Infrastructure as Code

## Disclaimer

This is a learning and portfolio project. Security scanners provide useful signals but cannot guarantee that an application is secure. Findings require review, and additional testing is needed for production use.

## Author

**Rares Bighiu**

GitHub: [@Raresney](https://github.com/Raresney)
