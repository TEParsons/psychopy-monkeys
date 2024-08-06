from psychopy_monkeys.components.sliderMonkey import SliderMonkeyComponent
from psychopy_monkeys.utils.monkey import Monkey
from psychopy.tests.test_experiment.test_components.test_base_components import BaseComponentTests, _TestLibraryClassMixin

class TestSliderMonkeyComponent(BaseComponentTests, _TestLibraryClassMixin):
    """
    Basic Component tests
    """
    comp = SliderMonkeyComponent
    libraryClass = Monkey
