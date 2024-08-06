from psychopy_monkeys.components.mouseMonkey import MouseMonkeyComponent
from psychopy_monkeys.utils.monkey import Monkey
from psychopy.tests.test_experiment.test_components.test_base_components import BaseComponentTests, _TestLibraryClassMixin

class TestMouseMonkeyComponent(BaseComponentTests, _TestLibraryClassMixin):
    """
    Basic Component tests
    """
    comp = MouseMonkeyComponent
    libraryClass = Monkey
