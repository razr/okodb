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
