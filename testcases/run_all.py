__author__ = 'Administrator'
import pytest
import os
if __name__ == '__main__':
    pytest.main(['-vs'])
    os.system('allure generate ../temp -o ../report --clean')