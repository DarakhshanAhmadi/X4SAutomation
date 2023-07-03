import pytest

from CommonUtilities.logGeneration import LogGenerator


class BaseTest:
    logger = LogGenerator.logGen()

