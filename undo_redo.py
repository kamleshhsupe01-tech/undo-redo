class TextEditor:
    def __init__(self):
        self.doc = ""
        self.undo = []
        self.redo = []

    def change(self, text):
        self.undo.append(self.doc)
        self.doc += text
        self.redo.clear()
        print("Changed:", self.doc)

    def undo_action(self):
        if self.undo:
            self.redo.append(self.doc)
            self.doc = self.undo.pop()
            print("Undo:", self.doc)
        else:
            print("Nothing to undo")

    def redo_action(self):
        if self.redo:
            self.undo.append(self.doc)
            self.doc = self.redo.pop()
            print("Redo:", self.doc)
        else:
            print("Nothing to redo")

    def run(self):
        while True:
            choice = input("1-Change 2-Undo 3-Redo 4-Show 5-Exit: ")
            if choice == '1':
                self.change(input("Add text: "))
            elif choice == '2':
                self.undo_action()
            elif choice == '3':
                self.redo_action()
            elif choice == '4':
                print("Doc:", self.doc)
            elif choice == '5':
                break
            else:
                print("Invalid")

TextEditor().run()
