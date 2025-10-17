# GitHub Actions Workflows for OkodB

This directory contains GitHub Actions workflows used to build, validate, and test the OkodB Python package.

## Overview

We use GitHub Actions to ensure the quality and correctness of the database and scripts. The workflows include:

1. **CI Validation**
   - Triggered on `push` or `pull_request`.
   - Installs dependencies.
   - Validates all JSON records (`errors`, `fixes`, `repositories`, `sdks`) against their respective JSON schemas.
   - Runs unit tests if any.

2. **On-Demand Manual Runs**
   - Workflows support `workflow_dispatch` so you can trigger validation manually from the GitHub Actions tab.

## Structure

- `validate.yml` – Validates all JSON records and schemas.
- `build.yml` – (Optional) Builds the Python package and runs tests.
- `publish.yml` – (Optional) Publishes the package to PyPI if tests pass.

## Example Usage

### Manual Trigger

1. Go to the **Actions** tab in GitHub.
2. Select the workflow you want to run (e.g., `validate.yml`).
3. Click **Run workflow**.

### Local Testing with `act`

```bash
# Install act: https://github.com/nektos/act
$ act workflow_dispatch --artifact-server-path /tmp/artifacts
```
