from importlib import import_module

m_imported = import_module("models.engine.file_storage")

if m_imported.__doc__ is None:
    print("No module documentation")

if m_imported.FileStorage.__doc__ is None:
    print("No class documentation")
