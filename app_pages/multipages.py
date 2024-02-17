import streamlit as st

class MultiPage:
    """
    Class for generating multiple Streamlit pages using an object-oriented approach.
    """

    def __init__(self, app_name: str) -> None:
        """
        Constructor for the MultiPage class.
        
        :param app_name: Title of the Streamlit app.
        """
        self.pages = []
        self.app_name = app_name

        # Configure the page with a title and icon.
        st.set_page_config(page_title=self.app_name, page_icon="🏘️")
    
    def add_page(self, title: str, func) -> None:
        """
        Add a new page to the Streamlit app.

        :param title: Title of the page.
        :param func: Python function to render the page.
        """
        if callable(func):
            self.pages.append({"title": title, "function": func})
        else:
            raise ValueError("The page function must be callable.")

    def run(self):
        """
        Run the Streamlit app and render pages based on user selection.
        """
        # Display the app name as the main title
        st.title(self.app_name)

        # If no pages are added, display a message
        if not self.pages:
            st.error("No pages available. Please add pages to the app.")
            return

        # Sidebar for navigation
        with st.sidebar:
            st.title("Navigation")
            page = st.radio('Go to', self.pages, format_func=lambda page: page['title'])

        # Execute the render function of the selected page
        page['function']()