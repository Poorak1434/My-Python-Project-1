import subprocess
import os
import json
import time

def run_assignment(inputs):
    """Runs the assignment script with a list of inputs."""
    process = subprocess.Popen(
        ['python', '-u', 'Assignment.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    for line in inputs:
        process.stdin.write(line + '\\n')
        process.stdin.flush()
        time.sleep(0.1)

    process.stdin.close()
    stdout = process.stdout.read()
    stderr = process.stderr.read()

    if stderr:
        print("--- STDERR ---")
        print(stderr)
    return stdout

def test_add_product():
    """Test case for adding a product."""
    print("--- Test: Add Product ---")
    if os.path.exists("products.json"):
        os.remove("products.json")

    inputs_add = [
        'ironman@123',  # password
        '1',            # add product
        'P001',         # product code
        'Test Product', # product name
        '10.50',        # price
        '100',          # stock
        '7'             # exit
    ]
    stdout = run_assignment(inputs_add)

    if "Product 'Test Product' added successfully" not in stdout:
        print("FAIL: Did not see success message for adding product.")
        print(stdout)
        return

    if not os.path.exists("products.json"):
        print("FAIL: products.json was not created.")
        return

    with open("products.json", "r") as f:
        data = json.load(f)

    if "P001" not in data:
        print("FAIL: Product P001 not in products.json.")
        return

    if data["P001"][0] != "Test Product":
        print("FAIL: Product name is incorrect in products.json.")
        return

    print("PASS: Product added and saved successfully.")

def test_load_product():
    """Test case for loading products."""
    print("\\n--- Test: Load Product ---")
    # Assumes test_add_product ran and created the file.
    if not os.path.exists("products.json"):
        print("SKIP: products.json not found. Run add test first.")
        return

    inputs_view = [
        'ironman@123',  # password
        '4',            # view products
        '7'             # exit
    ]
    stdout = run_assignment(inputs_view)

    if 'P001' in stdout and 'Test Product' in stdout and '10.50' in stdout:
        print('PASS: Product was loaded and displayed successfully.')
    else:
        print('FAIL: Product was not found after relaunch.')
        print(stdout)

def test_delete_product():
    """Test case for deleting a product."""
    print("\\n--- Test: Delete Product ---")
    # Assumes test_add_product ran and created the file.
    if not os.path.exists("products.json"):
        print("SKIP: products.json not found. Run add test first.")
        return

    inputs_delete = [
        'ironman@123',  # password
        '3',            # delete product
        'P001',         # product code
        '7'             # exit
    ]
    stdout = run_assignment(inputs_delete)

    if "Product 'Test Product' deleted" not in stdout:
        print("FAIL: Did not see success message for deleting product.")
        print(stdout)
        return

    with open("products.json", "r") as f:
        data = json.load(f)

    if "P001" in data:
        print("FAIL: Product P001 was not removed from products.json.")
        return

    print("PASS: Product deleted successfully.")


if __name__ == "__main__":
    test_add_product()
    test_load_product()
    test_delete_product()
    # Final cleanup
    if os.path.exists("products.json"):
        os.remove("products.json")
