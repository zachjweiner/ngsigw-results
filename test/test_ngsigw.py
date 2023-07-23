__license__ = """
ngsigw-results

Written in 2023 by Zachary J Weiner

To the extent possible under law, the author(s) have dedicated all copyright
and related and neighboring rights to this software to the public domain
worldwide. This software is distributed without any warranty.

You should have received a copy of the CC0 Public Domain Dedication along with
this software. If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.
"""


from ngsigw_results import (
    monochromatic, log_normal, broken_power_law, power_law_exp_cutoff
)
import pytest

all_results = (
    (monochromatic,)
    + tuple(log_normal.values())
    + tuple(broken_power_law.values())
    + tuple(power_law_exp_cutoff.values())
)


@pytest.mark.parametrize("result", all_results)
def test_ngsigw_result(result):
    _ = result.omega_gw(1e-3, 10)
    _ = result.omega_gw_gaussian(1e-3, 10)
    _ = result.omega_gw_F_NL_2(1e-3, 10)
    _ = result.omega_gw_F_NL_4(1e-3, 10)
