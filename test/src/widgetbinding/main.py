# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import sys
import os
from PySide6.QtWidgets import QApplication
 # Add the directory containing the wiggly module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from dialog import Dialog

if __name__ == "__main__":
    app = QApplication()
    w = Dialog()
    w.show()
    sys.exit(app.exec())
