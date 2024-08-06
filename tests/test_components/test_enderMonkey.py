from psychopy_monkeys.components.enderMonkey import RoutineEnderMonkeyComponent
from psychopy_monkeys.utils.monkey import Monkey
from psychopy.tests.test_experiment.test_components.test_base_components import BaseComponentTests, _TestLibraryClassMixin

class TestRoutineEnderMonkeyComponent(BaseComponentTests, _TestLibraryClassMixin):
    """
    Basic Component tests
    """
    comp = RoutineEnderMonkeyComponent
    libraryClass = Monkey
