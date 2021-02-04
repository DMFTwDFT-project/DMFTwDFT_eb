#!/usr/bin/env python
import VASP
import Struct

if __name__ == '__main__':

  p = {"Niter":     1,               # Number of DFT+DMFT iterations
     "atomnames": ['Ni'],       # The name of atoms"],
     "orbs"     : ['d'],       # The name  of orbitals
     "L_rot"     : [1],       # Whether rotate local axis or not
     "ewin":      [-8.1,3.2],           # Energy Window
     "cor_at":    [['Ni1','Ni2']],      # Correlated atoms, put degenerate atoms in the same list
     "cor_orb":   [[['d_z2','d_xz']]], # DMFT orbitals, other orbitals are treated by HF"],
  }
  TB=Struct.TBstructure('POSCAR',p['atomnames'],p['orbs'])
  TB.Compute_cor_idx(p['cor_at'],p['cor_orb'])
  print TB.TB_orbs
  DFT=VASP.VASP_class()
  DFT.NBANDS=28
  DFT.Create_win(TB,p['atomnames'],p['orbs'],p['L_rot'],DFT.NBANDS,DFT.EFERMI+p['ewin'][0],DFT.EFERMI+p['ewin'][1])
