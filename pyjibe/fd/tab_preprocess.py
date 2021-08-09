import pkg_resources

from nanite.preproc import IndentationPreprocessor
from PyQt5 import uic, QtCore, QtWidgets

from .widget_preprocess_item import WidgetPreprocessItem


class TabPreprocess(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(TabPreprocess, self).__init__(*args, **kwargs)
        path_ui = pkg_resources.resource_filename("pyjibe.fd",
                                                  "tab_preprocess.ui")
        uic.loadUi(path_ui, self)

        # Setup everything necessary for the preprocessing tab:
        # Get list of preprocessing methods
        premem = IndentationPreprocessor.available()

        self._map_widgets_to_preproc_ids = {}
        for pid in premem:
            pwidget = WidgetPreprocessItem(identifier=pid, parent=self)
            self._map_widgets_to_preproc_ids[pwidget] = pid
            self.layout_preproc_area.addWidget(pwidget)
            pwidget.stateChanged.connect(self.check_selection)
            if pid == "correct_tip_offset":
                idx = pwidget.comboBox.findData("deviation_from_baseline")
                pwidget.comboBox.setCurrentIndex(idx)
        spacer_item = QtWidgets.QSpacerItem(20, 0,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.layout_preproc_area.addItem(spacer_item)

        # Add recommended item (see `self.preproc_set_preset`)
        self.cb_preproc_presel.addItem("Recommended")
        self.cb_preproc_presel.activated.connect(self.on_preset_changed)
        self.cb_preproc_presel.currentIndexChanged.connect(
            self.on_preset_changed)
        # Apply recommended defaults
        self.cb_preproc_presel.setCurrentIndex(1)

    @QtCore.pyqtSlot(int)
    def check_selection(self, state):
        """If the user selects an item, make sure requirements are checked"""
        sender = self.sender()
        if sender in self._map_widgets_to_preproc_ids:
            pid = self._map_widgets_to_preproc_ids[sender]
            if state == 2:
                # Enable all steps that this step here requires
                req_stps = IndentationPreprocessor.get_require_steps(pid)
                if req_stps:
                    for pwid in self._map_widgets_to_preproc_ids:
                        if self._map_widgets_to_preproc_ids[pwid] in req_stps:
                            pwid.setChecked(True)
            if state == 0:
                # Disable all steps that depend on this one
                for dwid in self._map_widgets_to_preproc_ids:
                    did = self._map_widgets_to_preproc_ids[dwid]
                    req_stps = IndentationPreprocessor.get_require_steps(did)
                    if req_stps and pid in req_stps:
                        dwid.setChecked(False)

    def current_preprocessing(self):
        # Note: Preprocessing is cached once in `fdist`.
        # Thus calling this method a second time without any
        # change in the GUI is free.
        identifiers = []
        options = {}
        for pwidget in self._map_widgets_to_preproc_ids:
            pid = self._map_widgets_to_preproc_ids[pwidget]
            if pwidget.isChecked():
                identifiers.append(pid)
                popts = pwidget.get_options()
                if popts:
                    options[pid] = popts
        # Make sure the order is correct
        identifiers = IndentationPreprocessor.autosort(identifiers)
        return identifiers, options

    def fit_apply_preprocessing(self, fdist):
        """Apply the preprocessing steps if required"""
        identifiers, options = self.current_preprocessing()
        # Perform preprocessing
        fdist.apply_preprocessing(identifiers, options=options)

    @QtCore.pyqtSlot()
    def on_preset_changed(self):
        """Update preselection"""
        text = self.cb_preproc_presel.currentText()
        if text == "None":
            used_methods = []
        elif text == "Recommended":
            used_methods = ["compute_tip_position",
                            "correct_force_offset",
                            "correct_tip_offset",
                            "correct_split_approach_retract"]
        else:
            raise ValueError(f"Unknown text '{text}'!")

        for pwidget in self._map_widgets_to_preproc_ids:
            pid = self._map_widgets_to_preproc_ids[pwidget]
            pwidget.setChecked(pid in used_methods)

    def set_preprocessing(self, preprocessing, options=None):
        """Set preprocessing (mostly used for testing)"""
        if options is None:
            options = {}
        for pwidget in self._map_widgets_to_preproc_ids:
            pid = self._map_widgets_to_preproc_ids[pwidget]
            pwidget.setChecked(pid in preprocessing)
            if pid in options:
                opts = options[pid]
                key = sorted(opts.keys())[0]  # not future-proof
                idx = pwidget.comboBox.findData(opts[key])
                pwidget.comboBox.setCurrentIndex(idx)
