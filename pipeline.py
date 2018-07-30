import os
import subprocess

class Pipeline:

    def __init__(self):
        self.ENV_VARS = ['TEST_ENV', 'TAGS']
        self._test_env = os.environ['TEST_ENV'] if 'TEST_ENV' in os.environ else 'UAT'
        self._tags = os.environ['TAGS'] if os.environ['TEST_ENV'] is not "none" else None
        self.command_Sh = ""

    def test(self):
        print("Tag name : {}".format(self._tags))
        print("Test env : {}".format(self._test_env))
        if self._tags is None:
            command_Sh = "-D instance={} feature".format(self._test_env.strip())
        else:
            command_Sh = "-D instance={} --tags={} feature".format(self._test_env.strip(),self._tags.strip())
        return command_Sh

if  __name__ == '__main__':
    p = Pipeline()
    print(p.test())
    print("------")
    subprocess.call(['./runner_allure.sh',p.test()])

