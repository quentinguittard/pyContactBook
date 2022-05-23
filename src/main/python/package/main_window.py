from PySide2 import QtWidgets, QtGui

# from package.api.note import Note, get_notes


class MainWindow(QtWidgets.QMainWindow):
    """This is a class to create the window of the application."""

    def __init__(self, ctx):
        """The constructor of the window.

        :param ctx: The context of the application.
        :type ctx: ApplicationContext
        """
        super().__init__()
        self.ctx = ctx
        self.setWindowTitle("PyContactBook")
        self.setup_ui()
        # self.populate_notes()

    def setup_ui(self):
        """Setup the user interface of the application."""
        self.create_widgets()
        self.create_layouts()
        self.modify_widgets()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        """Create the widgets of the application."""
        main_menu = self.menuBar()
        self.file_menu = main_menu.addMenu('File')
        self.contact_menu = main_menu.addMenu('Contact')
        self.__create_actions()
        self.__add_actions()

        self.contact_widget = QtWidgets.QWidget()
        self.lw_contact = QtWidgets.QListWidget()

        self.form_widget = QtWidgets.QWidget()
        self.gb_form = QtWidgets.QGroupBox("New Contact")
        self.le_first_name = QtWidgets.QLineEdit()
        self.le_last_name = QtWidgets.QLineEdit()
        self.le_job = QtWidgets.QLineEdit()
        self.le_city = QtWidgets.QLineEdit()
        self.le_birthday = QtWidgets.QLineEdit()
        self.le_email = QtWidgets.QLineEdit()
        self.le_phone = QtWidgets.QLineEdit()
        self.le_facebook = QtWidgets.QLineEdit()
        self.le_instagram = QtWidgets.QLineEdit()
        self.te_notes = QtWidgets.QTextEdit()

        self.pb_save = QtWidgets.QPushButton("Save Contact")

    def __create_actions(self):
        # File actions
        self.new_action = QtWidgets.QAction("&New", self)
        self.new_action.setShortcut("Ctrl+N")
        self.open_action = QtWidgets.QAction("&Open...", self)
        self.open_action.setShortcut("Ctrl+O")
        self.save_action = QtWidgets.QAction("&Save", self)
        self.save_action.setShortcut("Ctrl+S")

        # Contact actions
        self.add_action = QtWidgets.QAction("&Add", self)
        self.add_action.setShortcut("Ctrl+A")
        self.delete_action = QtWidgets.QAction("&Delete", self)
        self.delete_action.setShortcut("Ctrl+D")
        self.edit_action = QtWidgets.QAction("&Edit", self)
        self.edit_action.setShortcut("Ctrl+E")
        self.filter_action = QtWidgets.QAction("Filter", self)

    def __add_actions(self):
        # File menu
        self.file_menu.addAction(self.new_action)
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.save_action)
        # Contact menu
        self.contact_menu.addAction(self.add_action)
        self.contact_menu.addAction(self.delete_action)
        self.contact_menu.addAction(self.edit_action)
        self.contact_menu.addAction(self.filter_action)

    def modify_widgets(self):
        """Apply a CSS style sheet to the user interface of the application."""
        # css_file = self.ctx.get_resource("style.css")
        # with open(css_file, "r") as f:
        #     self.setStyleSheet(f.read())

    def create_layouts(self):
        """Create the grid layout of the user interface."""
        self.contact_layout = QtWidgets.QHBoxLayout(self)
        self.fw_layout = QtWidgets.QVBoxLayout(self)
        self.form_layout = QtWidgets.QFormLayout(self)
        self.form_layout.addRow(QtWidgets.QLabel("First Name"), self.le_first_name)
        self.form_layout.addRow(QtWidgets.QLabel("Last Name"), self.le_last_name)
        self.form_layout.addRow(QtWidgets.QLabel("Job"), self.le_job)
        self.form_layout.addRow(QtWidgets.QLabel("City"), self.le_city)
        self.form_layout.addRow(QtWidgets.QLabel("Birthday"), self.le_birthday)
        self.form_layout.addRow(QtWidgets.QLabel("Email"), self.le_email)
        self.form_layout.addRow(QtWidgets.QLabel("Phone"), self.le_phone)
        self.form_layout.addRow(QtWidgets.QLabel("Facebook"), self.le_facebook)
        self.form_layout.addRow(QtWidgets.QLabel("Instagram"), self.le_instagram)
        self.form_layout.addRow(QtWidgets.QLabel("Notes"), self.te_notes)

    def add_widgets_to_layouts(self):
        """Add created widgets to the user interface layout."""
        self.fw_layout.addWidget(self.gb_form)
        self.fw_layout.addWidget(self.pb_save)
        self.contact_layout.addWidget(self.lw_contact)
        self.contact_layout.addWidget(self.form_widget)

        self.gb_form.setLayout(self.form_layout)
        self.form_widget.setLayout(self.fw_layout)
        self.contact_widget.setLayout(self.contact_layout)

        self.setCentralWidget(self.contact_widget)

    def setup_connections(self):
        """Setup the connections between the widgets and their functions."""
        # self.te_content.textChanged.connect(self.save_note)
        # self.lw_contact.itemSelectionChanged.connect(self.populate_note_content)
        # QtWidgets.QShortcut(QtGui.QKeySequence("Backspace"), self.lw_contact, self.delete_selected_note)

    # END UI
    #
    # def add_note_to_listwidget(self, note):
    #     """Add a note to the list.
    #
    #     :param note: A note object.
    #     :type note: Note
    #     """
    #     lw_item = QtWidgets.QListWidgetItem(note.title)
    #     lw_item.note = note
    #     self.lw_contact.addItem(lw_item)
    #
    # def create_note(self):
    #     """Create a note."""
    #     title, result = QtWidgets.QInputDialog.getText(self, "Add a note", "Title: ")
    #     if result and title:
    #         note = Note(title=title)
    #         note.save()
    #         self.add_note_to_listwidget(note)
    #
    # def delete_selected_note(self):
    #     """Delete a selected note from the note list."""
    #     selected_item = self.get_selected_lw_item()
    #     if selected_item:
    #         result = selected_item.note.delete()
    #         if result:
    #             self.lw_contact.takeItem(self.lw_contact.row(selected_item))
    #
    # def get_selected_lw_item(self):
    #     """Get the first selected note.
    #
    #     :return: The first item of the selection or None if there is no selection.
    #     :rtype: QListWidgetItem or None
    #     """
    #     selected_items = self.lw_contact.selectedItems()
    #     if selected_items:
    #         return selected_items[0]
    #     return None
    #
    # def populate_notes(self):
    #     """Populate the note list with the notes found in the notes directory."""
    #     notes = get_notes()
    #     for note in notes:
    #         self.add_note_to_listwidget(note)
    #
    # def populate_note_content(self):
    #     """Populate note content in the user interface from a selected note."""
    #     selected_item = self.get_selected_lw_item()
    #     if selected_item:
    #         self.te_content.setText(selected_item.note.content)
    #     else:
    #         self.te_content.clear()
    #
    # def save_note(self):
    #     """Save the content of the selected note."""
    #     selected_item = self.get_selected_lw_item()
    #     if selected_item:
    #         selected_item.note.content = self.te_content.toPlainText()
    #         selected_item.note.save()
