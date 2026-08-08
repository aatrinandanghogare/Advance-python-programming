# Dynamic Report Generator using OOP

# Decorator
def border(func):
    def wrapper(self):
        print("=" * 30)
        func(self)
        print("=" * 30)
    return wrapper

class Report:
    template = "Simple Report"

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def set_template(cls, name):
        cls.template = name

    @border
    def display(self):
        print("Template:", Report.template)
        print("Title:", self.title)
        print("Content:", self.content)

    def __str__(self):      # Magic method
        return f"{self.title} - {self.content}"

# Driver Code
Report.set_template("Monthly Report")
r = Report("Sales", "Sales increased by 20%")
r.display()
print(r)
