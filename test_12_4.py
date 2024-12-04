import logging
import unittest
from rt_with_exceptions import Runner

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='runner_tests.log',
    encoding='utf-8',
)


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        try:
            runner = Runner("Усэйн", -10)
            runner.walk()
            logging.info("""test_walk выполнен успешно""")
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)

    def test_run(self):
        try:
            runner = Runner(12345, 10)
            runner.run()
            logging.info("""test_run выполнен успешно""")
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)


if __name__ == "__main__":
    unittest.main()
