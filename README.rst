ngsigw-results
==============

.. image:: https://zenodo.org/badge/668438090.svg
    :target: https://doi.org/10.5281/zenodo.8176107
.. image:: https://img.shields.io/badge/arXiv-2105.01659-b31b1b.svg
    :target: https://arxiv.org/abs/2105.01659
.. image:: https://img.shields.io/badge/License-CC--0-blue.svg
    :target: http://creativecommons.org/publicdomain/zero/1.0/

This repository makes available the numerical results for gravitational waves induced by non-Gaussian scalar perturbations from `2105.01659 <https://arxiv.org/abs/2105.01659>`_.
Access is implemented as a simple Python package (see ``example.ipynb`` for example usage), but the data is stored in the portable `HDF5 <https://www.hdfgroup.org/solutions/hdf5/>`_ format (``ngsigw_results/data/ngsigw-results.h5``), which has interfaces available in most programming languages.

Simply install with ``pip`` for your preferred ``python`` interpreter:

.. code-block:: bash

    python -m pip install git+https://github.com/zachjweiner/ngsigw-results.git

You can of course clone the repository first and then install.

The data, being "factual" in nature and likely not subject to copyright law, is available under `CC0 <https://creativecommons.org/publicdomain/zero/1.0/>`_.
For convenience, the code itself is also available under CC0.
However, if you use these results please cite both this repository (refer to the `Zenodo archive <https://doi.org/10.5281/zenodo.8176107>`_ or the sidebar on GitHub/``CITATION.cff``) and the original article itself (e.g., with the BibTeX entry `here <https://inspirehep.net/literature/1862163>`_).
