# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
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
#     spack install spooles
#
# You can edit this file again by typing:
#
#     spack edit spooles
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os


class Spooles(MakefilePackage):
    """
    SPOOLES is a library for solving sparse real and complex linear systems of equations, written in the C language using object oriented design.
    """

    homepage = "http://www.netlib.org/linalg/spooles"
    url      = "http://www.netlib.org/linalg/spooles/spooles.2.2.tgz"

    version('2.2', sha256='a84559a0e987a1e423055ef4fdf3035d55b65bbe4bf915efaa1a35bef7f8c5dd')

    patch('spooles.patch')
    build_targets = ['lib']

    def install(self, spec, prefix):
        # Install libraries
        mkdir(prefix.lib)
        for lib  in find('.', 'libspooles.*', recursive=False):
            install(lib, prefix.lib)

        # Install headers
        includeDir = join_path(prefix.include, 'spooles')
        mkdirp(includeDir)
        for header in find('.', '*.h', recursive=False):
            # MPI is currently not supported
            if "MPI.h" in header:
                continue
            install(header, includeDir)
            # Some headers have a subtree associated to them.
            # This detects and installs them.
            partDir = os.path.splitext(header)[0]
            if os.path.isdir(partDir):
                partName = os.path.basename(partDir)
                partInstallDir = join_path(includeDir, partName)
                mkdir(partInstallDir)
                for partHeader in find(partDir, '*.h'):
                    install(partHeader, partInstallDir)

