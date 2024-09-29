from wiring_the_filesystem import compute


def test_compute():
    assert compute(["a", "bc", "abc"]) == "abc"
