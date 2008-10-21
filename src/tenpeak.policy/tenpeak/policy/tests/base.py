from Products.Five import zcml
from Products.Five import fiveconfigure

from Testing import ZopeTestCase as ztc

from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

# These are traditional products (in the Products namespace).  They'd normally
# be loaded automatically, but in tests we have to load them explicitly.  This
# should happen at module level to make sure they are available early enoug.

ztc.installProduct('SimpleAttachment')
ztc.installProduct('RichDocument')

@onsetup
def setup_tenpeak_policy():
    """Set up the additional products required for the Tenpeak site policy.

    The @onsetup decorator causes the execution of this body to be deferred until the setup of the Plone site testing layer
    """
    
    # Load the ZCML configuration for the tenpeak.policy package.

    fiveconfigure.debug_mode = True
    import tenpeak.policy
    zcml.load_config('configure.zcml', tenpeak.policy)
    fiveconfigure.debug_mode = False

    # We need to tell the testing framework that these products
    # should be available.  This can't happen until after we have loaded 
    # the ZCML.

    ztc.installPackage('tenpeak.policy')
    ztc.installPackage('tenpeak.theme')

# The order here is important:  We first call the (deferred) function
# which installs the product we need for teh Tenpeak package. Then,
# we let PloneTestCase set up this product on installation.

setup_tenpeak_policy()
ptc.setupPloneSite(products=['tenpeak.policy'])

class TenpeakPolicyTestCase(ptc.PloneTestCase):
    """We use this base class for all the tests in this package.  If necessarey, we can put common utility or setup code in here.
    """

    
