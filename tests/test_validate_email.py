from samplecode.validate import validate_email
import pytest

@pytest.mark.parametrize('email, is_okay', [
    ('john.doe@somecompany.com', True),
    ('asdfjkl;lkj', False),
    ('', False),
    ('test to force it to fail', True)
])
def test_validate_email(email, is_okay):
    assert validate_email(email) == is_okay