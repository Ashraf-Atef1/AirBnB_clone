from importlib import import_module

m_imported = import_module("models.state")

if m_imported.__doc__ is None:
    print("No module documentation")

if m_imported.State.__doc__ is None:
    print("No class documentation")

m_imported = import_module("models.city")

if m_imported.__doc__ is None:
    print("No module documentation")

if m_imported.City.__doc__ is None:
    print("No class documentation")

m_imported = import_module("models.place")

if m_imported.__doc__ is None:
    print("No module documentation")

if m_imported.Place.__doc__ is None:
    print("No class documentation")

m_imported = import_module("models.amenity")

if m_imported.__doc__ is None:
    print("No module documentation")

if m_imported.Amenity.__doc__ is None:
    print("No class documentation")

m_imported = import_module("models.review")

if m_imported.__doc__ is None:
    print("No module documentation")

if m_imported.Review.__doc__ is None:
    print("No class documentation")
