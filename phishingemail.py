import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import re
from urllib.parse import urlparse
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ==========================================
# DATA
# ==========================================

PHISHING_KEYWORDS = [
    "urgent",
    "verify your account",
    "click here",
    "account suspended",
    "login now",
    "password",
    "bank account",
    "winner",
    "free money",
    "claim reward",
    "limited time",
    "security alert",
    "update payment",
    "confirm identity"
]

SUSPICIOUS_DOMAINS = [
    ".xyz",
    ".tk",
    ".top",
    ".click",
    ".live",
    ".info"
]

last_report = ""

# ==========================================
# FILE UPLOAD
# ==========================================

def load_email_file():

    file_path = filedialog.askopenfilename(
        title="Select Email File",
        filetypes=[("Text Files", "*.txt")]
    )

    if not file_path:
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        email_input.delete("1.0", tk.END)
        email_input.insert(tk.END, content)

        messagebox.showinfo(
            "Success",
            "Email loaded successfully!"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )

# ==========================================
# ANALYSIS FUNCTIONS
# ==========================================

def extract_urls(text):
    return re.findall(r'https?://[^\s]+', text)


def check_keywords(text):

    found = []

    for keyword in PHISHING_KEYWORDS:
        if keyword.lower() in text.lower():
            found.append(keyword)

    return found


def analyze_urls(urls):

    suspicious = []

    for url in urls:

        parsed = urlparse(url)

        for domain in SUSPICIOUS_DOMAINS:

            if parsed.netloc.endswith(domain):
                suspicious.append(url)

    return suspicious


def calculate_score(keyword_count, suspicious_url_count):

    score = 0

    score += keyword_count * 10
    score += suspicious_url_count * 25

    if keyword_count >= 3:
        score += 15

    if suspicious_url_count >= 1:
        score += 20

    return min(score, 100)


def classify(score):

    if score >= 70:
        return "HIGH RISK PHISHING EMAIL", "red"

    elif score >= 40:
        return "SUSPICIOUS EMAIL", "orange"

    return "LIKELY SAFE", "green"

# ==========================================
# PIE CHART
# ==========================================

def show_chart(score):

    for widget in chart_frame.winfo_children():
        widget.destroy()

    fig = plt.Figure(figsize=(4, 4))
    ax = fig.add_subplot(111)

    safe = 100 - score
    risk = score

    ax.pie(
        [safe, risk],
        labels=["Safe", "Risk"],
        autopct="%1.1f%%"
    )

    ax.set_title("Risk Analysis")

    canvas = FigureCanvasTkAgg(
        fig,
        master=chart_frame
    )

    canvas.draw()
    canvas.get_tk_widget().pack()

# ==========================================
# PDF EXPORT
# ==========================================

def export_pdf():

    global last_report

    if not last_report:
        messagebox.showwarning(
            "Warning",
            "Analyze an email first."
        )
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not file_path:
        return

    doc = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()

    content = [
        Paragraph(
            "Phishing Email Analysis Report",
            styles["Title"]
        ),
        Spacer(1, 12),
        Paragraph(
            last_report.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    ]

    doc.build(content)

    messagebox.showinfo(
        "Success",
        "PDF exported successfully!"
    )

# ==========================================
# ANALYZE EMAIL
# ==========================================

def analyze_email():

    global last_report

    email_text = email_input.get(
        "1.0",
        tk.END
    )

    if not email_text.strip():

        messagebox.showwarning(
            "Warning",
            "Please enter email content."
        )
        return

    urls = extract_urls(email_text)

    keywords = check_keywords(email_text)

    suspicious_urls = analyze_urls(urls)

    score = calculate_score(
        len(keywords),
        len(suspicious_urls)
    )

    status, color = classify(score)

    report = f"""
PHISHING EMAIL ANALYSIS REPORT

Risk Score: {score}/100

Classification:
{status}

---------------------------------

Detected URLs:

{chr(10).join(urls) if urls else "None"}

---------------------------------

Suspicious URLs:

{chr(10).join(suspicious_urls) if suspicious_urls else "None"}

---------------------------------

Detected Keywords:

{chr(10).join(keywords) if keywords else "None"}

---------------------------------

Security Recommendation:

{"DO NOT click suspicious links or share information."
if score >= 70 else
"Verify sender before taking action."}
"""

    last_report = report

    result_box.delete(
        "1.0",
        tk.END
    )

    result_box.insert(
        tk.END,
        report
    )

    status_label.config(
        text=status,
        fg=color
    )

    show_chart(score)

# ==========================================
# UI
# ==========================================

root = tk.Tk()
root.title("Phishing Email Detector")
root.geometry("1200x750")
root.configure(bg="#1a1a2e")

title = tk.Label(
    root,
    text="🔐 Phishing Email Detector",
    bg="#1a1a2e",
    fg="white",
    font=("Arial", 24, "bold")
)
title.pack(pady=10)

email_input = scrolledtext.ScrolledText(
    root,
    width=120,
    height=12,
    font=("Consolas", 10)
)
email_input.pack(pady=10)

button_frame = tk.Frame(
    root,
    bg="#1a1a2e"
)
button_frame.pack()

upload_btn = tk.Button(
    button_frame,
    text="Upload Email",
    command=load_email_file,
    bg="#9C27B0",
    fg="white",
    font=("Arial", 11, "bold"),
    width=18
)
upload_btn.grid(row=0, column=0, padx=10)

analyze_btn = tk.Button(
    button_frame,
    text="Analyze Email",
    command=analyze_email,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    width=18
)
analyze_btn.grid(row=0, column=1, padx=10)

pdf_btn = tk.Button(
    button_frame,
    text="Export PDF",
    command=export_pdf,
    bg="#2196F3",
    fg="white",
    font=("Arial", 11, "bold"),
    width=18
)
pdf_btn.grid(row=0, column=2, padx=10)

status_label = tk.Label(
    root,
    text="Waiting For Analysis",
    bg="#1a1a2e",
    fg="yellow",
    font=("Arial", 15, "bold")
)
status_label.pack(pady=15)

content_frame = tk.Frame(
    root,
    bg="#1a1a2e"
)
content_frame.pack(fill="both", expand=True)

result_box = scrolledtext.ScrolledText(
    content_frame,
    width=70,
    height=20,
    font=("Consolas", 10)
)
result_box.pack(
    side=tk.LEFT,
    padx=15,
    pady=10
)

chart_frame = tk.Frame(
    content_frame,
    bg="#1a1a2e"
)
chart_frame.pack(
    side=tk.RIGHT,
    padx=20
)

root.mainloop()