from sejoung.wrapper import run_script


def test_wrapper():
    run_script("/Users/beni/wrapper_python/src/sejoung/run.py", "/Users/beni/wrapper_python/src/sejoung/test.json")
    assert True

def test_wrapper_is_null():
    run_script("/Users/beni/wrapper_python/src/sejoung/run.py", "")
    assert True
