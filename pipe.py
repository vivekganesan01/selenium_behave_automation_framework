import os
import subprocess

class Pipe:

    ENV_VARS = ['TEST_ENV', 'TAGS']
    _test_env = os.environ['TEST_ENV'] if not os.environ['TEST_ENV'] else 'UAT'
    _tags = os.environ['TAGS'] if not os.environ['TAGS'] else None
    command_Sh = ""

    def test(self):
        global command_Sh, _tags, _test_env
        print("Tag name : {}".format(_tags))
        print("Test env : {}".format(_test_env))
        if _tags is None:
            command_Sh = "-D instance={} feature".format(_test_env.strip())
        else:
            command_Sh = "-D instance={} --tags={} feature".format(_test_env.strip(),_tags.strip())
        return command_Sh

if  __name__ == '__main__':
    p = Pipe()
    print(p.test())
    print("------")
    subprocess.call(['./runner_allure.sh',p.test()])

