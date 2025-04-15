import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

class FarmersMarketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Farmers' Market Management System")

        # Database connection
        try:
            print("Attempting to connect to MySQL...")
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Chimuelo1",  # Replace with your actual MySQL password
                port=3306,  # Adjust if your MySQL instance uses a different port
                database="farmers_market"
            )
            self.cursor = self.db.cursor()
            print("Database connection successful!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database connection failed: {err}")
            return

        # Create tabs
        self.tabs = ttk.Notebook(self.root)
        self.products_frame = ttk.Frame(self.tabs)
        self.vendors_frame = ttk.Frame(self.tabs)
        self.tabs.add(self.products_frame, text="Products")
        self.tabs.add(self.vendors_frame, text="Vendors")
        self.tabs.pack(expand=1, fill="both")

        # Setup tabs
        self.setup_products_tab()
        self.setup_vendors_tab()

    def setup_products_tab(self):
        # Form for adding products
        tk.Label(self.products_frame, text="Product Name:").grid(row=0, column=0, padx=5, pady=5)
        self.product_name = tk.Entry(self.products_frame)
        self.product_name.grid(row=0, column=1, padx=5, pady=5)
        self.product_name.config(state="normal")  # Ensure editable

        tk.Label(self.products_frame, text="Category:").grid(row=1, column=0, padx=5, pady=5)
        self.category = tk.Entry(self.products_frame)
        self.category.grid(row=1, column=1, padx=5, pady=5)
        self.category.config(state="normal")  # Ensure editable

        tk.Label(self.products_frame, text="Price:").grid(row=2, column=0, padx=5, pady=5)
        self.price = tk.Entry(self.products_frame)
        self.price.grid(row=2, column=1, padx=5, pady=5)
        self.price.config(state="normal")  # Ensure editable

        tk.Label(self.products_frame, text="Stock:").grid(row=3, column=0, padx=5, pady=5)
        self.stock = tk.Entry(self.products_frame)
        self.stock.grid(row=3, column=1, padx=5, pady=5)
        self.stock.config(state="normal")  # Ensure editable

        tk.Label(self.products_frame, text="Vendor ID:").grid(row=4, column=0, padx=5, pady=5)
        self.vendor_id = tk.Entry(self.products_frame)
        self.vendor_id.grid(row=4, column=1, padx=5, pady=5)
        self.vendor_id.config(state="normal")  # Ensure editable

        # Buttons for product operations
        tk.Button(self.products_frame, text="Add Product", command=self.add_product).grid(row=5, column=1, pady=10)
        tk.Button(self.products_frame, text="Update Product", command=self.update_product).grid(row=5, column=2, pady=10)
        tk.Button(self.products_frame, text="Delete Product", command=self.delete_product).grid(row=6, column=1, pady=10)
        tk.Button(self.products_frame, text="Show Products", command=self.show_products).grid(row=6, column=2, pady=10)

        # Search functionality
        tk.Label(self.products_frame, text="Search by Name:").grid(row=7, column=0, padx=5, pady=5)
        self.search_name = tk.Entry(self.products_frame)
        self.search_name.grid(row=7, column=1, padx=5, pady=5)
        self.search_name.config(state="normal")  # Ensure editable
        tk.Button(self.products_frame, text="Search", command=self.search_products).grid(row=7, column=2, pady=10)

        # Total sales button
        tk.Button(self.products_frame, text="Show Total Sales", command=self.show_total_sales).grid(row=8, column=1, pady=10)

        # Table to display products
        self.products_table = ttk.Treeview(self.products_frame, columns=("ID", "Name", "Category", "Price", "Stock", "Vendor ID"), show="headings")
        self.products_table.heading("ID", text="ID")
        self.products_table.heading("Name", text="Name")
        self.products_table.heading("Category", text="Category")
        self.products_table.heading("Price", text="Price")
        self.products_table.heading("Stock", text="Stock")
        self.products_table.heading("Vendor ID", text="Vendor ID")
        self.products_table.grid(row=9, column=0, columnspan=3, pady=10)

    def setup_vendors_tab(self):
        tk.Label(self.vendors_frame, text="Vendor Name:").grid(row=0, column=0, padx=5, pady=5)
        self.vendor_name = tk.Entry(self.vendors_frame)
        self.vendor_name.grid(row=0, column=1, padx=5, pady=5)
        self.vendor_name.config(state="normal")  # Ensure editable

        tk.Button(self.vendors_frame, text="Add Vendor", command=self.add_vendor).grid(row=1, column=1, pady=10)

    def add_product(self):
        name = self.product_name.get()
        category = self.category.get()
        price = self.price.get()
        stock = self.stock.get()
        vendor_id = self.vendor_id.get()

        if not all([name, category, price, stock, vendor_id]):
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            price = float(price)
            stock = int(stock)
            vendor_id = int(vendor_id)
        except ValueError:
            messagebox.showerror("Error", "Price must be a number, Stock and Vendor ID must be integers")
            return

        try:
            query = "INSERT INTO Products (name, category, price, stock, vendor_id) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(query, (name, category, price, stock, vendor_id))
            self.db.commit()
            messagebox.showinfo("Success", "Product added")
            self.clear_product_form()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to add product: {err}")

    def update_product(self):
        selected = self.products_table.selection()
        if not selected:
            messagebox.showerror("Error", "Select a product to update")
            return

        product_id = self.products_table.item(selected)["values"][0]
        name = self.product_name.get()
        category = self.category.get()
        price = self.price.get()
        stock = self.stock.get()
        vendor_id = self.vendor_id.get()

        if not all([name, category, price, stock, vendor_id]):
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            price = float(price)
            stock = int(stock)
            vendor_id = int(vendor_id)
        except ValueError:
            messagebox.showerror("Error", "Price must be a number, Stock and Vendor ID must be integers")
            return

        try:
            query = "UPDATE Products SET name=%s, category=%s, price=%s, stock=%s, vendor_id=%s WHERE product_id=%s"
            self.cursor.execute(query, (name, category, price, stock, vendor_id, product_id))
            self.db.commit()
            messagebox.showinfo("Success", "Product updated")
            self.show_products()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Update failed: {err}")

    def delete_product(self):
        selected = self.products_table.selection()
        if not selected:
            messagebox.showerror("Error", "Select a product to delete")
            return

        product_id = self.products_table.item(selected)["values"][0]
        try:
            query = "DELETE FROM Products WHERE product_id=%s"
            self.cursor.execute(query, (product_id,))
            self.db.commit()
            messagebox.showinfo("Success", "Product deleted")
            self.show_products()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Delete failed: {err}")

    def show_products(self):
        for row in self.products_table.get_children():
            self.products_table.delete(row)

        try:
            self.cursor.execute("SELECT product_id, name, category, price, stock, vendor_id FROM Products")
            for row in self.cursor.fetchall():
                self.products_table.insert("", tk.END, values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to fetch products: {err}")

    def search_products(self):
        search_term = self.search_name.get()
        for row in self.products_table.get_children():
            self.products_table.delete(row)

        try:
            query = "SELECT product_id, name, category, price, stock, vendor_id FROM Products WHERE name LIKE %s"
            self.cursor.execute(query, (f"%{search_term}%",))
            for row in self.cursor.fetchall():
                self.products_table.insert("", tk.END, values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Search failed: {err}")

    def show_total_sales(self):
        try:
            self.cursor.execute("SELECT SUM(total) FROM Sales")
            total = self.cursor.fetchone()[0]
            messagebox.showinfo("Total Sales", f"Total Sales: ${total:.2f}")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to fetch total sales: {err}")

    def clear_product_form(self):
        self.product_name.delete(0, tk.END)
        self.category.delete(0, tk.END)
        self.price.delete(0, tk.END)
        self.stock.delete(0, tk.END)
        self.vendor_id.delete(0, tk.END)

    def add_vendor(self):
        name = self.vendor_name.get()
        if not name:
            messagebox.showerror("Error", "Vendor name is required")
            return

        try:
            query = "INSERT INTO Vendors (name) VALUES (%s)"
            self.cursor.execute(query, (name,))
            self.db.commit()
            messagebox.showinfo("Success", "Vendor added")
            self.vendor_name.delete(0, tk.END)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to add vendor: {err}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FarmersMarketApp(root)
    root.mainloop()
