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
