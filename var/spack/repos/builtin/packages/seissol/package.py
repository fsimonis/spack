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
    git      = "https://github.com/SeisSol/SeisSol.git"

    version('master', branch='master', submodules=True)

    variant('order', default='2', description='convergence order of the ADER-DG method', values=('2', '3', '4', '5', '6', '7', '8'), multi=False)
    variant('mpi', default=True)
    variant('openmp', default=True)
    variant('precision', default='d', values=('s', 'd'), description='Floating point precision to use.')
    variant('arch', default='dnoarch', values=('snoarch', 'dnoarch', 'swsm', 'dwsm', 'ssnb', 'dsnb', 'sknc', 'dknc', 'shsw', 'dhsw', 'sknl', 'dknl', 'sskx', 'dskx'), multi=True)
    variant('asagi', default=True, description="use asagi for material input")

    depends_on('python@2.7:')
    depends_on('parmetis')
    depends_on('libxsmm')
    depends_on('cmake')
    depends_on('memkind')
    depends_on('mpi', when="+mpi")
    depends_on('hdf5 +shared +fortran ~mpi', when="~mpi")
    depends_on('hdf5 +shared +fortran +mpi', when="+mpi")
    depends_on('netcdf +shared ~mpi', when="~mpi")
    depends_on('netcdf +shared +mpi', when="+mpi")
    depends_on('asagi ~mpi', when="+asagi ~mpi")
    depends_on('asagi +mpi', when="+asagi +mpi")
            
    def build_args(self, spec, prefix):
        import os
        args = []
        #  args.append("buildVariablesFile=build/options/supermuc_mac_cluster.py")
        if "+debug" in spec:
            args.append("compileMode=debug")
        else:
            args.append("compileMode=release")

        if "+mpi" in spec and "+openmp" in spec:
            args.append("parallelization=hybrid")
        elif "+mpi" in spec:
            args.append("parallelization=mpi")
        elif "+openmp" in spec:
            args.append("parallelization=omp")
        else:
            args.append("parallelization=none")

        args.append("arch={}".format(spec.variants["arch"].value[0]))
        args.append("order={}".format(spec.variants["order"].value[0]))
        args.append("memkindDir={}".format(os.path.join(spec['memkind'].prefix, "lib")))
        args.append("netcdf=yes")
        args.append("netcdfDir={}".format(os.path.join(spec['netcdf'].prefix, "lib")))
        args.append("hdf5=yes")
        args.append("hdf5Dir={}".format(os.path.join(spec['hdf5'].prefix, "lib")))
        args.append("metis=yes")
        args.append("metisDir={}".format(os.path.join(spec['metis'].prefix, "lib")))
        return args
