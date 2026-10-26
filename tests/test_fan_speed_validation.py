import unittest

import esphome.config_validation as cv
from esphome.const import CONF_MAX_VALUE, CONF_MIN_VALUE, CONF_SPEED, CONF_STEP

from components.miot.fan import validate_speed_range


class FanSpeedValidationTest(unittest.TestCase):
    def validate(self, minimum, maximum, step):
        config = {CONF_SPEED: {CONF_MIN_VALUE: minimum, CONF_MAX_VALUE: maximum, CONF_STEP: step}}
        return validate_speed_range(config)

    def test_valid_ranges(self):
        self.assertIsNotNone(self.validate(1, 3, 1))
        self.assertIsNotNone(self.validate(300, 2300, 10))
        self.assertIsNotNone(self.validate(0, 0, 1))

    def test_rejects_zero_step(self):
        with self.assertRaisesRegex(cv.Invalid, "step"):
            self.validate(1, 3, 0)

    def test_rejects_reversed_range(self):
        with self.assertRaisesRegex(cv.Invalid, "min_value"):
            self.validate(3, 1, 1)


if __name__ == "__main__":
    unittest.main()
