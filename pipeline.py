import os
class Pipeline:
     #ENV_VARS = ['TEST_ENV', 'TAGS', 'FEATURE']
     #_test_env = os.environ['TEST_ENV'] if not os.environ['TEST_ENV'] else 'UAT'
     #_tags = os.environ['TAGS'] if not os.environ['TAGS'] else None
     #_feature_file = os.environ['FEATURE'] if not os.environ['FEATURE'] else '.'
    # _test_env = "UAT"
     #tags = "dev"
    # _feature_file = '.'
     command_Sh = ""
     def test(self,_test_env,_tags,_feature_file):
        global command_Sh
        if _tags is None and _feature_file is '.':
             command_Sh = "./behave -D instance={} feature".format(_test_env.strip())
        if _tags is None and _feature_file is not '.':
             command_Sh = "./behave -D instance={} feature/{}".format(_test_env.strip(),_feature_file.strip())
        if _tags is not None and _feature_file is '.':
             command_Sh = "./behave -D instance={} --tags={} feature".format(_test_env.strip(), _tags.strip())
        if _tags is not None and _feature_file is not '.' and _tags is not None:
             command_Sh = "./behave -D instance={} --tags={} feature/{}".format(_test_env.strip(),_tags.strip(),_feature_file.strip())
        else:
            command_Sh = "./behave"
        return command_Sh

p = Pipeline()
print(p.test("DEV","unittest","f.feature"))


