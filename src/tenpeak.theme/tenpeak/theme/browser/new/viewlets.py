from zope.component import getMultiAdapter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import common

class PathBarViewlet(common.PathBarViewlet):
    """A custom version of the path bar (breadcrumbs) viewlet, which 
    uses slightly different markup.
    """
    
    render = ViewPageTemplateFile('templates/path_bar.pt')
    
    # The update() method, inherited from the base class, takes care of
    # initializing various variables used in the template