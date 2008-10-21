from plone.theme.interfaces import IDefaultPloneLayer

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 skin layer.
       If you need to register a viewlet only for the
       "Optilux Theme" skin, this interface must be its layer
       (in theme/viewlets/configure.zcml).
    """
