"""Test __init__."""


def test_init(hello_world):
    """Run a test."""
    import nr_blockchain

    # Test __init__
    assert hasattr(nr_blockchain, '__version__')

    # Test pytest fixtures
    assert(hello_world == "Hello World!")
