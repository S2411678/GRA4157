import pytest
from example import double 
def test_double():
    assert double(2)==4
    assert double(3+4j)==6+8j
    assert double((1,2))==(1,2,1,2)
    assert double([1,2])==[1,2,1,2]
    assert double("hello")=="hellohello"

""" @pytest.mark.parametrize("x,expected_value",[(2,4),("hello","hellohello"),((1,2),(1,2,1,2)),([1,2],[1,2,1,2]),(3+4j,6+8j)])
def test_double(x,expected_value):
    assert double(x)==expected_value """ #assert #pytest test__ -v

from math import sqrt
from example import pathlength
def test_pathlength():
    assert pathlength((0,3,6),(0,4,8))==10
    assert pathlength((5,10,15),(12,24,36))==26

def test_linalg():
    import numpy as np
    n=4
    A=np.random.rand(n,n)
    B=np.random.rand(n,n)
    C=np.random.rand(n,n)
    
    tolerance=1E-14
    
    assert np.allclose(A+B,B+A,atol=tolerance)
    assert np.allclose((A@B)@C,A@(B@C),atol=tolerance)
    assert np.linalg.matrix_rank(A)==np.linalg.matrix_rank(np.matrix_transpose(A))
    assert abs(np.linalg.det(A@B)-np.linalg.det(A)*np.linalg.det(B))<tolerance
    assert np.allclose(np.linalg.eigvals(A),np.linalg.eigvals(np.matrix_transpose(A)),atol=tolerance)