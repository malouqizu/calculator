import os

def StabilityTest(TIMES):
    for i in range(0, TIMES):
        n = i + 1
        print('Test Round : ' + str(n))
        script = os.getcwd() + r'\test_v7_runner.py'
        cmd = 'python ' + script
        os.system(cmd)
        print('\n')

if __name__ == '__main__':
    StabilityTest(100)
    os.system('pause')
