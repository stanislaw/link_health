from link_health import find_links


def test_01():
    assert find_links("") == []
    assert find_links("https://www.microsoft.com") == [
        "https://www.microsoft.com"
    ]
    assert find_links("https://www.microsoft.com.") == [
        "https://www.microsoft.com"
    ]
    assert find_links("https://github.com/openlawlibrary/pygls.") == [
        "https://github.com/openlawlibrary/pygls"
    ]
    assert find_links("https://github.com/textX/textX>") == [
        "https://github.com/textX/textX"
    ]
    assert find_links("https://github.com/textX/textX}") == [
        "https://github.com/textX/textX"
    ]
    assert find_links("https://github.com/stanislaw/FileCheck.py}") == [
        "https://github.com/stanislaw/FileCheck.py"
    ]
    assert find_links("https://github.com/DatabaseCleaner/database_cleaner/commits?author=stanislaw}") == [
        "https://github.com/DatabaseCleaner/database_cleaner/commits?author=stanislaw"
    ]
    assert find_links("https://github.com/DatabaseCleaner/database_cleaner/issues?q=is%3Aopen+is%3Aissue+author%3Astanislaw+label%3Adoc") == [
        "https://github.com/DatabaseCleaner/database_cleaner/issues?q=is%3Aopen+is%3Aissue+author%3Astanislaw+label%3Adoc"
    ]
    assert find_links("https://www.youtube.com/watch?v=cdZZpaB2kDM") == [
        "https://www.youtube.com/watch?v=cdZZpaB2kDM"
    ]
