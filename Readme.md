# 🧞‍♂️ KeyGenie

Welcome to **KeyGenie**! Your personal assistant for automating text processing and AI-driven text generation right from your keyboard. ✨

## 🚀 Project Overview

**KeyGenie** is a Python-based tool that listens to your keyboard inputs and triggers text processing tasks like generating text, fixing grammar, or paraphrasing content using AI. The project is structured following clean architecture principles for maintainability and scalability.

## 📂 Project Structure

```
project_root/
│
├── services/              # Core services like text processing
│   └── text_processor.py
│
├── use_cases/             # Application logic and workflows
│   └── text_use_case.py
│
├── adapters/              # Interfaces and adapters like keyboard event handling
│   └── keyboard_listener.py
│
└── app.py                 # Main entry point of the application
```

## 🛠️ Installation

To get started with **KeyGenie**, clone the repository and install the required dependencies:

```bash
git clone https://github.com/Deepanshu291/KeyGenie.AI.git
cd keygenie
pip install -r requirements.txt
```

## 📝 Usage

Run the application with:

```bash
python app.py
```

### ✨ Features

- **AI-Driven Text Generation**: Use `$gen` or `$ai` to generate text.
- **Grammar and Punctuation Fixes**: Use `$fix` to clean up your text.
- **Paraphrasing**: Use `$phi3` for paraphrasing text while retaining line breaks.

### 🔧 Commands

- **F7**: Fix selected text.
- **F8**: Paraphrase selected text.
- **$gen, $ai**: Generate text using AI.
- **$fix**: Fix grammar, casing, and punctuation.
- **$phi3**: Paraphrase the selected text.

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## 🛡️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 📧 Contact

For any questions or feedback, reach out at [deepanshu2912001@gmail.com](mailto:deepanshu2912001@gmail.com).

---

Enjoy using **KeyGenie**! 🧙‍♂️✨

---
