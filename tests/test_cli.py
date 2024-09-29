import subprocess


def test_main():
    assert subprocess.check_output(["wtf", "foo", "foobar"], text=True) == "foobar\n"
