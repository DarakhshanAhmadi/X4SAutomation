import pytest
from CommonUtilities.logGeneration import LogGenerator


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    logger = LogGenerator.logGen()

