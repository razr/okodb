# OkodB

OkodB is a lightweight database designed to store and manage a collection of common porting errors and fixes in JSON format. It helps automate program repair during porting tasks by categorizing errors and linking corresponding patches or configuration options. This database is especially useful for porting software to embedded systems like VxWorks, providing quick access to relevant fixes and configurations.

## Features

* **Error Records**: Contains common errors and their solutions.
* **Fixes Storage**: Stores patch files or configuration options as fixes for the errors.
* **Categorization**: Errors and fixes are categorized by programming language, such as CMake, Make, C, C++, Python, etc.
* **Easy Lookup**: Search for specific errors and their corresponding patches/fixes.
* **Trainable for Automated Repair**: This database can be used to train an LLM (Language Model) for automated program repair.
* **Python Package & CLI**: Access OkodB programmatically or via command line.

## Structure

The database is organized into four main categories:

- `errors/`: JSON files containing error details.
- `fixes/`: JSON files with fix details, including patches or configuration commands.
- `sdks/`: JSON files describing operating systems and their SDKs.
- `repositories/`: JSON files describing repositories with their metadata.

## Installation

Install via pip:

```bash
$ pip install .
```

Or install in editable mode during development:

```bash
$ pip install -e .
```

### CLI Tools

- `okodb-create`: Generates a combined `okodb.json` database from the individual JSON files.
- `okodb-validate`: Validates repository JSON files against the schema.

## Setup / Creating the Database

To create the combined database (`okodb.json`) from the individual JSON files:

```bash
$ okodb-create
```

This is equivalent to running the previous Python script manually.

## Validating Repository Records

To validate all repository JSON files against the schema:

```bash
$ okodb-validate
```

Any invalid files will be reported with detailed error messages.

## Using OkodB with JSON Server

1. Install JSON Server:

```bash
$ npm install -g json-server
```

2. Start the server:

```bash
$ json-server okodb.json
```

3. Access the database via HTTP:

* List all errors: http://localhost:3000/errors
* List all fixes: http://localhost:3000/fixes
* Retrieve specific categories, e.g., CMake errors: http://localhost:3000/errors?language=CMake

## Extending OkodB

1. Add new errors, fixes, OS descriptions, or repositories as JSON files in their respective directories.
2. Run `okodb-create` to regenerate the database.

## Contributing

Contributions are welcome! If you have ideas for improving OkodB or want to add new error/fix entries, feel free to open a pull request or submit an issue.

## License

OkodB is released under the MIT License.
