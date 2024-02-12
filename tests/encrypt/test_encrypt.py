import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    """Test the encrypt_message function."""

    with pytest.raises(TypeError):
        encrypt_message(1, 1)
    assert encrypt_message("axdefg", 1) == "a_gfedx"
    assert encrypt_message("axdefg", 3) == "dxa_gfe"

    assert encrypt_message("axdefg", 2) == "gfed_xa"
    assert encrypt_message("axdefg", 4) == "gf_edxa"

    assert encrypt_message("axdefg", 9) == "gfedxa"
    assert encrypt_message("axdefg", 6) == "gfedxa"
