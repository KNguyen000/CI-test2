import pytest
from models.ml_models import *


def test_model():
    assert 1 == 1

def test_model_name():
    assert 'Resnet' == 'Resnet'

@pytest.mark.parametrize("test_input", [
    Model("Resnet", 0.9, 0.7),
    Model("Resnet", 0.9, 0.8),
    Model("Resnet", 0.9, 0.8)
])

def test_modelName_str(test_input: Model):
    assert type(test_input.name)==str
    assert test_input.accuracy < 1
    assert test_input.f1 < 1
