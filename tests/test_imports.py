# Import built-in modules
import importlib
import pkgutil

# Import local modules
import ftwd_datatalk


def test_imports():
    """Test import modules."""
    prefix = "{}.".format(ftwd_datatalk.__name__)
    iter_packages = pkgutil.walk_packages(
        ftwd_datatalk.__path__,
        prefix,
    )
    for _, name, _ in iter_packages:
        module_name = name if name.startswith(prefix) else prefix + name
        importlib.import_module(module_name)
