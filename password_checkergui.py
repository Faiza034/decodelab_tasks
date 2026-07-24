import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Cyber Security Password Analyzer")
app.geometry("800x600")

# --------------------------
# Show/Hide Password
# --------------------------
def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.configure(show="")
        show_btn.configure(text="🙈 Hide")
    else:
        password_entry.configure(show="*")
        show_btn.configure(text="👁 Show")

# --------------------------
# Password Analysis
# --------------------------
def check_password(event=None):

    password = password_entry.get()

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)

    symbols = "!@#$%^&*()_+-=[]{}|;:',.<>?/"
    has_symbol = any(c in symbols for c in password)

    score = 0

    if len(password) >= 8:score += 1

    if has_upper: score += 1

    if has_lower: score += 1

    if has_digit: score += 1

    if has_symbol:score += 1

    progress.set(score / 5)

    suggestions = []

    if len(password) < 8:
        suggestions.append("• Minimum 8 characters")

    if not has_upper:
        suggestions.append("• Add uppercase letter")

    if not has_lower:
        suggestions.append("• Add lowercase letter")

    if not has_digit:
        suggestions.append("• Add numbers")

    if not has_symbol:
        suggestions.append("• Add special character")

    if score <= 2:
        strength_label.configure(
            text="🔴 WEAK PASSWORD",
            text_color="red"
        )

    elif score <= 4:
        strength_label.configure(
            text="🟡 MEDIUM PASSWORD",
            text_color="orange"
        )

    else:
        strength_label.configure(
            text="🟢 STRONG PASSWORD",
            text_color="green"
        )

    score_label.configure(
        text=f"Security Score: {score}/5"
    )

    if score == 5:
        suggestion_box.configure(
            text="✅ Excellent Password! Highly Secure."
        )
    else:
        suggestion_box.configure(
            text="\n".join(suggestions)
        )

# --------------------------
# Title
# --------------------------
title = ctk.CTkLabel(
    app,
    text="🔐 CYBER SECURITY PASSWORD ANALYZER",
    font=("Arial", 28, "bold")
)

title.pack(pady=25)

# --------------------------
# Password Frame
# --------------------------
password_frame = ctk.CTkFrame(app)

password_frame.pack(pady=15)

password_entry = ctk.CTkEntry(
    password_frame,
    width=450,
    height=45,
    show="*",
    placeholder_text="Enter Password"
)

password_entry.pack(side="left", padx=10)

show_btn = ctk.CTkButton(
    password_frame,
    text="👁 Show",
    width=100,
    command=toggle_password
)

show_btn.pack(side="left")

# Real-Time Analysis
password_entry.bind("<KeyRelease>", check_password)

# --------------------------
# Strength Label
# --------------------------
strength_label = ctk.CTkLabel(
    app,
    text="Enter a Password",
    font=("Arial", 20, "bold")
)

strength_label.pack(pady=15)

# --------------------------
# Progress Bar
# --------------------------
progress = ctk.CTkProgressBar(
    app,
    width=500,
    height=20
)

progress.pack(pady=10)
progress.set(0)

# --------------------------
# Score
# --------------------------
score_label = ctk.CTkLabel(
    app,
    text="Security Score: 0/5",
    font=("Arial", 18)
)

score_label.pack(pady=10)

# --------------------------
# Suggestions Box
# --------------------------
suggestion_box = ctk.CTkLabel(
    app,
    text="Suggestions will appear here",
    justify="left",
    font=("Arial", 16)
)

suggestion_box.pack(pady=25)

# --------------------------
# Footer
# --------------------------
footer = ctk.CTkLabel(
    app,
    text="DecodeLabs Cyber Security Project 1",
    font=("Arial", 12)
)

footer.pack(side="bottom", pady=20)

app.mainloop()