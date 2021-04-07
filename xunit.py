class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1
        self.log = 'setUp '

    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + 'testMethod '


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun('testMethod')

    def testRunning(self):
        self.test.run()

    def testSetUp(self):
        self.test.run()
        assert(self.test.wasRun)
        assert('setUp ' == self.test.log)


TestCaseTest('testRunning').run()
TestCaseTest('testSetUp').run()
