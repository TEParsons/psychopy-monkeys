from psychopy_monkeys.components.keyboardMonkey import KeyboardMonkeyComponent
from psychopy_monkeys.utils.monkey import Monkey
from psychopy.tests.test_experiment.test_components.test_base_components import BaseComponentTests, _TestLibraryClassMixin

class TestKeyboardMonkeyComponent(BaseComponentTests, _TestLibraryClassMixin):
    """
    Basic Component tests
    """
    comp = KeyboardMonkeyComponent
    libraryClass = Monkey
