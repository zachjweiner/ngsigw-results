__license__ = """
ngsigw-results

Written in 2023 by Zachary J Weiner

To the extent possible under law, the author(s) have dedicated all copyright
and related and neighboring rights to this software to the public domain
worldwide. This software is distributed without any warranty.

You should have received a copy of the CC0 Public Domain Dedication along with
this software. If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.
"""


from dataclasses import dataclass
from pathlib import Path
import numpy as np
from h5py import File


@dataclass(repr=False)
class NGSIGWResult:
    k: np.ndarray
    gaussian: np.ndarray
    hybrid: np.ndarray
    reducible: np.ndarray
    C: np.ndarray
    Z: np.ndarray
    planar: np.ndarray
    nonplanar: np.ndarray

    @classmethod
    def from_hdf5(cls, grp):
        data = {key: val[()] for key, val in grp.items()}
        return cls(**data)

    def omega_gw_gaussian(self, A_R, F_NL=0):
        return A_R**2 / 48 * self.gaussian

    def omega_gw_F_NL_2(self, A_R, F_NL):
        return A_R**3 * F_NL**2 / 48 * (self.hybrid + self.C + self.Z)

    def omega_gw_F_NL_4(self, A_R, F_NL):
        tot = self.reducible + self.planar + self.nonplanar
        return A_R**4 * F_NL**4 / 48 * tot

    def omega_gw(self, A_R, F_NL):
        return (
            self.omega_gw_gaussian(A_R, F_NL)
            + self.omega_gw_F_NL_2(A_R, F_NL)
            + self.omega_gw_F_NL_4(A_R, F_NL)
        )


with File(Path(__file__).parent / "data/ngsigw-results.h5", "r") as f:
    monochromatic = NGSIGWResult.from_hdf5(f["monochromatic"])
    log_normal = {
        float(key): NGSIGWResult.from_hdf5(val)
        for key, val in f["log-gaussian"].items()
    }
    broken_power_law = {
        tuple(float(x) for x in key.split(",")): NGSIGWResult.from_hdf5(val)
        for key, val in f["broken-power-law"].items()
    }
    power_law_exp_cutoff = {
        float(key): NGSIGWResult.from_hdf5(val)
        for key, val in f["power-law-exp-cutoff"].items()
    }

__all__ = [
    "NGSIGWResult",
    "monochromatic",
    "log_normal",
    "broken_power_law",
    "power_law_exp_cutoff",
]
