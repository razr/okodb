# Using OkodB with Python

You can load and inspect the database directly from Python. Here’s a minimal example:

```bash
$ python3 examples/hello_okodb.py


Example output:

OkodB contains:
  2 errors
  2 fixes
  1 repositories
  2 SDKs

Example error:
  ID: cmake-iconv-missing
  Message: Could NOT find Iconv (missing: Iconv_LIBRARY Iconv_INCLUDE_DIR)
  Repository: libxml2-v2.12.6
  Fix: disable-iconv

Example fix:
  ID: disable-iconv
  Option: -DLIBXML2_WITH_ICONV=OFF
  Description: Disable Iconv support during the CMake configuration since it is not available in VxWorks.
```

## Queries and Usage Examples

1. Retrieve Errors by Language

```
$ curl "http://localhost:3000/errors?language=CMake"
```

2. Retrieve Fix by ID

```
$ curl "http://localhost:3000/fixes?id=disable-iconv"
```

3. Retrieve SDK Information

```bash
$ curl "http://localhost:3000/sdks"
```

## Using OkodB with cURL

To retrieve errors and their corresponding fixes using curl, you can follow these steps:

1. Retrieve an Error
For example, to find errors related to "Could NOT find Iconv", use the following command:

```bash
$ curl "http://localhost:3000/errors?error_message_like=Could%20NOT%20find%20Iconv"
```

Example output:

```bash
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

To retrieve the fix associated with the error, use the fix_id from the previous response. In this case, the fix_id is disable-iconv. Use the following curl command:

```bash
$ curl "http://localhost:3000/fixes?id=disable-iconv"
Example output:

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
