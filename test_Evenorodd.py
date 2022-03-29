import pytest
import evenorodd

@pytest.mark.parametrize("a,res",[(10,True),(7,True),(12,True)])
def test_EvenorOdd(a,res):
    result = evenorodd.Evenoradd(a)
    assert result == res