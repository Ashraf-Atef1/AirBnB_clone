from importlib import import_module

m_imported = import_module("models.base_model")

if m_imported.__doc__ is None:
    print("No module documentation")

if m_imported.BaseModel.__doc__ is None:
    print("No class documentation")
