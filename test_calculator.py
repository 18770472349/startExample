from unittest import TestCase

from calculator import Calculator

from time import sleep


class TestCalculator(TestCase):
    def test_add(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.add(3, 4), 7)

    def test_multiply(self):
        sleep(0.01)
        self.calculator = Calculator()
        self.assertEqual(self.calculator.multiply(3, 4), 12)


# 使用以下方法中的任意一个运行测试：
#
# 在 Mac 系统中使用 Ctrl+R 键，在 Windows 或 Linux 系统中使用 Shift+F10 键。
# 右键单击背景，选择「Run 『Unittests for test_calculator.py』」。
# 点击测试类名称左侧的绿色小箭头，选择「Run 『Unittests for test_calculator.py』」。
