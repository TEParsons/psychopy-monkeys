from psychopy.tests.utils import profiledImport


def test_component_import():
    """
    Test that Components can be imported in good time and without touching costly packages.
    """
    for ref in [
        "psychopy_monkeys.components.buttonBoxMonkey",
        "psychopy_monkeys.components.buttonMonkey",
        "psychopy_monkeys.components.enderMonkey",
        "psychopy_monkeys.components.keyboardMonkey",
        "psychopy_monkeys.components.mouseMonkey",
        "psychopy_monkeys.components.skipMonkey",
        "psychopy_monkeys.components.sliderMonkey",
    ]:
        profiledImport(
            ref=ref,
            notouch=[
                "psychopy.visual",
                "psychopy.hardware",
                "psychopy.sound"
            ]
        )
