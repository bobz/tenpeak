# Register our skins directory - this makes it available via portal_skins.
from Products.CMFCore.DirectoryView import registerDirectory
GLOBALS = globals()
registerDirectory('skins', GLOBALS)

def initialize(context):
    """Intializer called when used as a Zope 2 product."""
