from note_helper.link_handling import _clean_string_of_aliases, build_rehydration_map


def test_build_rehydration_map():
    test_alias = {"hi": True, "bi": True, "hi bi": True, "cool": True}
    expected_map = {
        "h": None,
        "b": None,
        "hi": "hi",
        "bi": "bi",
        "hi ": "hi",
        "hi b": "hi",
        "hi bi": "hi bi",
        "c": None,
        "co": None,
        "coo": None,
        "cool": "cool",
    }
    assert build_rehydration_map(test_alias) == expected_map


def test_clean_string_of_aliases_does_not_match_with_exclamation_point():
    test_string = "hi [[hi]] ![[hi]]"
    expected_string = "hi hi ![[hi]]"
    actual_string, _ = _clean_string_of_aliases(test_string)
    assert actual_string == expected_string
