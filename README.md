# Research Notes
A repo to keep my research notes, links to papers, repos etc.

## Reasoning capabilities of LLMs

This is where the current generation of LLMs fail the most. 
Could more training or larger but similar models solve this problems?
An architectural change in the neural network might be required for a major improvement.

* https://arxiv.org/abs/2311.12983
* https://arxiv.org/pdf/2311.09247
* https://towardsdatascience.com/solving-reasoning-problems-with-llms-in-2023-6643bdfd606d
* https://x.com/ylecun/status/1738934781692309946
* https://arxiv.org/pdf/2405.19616
* https://arxiv.org/html/2406.02061v1


## Structure generators

* PackMol: https://m3g.github.io/packmol/
    Fortran code, julia wrapper, conda package available
* MDAPackMol: https://github.com/MDAnalysis/MDAPackmol
    MDAnalysis wrapper, last updated in 2018. Example fails with:
    ```
    ValueError                                Traceback (most recent call last)
Cell In[1], line 23
     10 system = mdapackmol.packmol(
     11     [mdapackmol.PackmolStructure(
     12         water, number=1000,
   (...)
     16         instructions=['inside box 0. 0. 0. 40. 40. 40.'])]
     17 )
     19 # the returned system is a MDAnalysis Universe
     20 # with all topology information from building blocks retained
     21 # which can then be saved into any format
     22 # eg to Lammps data file:
---> 23 system.atoms.write('topology.data')

File ~/venv/chemmat/lib/python3.10/site-packages/MDAnalysis/core/groups.py:3567, in AtomGroup.write(self, filename, file_format, filenamefmt, frames, **kwargs)
   3565 with writer(filename, n_atoms=self.n_atoms, **kwargs) as w:
   3566     if frames is None:
-> 3567         w.write(self.atoms)
   3568     else:
   3569         current_frame = trj.ts.frame

File ~/venv/chemmat/lib/python3.10/site-packages/MDAnalysis/core/groups.py:4648, in requires.<locals>.require_dec.<locals>.check_args(*args, **kwargs)
   4641         if missing:
   4642             raise NoDataError(
   4643                 "{funcname} failed. "
   4644                 "AtomGroup is missing the following required "
   4645                 "attributes: {attrs}".format(
   4646                     funcname=func.__name__,
   4647                     attrs=', '.join(missing)))
-> 4648 return func(*args, **kwargs)

File ~/venv/chemmat/lib/python3.10/site-packages/MDAnalysis/coordinates/LAMMPS.py:412, in DATAWriter.write(self, selection, frame)
    409 except ValueError:
    410     errmsg = ("LAMMPS.DATAWriter: atom types must be convertible to "
    411               "integers")
--> 412     raise ValueError(errmsg) from None
    414 try:
    415     velocities = atoms.velocities

ValueError: LAMMPS.DATAWriter: atom types must be convertible to integers
4096
```

* TurtleMol https://github.com/Dfilono/TurtleMol

* ASE build: https://wiki.fysik.dtu.dk/ase/ase/build/build.html