#!/usr/bin/env python3
"""
Days Learning - Multilingual Flashcard Application

A Python GUI application for learning days of the week in multiple languages.
"""

import customtkinter as ctk
import sys
from typing import Dict, List

# Set the appearance and color theme for the application
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class DaysLearningApp:
    """
    Main application class for the Days Learning flashcard system.

    Attributes:
        root (ctk.CTk): The main application window.
        current_day_index (int): Index of the currently displayed day.
        days_data (List[Dict[str, str]]): List of dictionaries with day translations.
        language_labels (Dict[str, ctk.CTkLabel]): Mapping of language keys to label widgets.
        prev_button (ctk.CTkButton): Button to navigate to the previous day.
        next_button (ctk.CTkButton): Button to navigate to the next day.
        progress_label (ctk.CTkLabel): Label showing progress through the days.
        day_number_label (ctk.CTkLabel): Label showing the current day number.
    """

    def __init__(self):
        """
        Initialize the application and set up the main window.
        """
        self.root = ctk.CTk()
        self.root.title("Days Learning - Multilingual Flashcards")
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        self.current_day_index = 0
        self.days_data = self._initialize_days_data()

        self._setup_gui()

    def _initialize_days_data(self) -> List[Dict[str, str]]:
        """
        Initialize the days data with translations in all required languages.

        Returns:
            List[Dict[str, str]]: List of dictionaries containing day information in all languages.
        """
        return [
            {
                "english": "Monday",
                "spanish": "Lunes",
                "japanese_romanji": "Getsuyoubi",
                "japanese_hiragana": "げつようび",
                "japanese_kanji": "月曜日"
            },
            {
                "english": "Tuesday",
                "spanish": "Martes",
                "japanese_romanji": "Kayoubi",
                "japanese_hiragana": "かようび",
                "japanese_kanji": "火曜日"
            },
            {
                "english": "Wednesday",
                "spanish": "Miércoles",
                "japanese_romanji": "Suiyoubi",
                "japanese_hiragana": "すいようび",
                "japanese_kanji": "水曜日"
            },
            {
                "english": "Thursday",
                "spanish": "Jueves",
                "japanese_romanji": "Mokuyoubi",
                "japanese_hiragana": "もくようび",
                "japanese_kanji": "木曜日"
            },
            {
                "english": "Friday",
                "spanish": "Viernes",
                "japanese_romanji": "Kinyoubi",
                "japanese_hiragana": "きんようび",
                "japanese_kanji": "金曜日"
            },
            {
                "english": "Saturday",
                "spanish": "Sábado",
                "japanese_romanji": "Doyoubi",
                "japanese_hiragana": "どようび",
                "japanese_kanji": "土曜日"
            },
            {
                "english": "Sunday",
                "spanish": "Domingo",
                "japanese_romanji": "Nichiyoubi",
                "japanese_hiragana": "にちようび",
                "japanese_kanji": "日曜日"
            }
        ]

    def _setup_gui(self):
        """
        Set up the graphical user interface components.
        """
        # Configure grid weights for responsive layout
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        self._create_title_section()
        self._create_flashcard_section()
        self._create_navigation_section()
        self._create_status_section()
        self._update_flashcard()

    def _create_title_section(self):
        """
        Create the application title section.
        """
        title_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        title_frame.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")
        title_frame.grid_columnconfigure(0, weight=1)

        # Main title
        title_label = ctk.CTkLabel(
            title_frame,
            text="Days Learning",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color="#1f538d"
        )
        title_label.grid(row=0, column=0, pady=(0, 5))

        # Subtitle
        subtitle_label = ctk.CTkLabel(
            title_frame,
            text="Multilingual Flashcards",
            font=ctk.CTkFont(size=16),
            text_color="#666666"
        )
        subtitle_label.grid(row=1, column=0)

    def _create_flashcard_section(self):
        """
        Create the main flashcard display section.
        """
        self.flashcard_frame = ctk.CTkFrame(
            self.root,
            fg_color="#f0f8ff",
            corner_radius=15,
            border_width=2,
            border_color="#1f538d"
        )
        self.flashcard_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.flashcard_frame.grid_columnconfigure(0, weight=1)
        self.flashcard_frame.grid_rowconfigure(1, weight=1)

        # Day number indicator
        self.day_number_label = ctk.CTkLabel(
            self.flashcard_frame,
            text="",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#1f538d"
        )
        self.day_number_label.grid(row=0, column=0, pady=(20, 10))

        # Language labels container
        self.language_frame = ctk.CTkFrame(
            self.flashcard_frame,
            fg_color="transparent"
        )
        self.language_frame.grid(row=1, column=0, padx=30, pady=20, sticky="nsew")
        self.language_frame.grid_columnconfigure(0, weight=1)

        # Create language labels for each language
        self.language_labels = {}
        languages = [
            ("english", "English", "#2c3e50"),
            ("spanish", "Español", "#e74c3c"),
            ("japanese_romanji", "Japanese (Romanji)", "#8e44ad"),
            ("japanese_hiragana", "Japanese (Hiragana)", "#27ae60"),
            ("japanese_kanji", "Japanese (Kanji)", "#f39c12")
        ]

        for i, (key, display_name, color) in enumerate(languages):
            # Language name label
            lang_name_label = ctk.CTkLabel(
                self.language_frame,
                text=display_name,
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color=color
            )
            lang_name_label.grid(row=i * 2, column=0, pady=(10, 5), sticky="w")

            # Day name label
            day_label = ctk.CTkLabel(
                self.language_frame,
                text="",
                font=ctk.CTkFont(size=20, weight="bold"),
                text_color="#1f538d"
            )
            day_label.grid(row=i * 2 + 1, column=0, pady=(0, 10), sticky="w")

            self.language_labels[key] = day_label

    def _create_navigation_section(self):
        """
        Create the navigation controls section.
        """
        nav_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        nav_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        nav_frame.grid_columnconfigure(1, weight=1)

        # Previous button
        self.prev_button = ctk.CTkButton(
            nav_frame,
            text="◀ Previous",
            command=self._previous_day,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#3498db",
            hover_color="#2980b9",
            width=120,
            height=40
        )
        self.prev_button.grid(row=0, column=0, padx=(0, 10))

        # Next button
        self.next_button = ctk.CTkButton(
            nav_frame,
            text="Next ▶",
            command=self._next_day,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#3498db",
            hover_color="#2980b9",
            width=120,
            height=40
        )
        self.next_button.grid(row=0, column=2, padx=(10, 0))

        # Progress indicator
        self.progress_label = ctk.CTkLabel(
            nav_frame,
            text="",
            font=ctk.CTkFont(size=14),
            text_color="#666666"
        )
        self.progress_label.grid(row=0, column=1, pady=10)

    def _create_status_section(self):
        """
        Create the status/info section.
        """
        status_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        status_frame.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="ew")

        # Instructions
        instructions_label = ctk.CTkLabel(
            status_frame,
            text="Use the navigation buttons to cycle through the days of the week",
            font=ctk.CTkFont(size=12),
            text_color="#888888"
        )
        instructions_label.pack(pady=5)

        # Keyboard shortcuts info
        shortcuts_label = ctk.CTkLabel(
            status_frame,
            text="Keyboard shortcuts: ⬅️ (Previous), ➡️ (Next), ESC (Exit)",
            font=ctk.CTkFont(size=10),
            text_color="#aaaaaa"
        )
        shortcuts_label.pack(pady=2)

    def _update_flashcard(self):
        """
        Update the flashcard display with current day data.
        """
        current_day = self.days_data[self.current_day_index]

        # Update day number indicator
        day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.day_number_label.configure(
            text=f"Day {self.current_day_index + 1}: {day_names[self.current_day_index]}"
        )

        # Update all language labels
        for key, label in self.language_labels.items():
            label.configure(text=current_day[key])

        # Update progress indicator
        self.progress_label.configure(
            text=f"{self.current_day_index + 1} of {len(self.days_data)}"
        )

        # Update button states
        self.prev_button.configure(
            state="normal" if self.current_day_index > 0 else "disabled"
        )
        self.next_button.configure(
            state="normal" if self.current_day_index < len(self.days_data) - 1 else "disabled"
        )

    def _next_day(self):
        """
        Navigate to the next day.
        """
        if self.current_day_index < len(self.days_data) - 1:
            self.current_day_index += 1
            self._update_flashcard()

    def _previous_day(self):
        """
        Navigate to the previous day.
        """
        if self.current_day_index > 0:
            self.current_day_index -= 1
            self._update_flashcard()

    def _handle_keyboard(self, event):
        """
        Handle keyboard shortcuts for navigation and exit.

        Args:
            event: The keyboard event object.
        """
        if event.keysym == "Left":
            self._previous_day()
        elif event.keysym == "Right":
            self._next_day()
        elif event.keysym == "Escape":
            self.root.quit()

    def run(self):
        """
        Start the application main loop.
        """
        # Bind keyboard events
        self.root.bind("<Key>", self._handle_keyboard)
        self.root.focus_set()

        # Center the window on screen
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

        # Start the main loop
        self.root.mainloop()


def main():
    """
    Main execution function.
    Creates and runs the Days Learning application.
    """
    try:
        app = DaysLearningApp()
        app.run()
    except KeyboardInterrupt:
        print("\nApplication interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
