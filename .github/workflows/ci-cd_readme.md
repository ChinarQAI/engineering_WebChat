# Code Test CI Workflow

This repository includes a GitHub Actions workflow to ensure continuous integration. The workflow automates tasks like linting, testing, and ensuring compatibility across multiple Python versions.

---

## Workflow Name

**Code test with Flake8 and Pytest**

---

## Triggering Events

The workflow is triggered on:

1. **Push events** to the `main` branch.
2. **Pull requests** targeting the `main` branch.

---

## Workflow Structure

The workflow includes a single job, `build`, which performs the following steps:

### 1. **Environment Setup**

- **Runs on**: `ubuntu-latest`
- **Python versions tested**: 3.9, 3.10, 3.11
  - This is achieved using a **matrix strategy**, which runs the job for each specified Python version.

---

### 2. **Job Steps**

#### a. Checkout Repository
Uses the `actions/checkout@v4` action to fetch the repository code.

#### b. Set Up Python
Uses `actions/setup-python@v3` to set up Python based on the version specified in the matrix (`3.9`, `3.10`, `3.11`).

#### c. Configure Environment Variables
Secrets stored in GitHub (e.g., `ES_ENDPOINT`, `OPENAI_API_KEY`) are loaded as environment variables. These variables are added to `$GITHUB_ENV` for use in subsequent steps.

#### d. Verify Environment Variables (Optional)
Prints the environment variables to verify their configuration. This step can be removed or restricted to specific debugging scenarios.

#### e. Install Dependencies
- Upgrades `pip` to the latest version.
- Installs essential tools like `flake8` and `pytest`.
- Installs project-specific dependencies if a `requirements.txt` file is present.

#### f. Lint with flake8
Performs static code analysis using `flake8`:
- Stops the build for critical issues (e.g., syntax errors, undefined names).
- Treats other errors as warnings to avoid breaking the build.

#### g. Test with pytest
Runs the test suite using `pytest`. Ensure our tests are defined in a format compatible with `pytest`.

---

## Outputs

1. **Linting Report**: Provides statistics and warnings/errors based on `flake8` rules.
2. **Test Results**: Displays the output of `pytest` for the test suite.
3. **CI Validation**: Confirms compatibility across multiple Python versions.

---

This workflow ensures a robust CI pipeline for our code, helping maintain code quality and reliability.
