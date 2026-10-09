import importlib.util
from pathlib import Path
import sys
import unittest
import numpy as np
S=Path(__file__).resolve().parents[1]/'scripts'
sys.path.insert(0,str(S))
class MechanismTests(unittest.TestCase):
 def test_script_exists(self): self.assertTrue((S/'generate_mechanism_examples.py').exists())
 def test_model(self):
  self.assertTrue((S/'generate_mechanism_examples.py').exists(),'model implementation missing')
  import generate_mechanism_examples as m
  self.assertTrue(np.allclose(np.sort(m.poles(.1).real),[-.27-np.sqrt(.23**2-.1**2),-.27+np.sqrt(.23**2-.1**2)]))
  self.assertTrue(np.allclose(m.poles(.25).real,-.27))
  w=np.linspace(-2,2,101)
  self.assertTrue(np.allclose(m.response(w,0,0),1/(.5-1j*w)))
  t=np.linspace(0,80,501); state=m.evolution(t,.1)
  self.assertTrue(np.allclose(state[0],[1,0]))
  total=np.sum(abs(state)**2,axis=1)
  self.assertTrue(np.all(np.diff(total)<=1e-12))
  self.assertTrue(np.allclose(m.evolution(t,0)[:,1],0))
  self.assertTrue(np.allclose(m.evolution(t,0)[:,0],np.exp(-t/2)))
  for omega in [-.3,0,.4]:
   expected=np.linalg.solve(-1j*omega*np.eye(2)-m.generator(.1,.2),[1,0])[0]
   self.assertAlmostEqual(abs(expected-m.response(omega,.2,.1)),0,places=12)
  h=1e-6; derivative=(m.evolution([h],.1)[0]-[1,0])/h
  self.assertTrue(np.allclose(derivative,m.generator(.1)@np.array([1,0]),atol=2e-7))
  for val in [-1,0]:
   with self.assertRaises(ValueError):m.footprint('single',val)
  with self.assertRaises(ValueError):m.footprint('unknown',80)
  self.assertTrue(np.allclose(m.footprint('single',82),(85/25.4,82/25.4)))
  self.assertTrue(np.allclose(m.footprint('double',65),(178/25.4,65/25.4)))
if __name__=='__main__':unittest.main()
