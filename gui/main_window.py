import tkinter as tk
from tkinter import filedialog, messagebox
from core.sequence_utils import load_fasta
from core.motif_search import overlapping_motif

class MotifFinderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Motif Finder")
        self.root.geometry("800x600")

        # Sequence storage
        self.sequences = {}

        # --- UI Elements ---
        # File selection
        self.file_frame = tk.Frame(root)
        self.file_frame.pack(pady=10)

        self.load_button = tk.Button(self.file_frame, text="Load FASTA File", command=self.load_file)
        self.load_button.pack(side=tk.LEFT, padx=5)

        self.file_label = tk.Label(self.file_frame, text="No file selected")
        self.file_label.pack(side=tk.LEFT)

        # Motif input
        self.motif_frame = tk.Frame(root)
        self.motif_frame.pack(pady=10)

        tk.Label(self.motif_frame, text="Motif:").pack(side=tk.LEFT)
        self.motif_entry = tk.Entry(self.motif_frame, width=20)
        self.motif_entry.pack(side=tk.LEFT, padx=5)

        self.search_button = tk.Button(self.motif_frame, text="Find Motifs", command=self.find_motifs)
        self.search_button.pack(side=tk.LEFT, padx=5)

        # Results display
        self.text_box = tk.Text(root, wrap="word", height=25, width=90)
        self.text_box.pack(pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("FASTA files", "*.fasta *.fa")])
        if file_path:
            self.file_label.config(text=file_path.split("/")[-1])
            try:
                self.sequences = load_fasta(file_path)
                messagebox.showinfo("Success", f"Loaded {len(self.sequences)} sequences.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def find_motifs(self):
        motif = self.motif_entry.get().strip()
        if not motif:
            messagebox.showwarning("Input Error", "Please enter a motif.")
            return
        if not self.sequences:
            messagebox.showwarning("No Sequences", "Please load a FASTA file first.")
            return

        self.text_box.delete(1.0, tk.END)
        for seq_id, seq in self.sequences.items():
            positions = overlapping_motif(seq, motif)
            self.text_box.insert(tk.END, f"{seq_id}:\n")
            self.text_box.insert(tk.END, f"Positions: {positions}\n\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = MotifFinderApp(root)
    root.mainloop()