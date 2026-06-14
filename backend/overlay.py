import customtkinter as ctk
import threading

def show_roast(message):

    def popup():

        app = ctk.CTk()

        # Window size
        width = 420
        height = 280

        # Screen position
        screen_width = app.winfo_screenwidth()

        x = screen_width - width - 150
        y = 100

        app.geometry(f"{width}x{height}+{x}+{y}")

        # Window settings
        app.overrideredirect(True)

        app.attributes("-topmost", True)

        app.configure(fg_color="#0f172a")

        # Title
        title = ctk.CTkLabel(
            app,
            text="🤖 RoastOS",
            font=("Consolas", 26, "bold"),
            text_color="#00ff99"
        )

        title.pack(pady=(20, 10))

        # Roast label
        roast_label = ctk.CTkLabel(
            app,
            text="",
            font=("Consolas", 20),
            wraplength=360,
            justify="left",
            text_color="white"
        )

        roast_label.pack(padx=25, pady=10)

        # Typing animation
        def type_text(index=0):

            if index <= len(message):

                roast_label.configure(
                    text=message[:index] + "▋"
                )

                app.after(
                    18,
                    lambda: type_text(index + 1)
                )

            else:

                roast_label.configure(
                    text=message
                )

        # Start typing
        type_text()

        # Auto close
        app.after(8000, app.destroy)

        app.mainloop()

    threading.Thread(
        target=popup,
        daemon=True
    ).start()