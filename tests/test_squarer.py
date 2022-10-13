from app.squarer import square


def test_square():
    """Square a number."""
    # When
    subject = square(4)

    # Then
    assert subject == 16
