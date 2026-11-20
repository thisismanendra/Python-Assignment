import pandas as pd
import matplotlib.pyplot as plt
import os

class SalesDashboard:
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.filename, engine="python")
            print("Sales Data Loaded Successfully!")

            required_columns = ["Date", "Product", "Sales"]

            for column in required_columns:
                if column not in self.data.columns:
                    print(f"Missing column: {column}")
                    return False

            return True

        except FileNotFoundError:
            print("Error: sales.csv file not found!")
            return False

        except Exception as e:
            print("Error loading CSV:", e)
            return False

    def display_data(self):
        print("\nRetail Sales Data:")
        print(self.data)

    def line_graph(self):
        self.data["Date"] = pd.to_datetime(self.data["Date"])

        daily_sales = self.data.groupby("Date")["Sales"].sum()

        plt.plot(daily_sales.index, daily_sales.values, marker='o')
        plt.title("Daily Retail Sales")
        plt.xlabel("Date")
        plt.ylabel("Sales")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def bar_chart(self):
        product_sales = self.data.groupby("Product")["Sales"].sum()

        plt.bar(product_sales.index, product_sales.values)
        plt.title("Product-wise Sales")
        plt.xlabel("Product")
        plt.ylabel("Total Sales")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


dashboard = SalesDashboard(
    os.path.join(os.path.dirname(__file__), "sales.csv")
)

if dashboard.load_data():
    dashboard.display_data()
    dashboard.line_graph()
    dashboard.bar_chart()