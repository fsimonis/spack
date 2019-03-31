# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install seissol
#
# You can edit this file again by typing:
#
#     spack edit seissol
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Seissol(SConsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.seissol.org"
    url      = "https://github.com/SeisSol/SeisSol"
    #git      = "https://github.com/SeisSol/SeisSol.git"

    # FIXME: Add proper versions and checksums here.
    version('master', branch='master', submodules=True)

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on('python@2.7:')
    depends_on('hdf5~shared+mpi+fortran+threadsafe')
    depends_on('netcdf+mpi~shared')
    depends_on('mpi')
    depends_on('parmetis')
    depends_on('libxsmm')
    depends_on('cmake')

    def patch(self):
        """ We need to setup the configuration by patching build/options/supermuc_mac_cluster.py """
        optsfile=os.path.join(self.package_dir, "build", "options", "supermuc_mac_cluster")
        filter_file(r"^arch.\+", r"arch  = '{}'".format(self.arch), optsfile)

        if self.debug:
            filter_file(r"^compileMode.\+", r"compileMode='debug'", optsfile)


    def build_args(self, spec, prefix):
        # FIXME: Add arguments to pass to build.
        # FIXME: If not needed delete this function
        args = []
        args.append("buildVariablesFile=build/options/supermuc_mac_cluster.py")
        return args
