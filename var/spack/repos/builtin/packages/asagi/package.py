# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Asagi(CMakePackage):
    """a pArallel Server for Adaptive GeoInformation."""

    homepage = "https://github.com/TUM-I5/ASAGI"
    git      = "https://github.com/TUM-I5/ASAGI.git"

    version('master', branch='master', submodules=True)

    variant('mpi',           default=True, description='Use MPI')
    variant('shared',        default=True, description='Build shared libraries')
    variant('threadsafe',    default=True, description='Enable thread-safe interface')
    variant('maxdimensions', default=4,    values=int, description='Maximum number of dimensions.')
    variant('fortran',       default=True, description='Enable Fortran support')

    depends_on('mpi', when="+mpi")
    depends_on('netcdf +shared +mpi', when="+shared +mpi")
    depends_on('netcdf +shared ~mpi', when="+shared ~mpi")
    depends_on('netcdf ~shared +mpi', when="~shared +mpi")
    depends_on('netcdf ~shared ~mpi', when="~shared ~mpi")
    depends_on('cmake@2.8:')

    def cmake_args(self):
        spec = self.spec
        cmake_args = []
        if "+shared" in spec:
            cmake_args.append('-DBUILD_SHARED_LIBS=ON')
        else:
            cmake_args.append('-DSHARED_LIB=OFF')
            cmake_args.append('-DSTATIC_LIB=ON')

        if "+fortran" in spec:
            cmake_args.append('-DFORTRAN_SUPPORT=ON')

        if "~threadsafe" in spec:
            cmake_args.append('-DTHREADSAFE=OFF')

        cmake_args.append(
            '-DMAX_DIMENSIONS=' + str(spec.variants['maxdimensions'].value))

        return cmake_args
