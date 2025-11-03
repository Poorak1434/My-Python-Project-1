# CLI Billing System

A simple, secure command-line billing and inventory management system in Python. This project allows store owners or students to manage products, update stock, and generate customer bills interactively—all from the terminal, without requiring any database or third-party packages.

## Features

- Master password login for authorized access
- Add, modify, delete, search, and view products
- Real-time stock updates as bills are generated
- Bill creation with automatic stock deduction and totals calculation
- Error handling for invalid input (negative prices, insufficient stock, etc.)
- In-memory product database (data resets each run)
- Pure Python: no external dependencies needed

## Installation

1. Ensure you have Python 3.8 or newer installed.
2. Clone this repository:
   ```
   https://github.com/Poorak1434/My-Python-Project-1.git
   ```
3. Run the script:
   ```
   Assignment.py
   ```

## Usage

- **Login:** Enter the master password (`ironman@123` by default).
- **Main Menu:** Choose actions—add, modify, delete, view, search products, or generate a bill.
- **Add Product:** Provide code, name, price (must be positive), and stock (cannot be negative).
- **Generate Bill:** Enter product codes and quantities, type 'done' to finish. The application calculates totals and updates stock automatically.
- **Search/View Products:** Quickly view inventory or find products by code/name.
- **Exit:** Select "Exit" to safely quit the system.

## Example Workflow

1. Log in with the password.
2. Add product: Code `P001`, Name `Pen`, Price `10`, Stock `100`.
3. View all products: See inventory table.
4. Generate bill: Add `P001` with quantity `5` (total Rs 50), stock now 95.

## Limitations

- Data is not saved between runs. For persistence, consider adding a file/database backend.
- Only one user (master password).
- All product and billing data is managed in memory.

## Project Structure

```
billing-system/
├── Assignment.py          # Main Python script (all logic in one file)
├── README.md        # This documentation
├── LICENSE          # MIT License for open source use
├── .gitignore       # To ignore temporary Python files
└── requirements.txt # (Empty, as no libraries are needed)
```

## Author

Poorak Pandey  
Enrollment No: 2502140055  
B.Tech Computer Science & Data Science (1st Year)

## License

This project is licensed under the MIT License – feel free to use, modify, and share!

***

**Tip:** Replace `yourusername` with your GitHub username in the clone URL above. Update any details as you improve the system or convert it for GUI/database use in future.