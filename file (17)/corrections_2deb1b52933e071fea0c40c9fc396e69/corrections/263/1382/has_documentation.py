from importlib import import_module

m_imported = import_module("models.user")

if m_imported.__doc__ is None:
    print("No module documentation")

if m_imported.User.__doc__ is None:
    print("No class documentation")
