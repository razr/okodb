# OkodB

OkodB is a lightweight database designed to store and manage a collection of common porting errors and fixes in JSON format. It helps automate program repair during porting tasks by categorizing errors and linking corresponding patches or configuration options. This database is especially useful for porting software to embedded systems like VxWorks, providing quick access to relevant fixes and configurations.

## Features

* **Error Records**: Contains common errors and their solutions.
* **Fixes Storage**: Stores patch files or configuration options as fixes for the errors.
* **Categorization**: Errors and fixes are categorized by programming language, such as CMake, Make, C, C++, Python, etc.
* **Easy Lookup**: Search for specific errors and their corresponding patches/fixes.
* **Trainable for Automated Repair**: This database can be used to train an LLM (Language Model) for automated program repair.

## Structure

The database is organized into four main categories:
- `errors/`: JSON files containing error details.
- `fixes/`: JSON files with fix details, including patches or configuration commands.
- `sdks/`: JSON files describing operating systems and their SDKs.
- `repositories/`: JSON files describing repositories with their metadata.

## Setup

To create the combined database (`okodb.json`) from the individual JSON files, run the provided Python script:

```bash
$ python3 scripts/create_okodb.py
```

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
* Retrieve specific categories:
  * CMake errors: http://localhost:3000/errors?language=CMake

## Queries and Usage Examples

1. Retrieve Errors by Language

```bash
$ curl "http://localhost:3000/errors?language=CMake"
```

2. Retrieve Fix by ID

```bash
$ curl "http://localhost:3000/fixes?id=disable-iconv"
```

3. Retrieve SDK Information

```bash
$ curl "http://localhost:3000/sdks"
```

## Using OkodB with cURL

To retrieve errors and their corresponding fixes using `curl`, you can follow these steps:

1. Retrieve an Error

For example, to find errors related to "Could NOT find Iconv", use the following command:

```bash
$ curl "http://localhost:3000/errors?error_message_like=Could%20NOT%20find%20Iconv"
```

Example output:

```json
[
  {
    "id": "cmake-iconv-error",
    "error_message": "Could NOT find Iconv (missing: Iconv_LIBRARY Iconv_INCLUDE_DIR)",
    "description": "CMake provides an option LIBXML2_WITH_ICONV to add ICONV support, which is set to ON by default, but Iconv is not supported by VxWorks.",
    "command": "cmake .. -DCMAKE_TOOLCHAIN_FILE=$WIND_CC_SYSROOT/mk/toolchain.cmake -DPython_EXECUTABLE=$WIND_SDK_HOME/vxsdk/host/x86_64-linux/bin/python3.9 -DPython_ROOT_DIR=/usr/3pp/develop/usr/",
    "category": "dependency_error",
    "repository_id": "libxml2-v2.12.6",
    "sdk_id": "wrsdk-vxworks7-qemu-1.14",
    "fix_id": "disable-iconv",
    "language": "CMake",
    "url": "https://cmake.org/cmake/help/latest/module/FindIconv.html",
    "file": "CMakeLists.txt",
    "line": 103,
    "line_content": "find_package(Iconv REQUIRED)"
  }
]
```

2. Retrieve a Fix

To retrieve the fix associated with the error, use the `fix_id` from the previous response. In this case, the `fix_id` is `disable-iconv`. Use the following curl command:

```bash
$ curl "http://localhost:3000/fixes?id=disable-iconv"
```

Example output:

```json
[
  {
    "id": "disable-iconv",
    "type": "configuration",
    "language": "CMake",
    "option": "-DLIBXML2_WITH_ICONV=OFF",
    "description": "Disable Iconv support in the CMake configuration since it is not available in VxWorks."
  }
]
```

## Extending OkodB

OkodB is designed for easy extensibility:

1. Add new errors, fixes, OS descriptions, or repositories as JSON files in their respective directories.
2. Run create_okodb.py to regenerate the database.

## Contributing

Contributions are welcome! If you have ideas for improving OkodB or want to add new error/fix entries, feel free to open a pull request or submit an issue.

## License

OkodB is released under the MIT License.