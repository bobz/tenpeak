from Products.CMFCore.utils import getToolByName

def setupGroups(portal):
    acl_users = getToolByName(portal, 'acl_users')
    if not acl_users.searchGroups(name='Staff'):
        gtool = getToolByName(portal, 'portal_groups')
        gtool.addGroup('Staff', roles=['StaffMember'])
        
def renameRichDocument(portal):
    portal_types = getToolByName(portal, 'portal_types')
    rich_document_fti = getattr(portal_types, 'RichDocument')
    rich_document_fti.title = "Web page"

def disableDocument(portal):
    portal_types = getToolByName(portal, 'portal_types')
    document_fti = getattr(portal_types, 'Document')
    document_fti.global_allow = False

def importVarious(context):
    """Miscellaneous steps import handle
    """

    if context.readDataFile('tenpeak.policy_various.txt') is None:
        return
    portal = context.getSite()
    setupGroups(portal)
    renameRichDocument(portal)
    disableDocument(portal)
