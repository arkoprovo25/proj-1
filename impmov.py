from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.slider import Slider

class Movie:
    def __init__(self, title, genre, duration, priority=1, watch_time=None):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.priority = priority
        self.watch_time = watch_time

class MovieManagerApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.movies = []

    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.movie_list_label = Label(text="Movie List")
        layout.add_widget(self.movie_list_label)
        self.movie_list = BoxLayout(orientation='vertical')
        layout.add_widget(self.movie_list)
        self.add_movie_form = BoxLayout(orientation='vertical')
        self.title_input = TextInput(hint_text="Title")
        self.genre_input = TextInput(hint_text="Genre")
        self.duration_input = TextInput(hint_text="Duration")
        self.add_button = Button(text="Add Movie")
        self.add_button.bind(on_press=self.add_movie)
        self.add_movie_form.add_widget(self.title_input)
        self.add_movie_form.add_widget(self.genre_input)
        self.add_movie_form.add_widget(self.duration_input)
        self.add_movie_form.add_widget(self.add_button)
        layout.add_widget(self.add_movie_form)
        self.manage_buttons = BoxLayout(orientation='vertical')
        self.allocate_watch_time_button = Button(text="Allocate Watch Time")
        self.allocate_watch_time_button.bind(on_press=self.show_watch_time_dropdown)
        self.manage_buttons.add_widget(self.allocate_watch_time_button)
        layout.add_widget(self.manage_buttons)
        self.arrange_movies_section = BoxLayout(orientation='vertical')
        self.priority_slider = Slider(min=0, max=100, value_track=True, value_track_color=(1, 0, 0, 1))
        self.arrange_movies_section.add_widget(self.priority_slider)
        layout.add_widget(self.arrange_movies_section)
        return layout

    def add_movie(self, instance):
        title = self.title_input.text
        genre = self.genre_input.text
        duration = self.duration_input.text
        if title and genre and duration:
            movie = Movie(title, genre, int(duration))
            self.movies.append(movie)
            self.update_movie_list()
            self.title_input.text = ''
            self.genre_input.text = ''
            self.duration_input.text = ''

    def update_movie_list(self):
        self.movie_list.clear_widgets()
        for movie in self.movies:
            label = Label(text=f"{movie.title} ({movie.genre}) - {movie.duration} min")
            self.movie_list.add_widget(label)

    def show_watch_time_dropdown(self, instance):
        dropdown = DropDown()
        for movie in self.movies:
            btn = Button(text=movie.title, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        dropdown.open(self.allocate_watch_time_button)

if __name__ == '__main__':
    MovieManagerApp().run()
