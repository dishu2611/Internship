import tkinter as tk

class AdventureGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Heartstone Adventure")

        self.text_box = tk.Text(root, wrap=tk.WORD, width=40, height=10)
        self.text_box.pack()
        self.text_box.insert(tk.END, "You are an aspiring adventurer on a quest to find the Heartstone. Everything is dark.\n")
        self.text_box.insert(tk.END, "You find yourself in a small village surrounded by lush forests.\n")

        self.choice_frame = tk.Frame(root)
        self.choice_frame.pack()

        self.add_choice("1. Enter the Enchanted Forest", self.enter_enchanted_forest)
        self.add_choice("2. Go to the Misty Mountains", self.go_to_misty_mountains)

    def add_choice(self, text, command):
        button = tk.Button(self.choice_frame, text=text, command=command)
        button.pack()

    def enter_enchanted_forest(self):
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, "You enter the Enchanted Forest which is filled with bright colored flowers and beautiful greenery.\n")
        self.add_choice("1. You hear a faint sound coming from a distance. Follow the faint music", self.follow_faint_music)
        self.add_choice("2. Explore the beautiful enchanted forest", self.explore_forest)

    def go_to_misty_mountains(self):
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, "You head towards the Misty Mountains which are shrouded in mist and fog, making them appear enigmatic and foreboding..\n")
        self.add_choice("1. You see a cave which has a entry. Enter the hidden cave", self.enter_hidden_cave)
        self.add_choice("2. You see a mysterious valley. Explore the mysterious valley", self.explore_mysterious_valley)

    def follow_faint_music(self):
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, "You follow the faint music and discover a tribe.\n")
        self.text_box.insert(tk.END, "They believe you are their leader and help you find the Heartstone.\n")
        self.add_choice("Congratulations! You found the Heartstone. You win!", self.quit_game)

    def explore_forest(self):
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, "You search the forest but do not find the Heartstone.\n")
        self.text_box.insert(tk.END, "Your time in this magical world is over. You lose the game.\n")
        self.add_choice("Game Over. Quit", self.quit_game)

    def enter_hidden_cave(self):
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, "You enter the hidden cave and find a bright light.\n")
        self.text_box.insert(tk.END, "As you approach it you are transported back to normal life. You lose the game.\n")
        self.add_choice("Game Over. Quit", self.quit_game)

    def explore_mysterious_valley(self):
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, "You explore the mysterious valley which is nestled between two imposing mountain ranges, with lush, emerald-green meadows where you find a flower.\n")
        self.text_box.insert(tk.END, " It has a delicate appearance with petals of a deep, iridescent purple color that seem to shimmer and change hues in the soft light of the magical valley where it's found and also emits a fragrance. The flower's fragrance gives you a vision of the route to find the Heartstone.\n")
        self.add_choice("Congratulations! You found the Heartstone. You win!", self.quit_game)

    def quit_game(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = AdventureGame(root)
    root.mainloop()
  