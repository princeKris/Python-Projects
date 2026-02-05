# Contributing

Thank you for your interest in contributing to this project! 🎉  
This repository is beginner-friendly and open to improvements of all kinds.

---

## Ways to Contribute

- Improve code readability
- Add move validation
- Enhance board display
- Fix bugs
- Improve documentation
- Suggest new features

---

## How to Contribute

### Step 1: Fork the Repository

Click the **Fork** button at the top right of the repository page on GitHub. This creates a copy of the project in your GitHub account.

---

### Step 2: Clone Your Fork

Download your forked repository to your local machine:

```bash
git clone https://github.com/YOUR-USERNAME/terminal-chess-python.git
```

Replace `YOUR-USERNAME` with your actual GitHub username.

Navigate to the project directory:

```bash
cd terminal-chess-python
```

---

### Step 3: Create a New Branch

Create a new branch for your feature or fix. Use a descriptive branch name:

```bash
git checkout -b feature/add-move-validation
```

Or for bugfixes:

```bash
git checkout -b fix/board-display-issue
```

**Branch naming tips:**
- Use `feature/` for new features
- Use `fix/` for bug fixes
- Use `docs/` for documentation updates
- Use `improve/` for code improvements

---

### Step 4: Make Your Changes

Edit the files you want to improve. Some places to focus on:

- **main.py** - Core game logic
- **Code comments** - Make them clearer
- **Function names** - Make them more descriptive
- **README.md** - Improve documentation
- **Code structure** - Simplify complex sections

Test your changes by running the game:

```bash
python main.py
```

Make sure your changes work correctly and don't break existing functionality.

---

### Step 5: Commit Your Changes

Stage your changes:

```bash
git add .
```

Commit with a clear, descriptive message:

```bash
git commit -m "Add move validation feature"
```

**Good commit messages:**
- Be clear and concise
- Explain what you changed and why
- Use present tense: "Add feature" not "Added feature"
- Examples:
  - `Add pawn movement validation`
  - `Fix board display formatting issue`
  - `Improve code comments in main.py`
  - `Update README with new features`

---

### Step 6: Push to Your Fork

Upload your changes to your GitHub fork:

```bash
git push origin feature/add-move-validation
```

Replace `feature/add-move-validation` with your actual branch name.

---

### Step 7: Open a Pull Request

1. Go to the original repository on GitHub
2. Click the **Compare & Pull Request** button (GitHub will usually suggest this)
3. Write a clear title and description of your changes
4. Explain **what** you changed and **why**
5. Click **Create Pull Request**

**In your PR description, include:**
- What problem does this solve?
- What changes did you make?
- How can this be tested?
- Any related issues or discussions?

Example:
```
**Description:**
Adds move validation to prevent invalid pawn moves.

**Changes:**
- Added is_valid_move() function
- Updated move_piece() to validate before moving
- Added unit tests for pawn movement

**How to test:**
Run python main.py and try invalid moves
```

---

### Step 8: Wait for Review

- The maintainers will review your pull request
- They may ask for changes or suggest improvements
- Be open to feedback and make requested changes
- Your contribution will be merged once approved!

---

### Have Issues?

If you run into problems:

1. Check that you're on the correct branch:
   ```bash
   git branch
   ```

2. See your changes:
   ```bash
   git diff
   ```

3. Undo changes (if needed):
   ```bash
   git checkout -- filename.py
   ```

4. Still stuck? Open an issue to ask for help!

---

## Guidelines

- Keep code simple and readable
- Follow existing coding style
- Write clear commit messages
- Avoid unnecessary complexity

---

## 👥 Contributors

- [Krishnakumar G](https://github.com/your-username) - Project Creator

*Add your name here when you contribute!*

---

## ❓ Questions or Ideas?

Feel free to open an issue to discuss improvements or ideas.

