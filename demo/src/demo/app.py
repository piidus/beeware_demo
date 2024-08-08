"""
First Testing Project
"""


import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import os

class Demo(toga.App):
    def startup(self):
        # Main window
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Dropdown menu for navigation
        self.dropdown = toga.Selection(items=["Sign In", "Picture View", "Map View"], on_change=self.on_dropdown_select)
        
        # Main box
        self.main_box = toga.Box(style=Pack(direction=COLUMN))

        # Add dropdown to main box
        self.main_box.add(self.dropdown)

        # Set the initial view
        self.current_view = toga.Box(style=Pack(direction=COLUMN))
        self.main_box.add(self.current_view)
        self.show_sign_in()

        # Set the main window content
        self.main_window.content = self.main_box
        self.main_window.show()

    def on_dropdown_select(self, widget):
        selection = widget.value
        if selection == "Sign In":
            self.show_sign_in()
        elif selection == "Picture View":
            self.show_picture_view()
        elif selection == "Map View":
            self.show_map_view()

    def show_sign_in(self):
        self.clear_current_view()
        self.__username_input = toga.TextInput(placeholder='Username', style=Pack(padding=10, width=200))
        password_input = toga.PasswordInput(placeholder='Password', style=Pack(padding=10, width=200))
        login_button = toga.Button('Login', on_press=self.on_login, style=Pack(padding=10))
        
        self.current_view.add(self.__username_input)
        self.current_view.add(password_input)
        self.current_view.add(login_button)

    def show_picture_view(self):
        self.clear_current_view()
        
        picture = toga.ImageView(toga.Image("logo.jpg"),id='view', style=Pack(width=300, height=300))
        self.current_view.add(picture)

    def show_map_view(self):
        self.clear_current_view()
        # For simplicity, using a placeholder for the map view. Integrating an actual map requires a more complex setup.
        map_placeholder = toga.Label("Map View Placeholder", style=Pack(padding=10))
        self.current_view.add(map_placeholder)

    def on_login(self, widget):
        # Handle login logic
        if self.__username_input.value :
            self.main_window.info_dialog("Login", "Login successful"+ " "+ self.__username_input.value)
        else:
            self.main_window.info_dialog("Login", "Login failed")

    def clear_current_view(self):
        for child in self.current_view.children:
            self.current_view.remove(child)

def main():
    return Demo()

if __name__ == '__main__':
    main().main_loop()



# import toga
# from toga.style import Pack
# from toga.style.pack import COLUMN, ROW


# class Demo(toga.App):
#     def startup(self):
#         """Construct and show the Toga application.

#         Usually, you would add your application to a main content box.
#         We then create a main window (with a name matching the app), and
#         show the main window.
#         """
#         main_box = toga.Box()

#         self.main_window = toga.MainWindow(title=self.formal_name)
#         self.main_window.content = main_box
#         self.main_window.show()


# def main():
#     return Demo()
