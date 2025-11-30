# Calculator Project (Python)

This repository contains two versions of a simple calculator built using Python:

1. **Command-Line Calculator (Beginner Friendly)**
2. **Streamlit Web Calculator (Beginner-Friendly Web App)**

Both versions support basic arithmetic operations such as addition, subtraction, multiplication, and division.  
The project is designed for beginners learning Python basics, functions, loops, error handling, and simple web app development.

---

## Features

### Command-Line Version
- Addition, subtraction, multiplication, division  
- Input validation and error handling  
- Handles division by zero  
- Loop-based structure for continuous calculations  
- Clean and simple Python function-based design  

### Streamlit Web App Version
- Interactive number input fields  
- Operator selection dropdown  
- Displays real-time results  
- Beginner-friendly UI  
- Runs locally in the browser  
- No advanced frameworks required

---

## Technologies Used
- Python  
- Streamlit (for web version)

---

## How to Run the Command-Line Calculator

1. Install Python (if not already installed).  
2. Save the file as `calculator.py`.  
3. Open your terminal or command prompt.  
4. Navigate to the project folder.  
5. Run:

```bash
python calculator.py
```

### Example Output

```
========== Simple Calculator ==========
You can perform: + - * /
Type 'q' to quit.

Enter first number: 10
Enter operator (+, -, *, /): /
Enter second number: 2
Result: 5.0
```

---

## How to Run the Streamlit Web Calculator

### Step 1: Install Streamlit

```bash
pip install streamlit
```

### Step 2: Run the app

```bash
streamlit run cal_streamlit.py
```

Your browser will open automatically at:

```
http://localhost:8501/
```

---

## Future Enhancements

- Add more operations (square root, power, percentage)  
- Add history feature  
- Add GUI version using Tkinter  
- Add a scientific calculator mode  
- Deploy the Streamlit version online  

---

## License

This project is open-source and free to use for learning purposes.
