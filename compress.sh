#!/bin/sh

# PraktiCalc © 2024-2026 Karl "karl152"
# Licensed under the GNU General Public License v3.0.
# See https://www.gnu.org/licenses/gpl-3.0.txt for details.
# SPDX-License-Identifier: GPL-3.0

pax -w . | xz -v -T0 -9e > ../prakticalc-source.pax.xz
