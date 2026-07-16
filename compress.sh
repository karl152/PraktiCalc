#!/bin/sh

# PraktiCalc © 2024-2026 Karl Wesseler
# Licensed under the GNU General Public License v3.0.
# See https://www.gnu.org/licenses/gpl-3.0.txt for details.
# SPDX-License-Identifier: GPL-3.0-only

read -p "PraktiCalc Version: " PraktiCalcVersion
rm build/prakticalc-$PraktiCalcVersion-source.pax.xz
pax -w . | xz -v -T0 -9e > ../prakticalc-source.pax.xz
mkdir -v build
mv -v ../prakticalc-source.pax.xz build/prakticalc-$PraktiCalcVersion-source.pax.xz
echo "Done!"
