class UndoRedoManager:
    def __init__(self):
        self.document = ""
        self.undo_stack = []
        self.redo_stack = []

    def make_change(self, action, pos, text):
        """
        Make a new change to the document.
        action: 'insert' or 'delete'
        pos: position in the document where change occurs
        text: text to insert or delete
        """
        if action == 'insert':
            # Insert text
            self.document = self.document[:pos] + text + self.document[pos:]
            # Push reverse operation to undo stack
            self.undo_stack.append(('delete', pos, text))

        elif action == 'delete':
            # Save deleted text for undo
            deleted_text = self.document[pos:pos + len(text)]
            self.document = self.document[:pos] + self.document[pos + len(text):]
            # Push reverse operation
            self.undo_stack.append(('insert', pos, deleted_text))

        else:
            raise ValueError("Unsupported action. Use 'insert' or 'delete'.")

        # Clear redo stack after any new change
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return

        action, pos, text = self.undo_stack.pop()

        if action == 'insert':
            # Undo means insert text back
            self.document = self.document[:pos] + text + self.document[pos:]
            self.redo_stack.append(('delete', pos, text))

        elif action == 'delete':
            # Undo means delete again
            self.document = self.document[:pos] + self.document[pos + len(text):]
            self.redo_stack.append(('insert', pos, text))

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return

        action, pos, text = self.redo_stack.pop()

        if action == 'insert':
            self.document = self.document[:pos] + text + self.document[pos:]
            self.undo_stack.append(('delete', pos, text))

        elif action == 'delete':
            self.document = self.document[:pos] + self.document[pos + len(text):]
            self.undo_stack.append(('insert', pos, text))

    def display(self):
        print("Current document state:", repr(self.document))


# Example usage
if __name__ == "__main__":
    editor = UndoRedoManager()

    editor.make_change('insert', 0, 'Hello')
    editor.display()

    editor.make_change('insert', 5, ' World')
    editor.display()

    editor.undo()
    editor.display()

    editor.redo()
    editor.display()

    editor.make_change('delete', 5, ' World')
    editor.display()

    editor.undo()
    editor.display()
