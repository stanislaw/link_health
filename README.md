# Link Health (a dead links checker)

`link_health.py` is a very simple Python script that checks the health of
Web links provided by a user. The script reads the links from a file and then
accesses them one by one. If all links are healthy, the script exits with a
successful exit code (0), if at least one of the links is dead, the script
records all failed links and exits with an error exit code (1).

```bash
python link_health.py <your_file_with_links.md>
```

The tool is very basic and is not intended to be released as a Pip package,
however, it works for 95%+ links that the author cares about (see known issues
below). 

## Known issues

This script uses only the `requests` library, so to many of the websites that
have protection against bots, this script's requests can be rejected with
HTTP error codes like `HTTP 403 Forbidden.` or left with no answer at all.
To record such exceptions, the link_health.py script can read them from a config
file `.link_health.yml`. Example:

```
exceptions:
  - url: https://www.fastcompany.com/28121/they-write-right-stuff
    code: HTTP_403
exceptions:
  - url: https://www.bugseng.com/blog/requirement-traceability-all-substance-and-no-fuss
    code: CONNECTION_ERROR
```

A list of available codes:

```
[
    'SUCCESS',
    'SUCCESS_READ_TIMEOUT_EXPECTED',
    'HTTP_4xx',
    'HTTP_403',
    'HTTP_5xx',
    'CONNECTION_ERROR',
    'SSL_ERROR',
    'CONNECT_TIMEOUT',
    'READ_TIMEOUT'
]
```

To record an exception, just follow which error the script fails with on your
URL and then just use its code for the `code:` field.

## License

The license for this software is Apache 2. See LICENSE for details.
