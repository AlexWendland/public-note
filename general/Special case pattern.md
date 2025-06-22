---
aliases:
  - special case pattern
checked: false
created: 2023-08-20
last_edited: 2023-11-11
draft: false
tags:
  - programming
type: design pattern
---
# Special case pattern

The Special Case Pattern is a design pattern used in software development to handle exceptional conditions without resorting to conditional logic scattered throughout the code. Essentially, it allows you to model what would be a "special case" as an object of the same type as the typical cases. By doing so, you can reduce the need for conditional logic to check for these cases, making the code more maintainable and easier to understand.

## How It Works

Let's consider a simple example in some accounting software to calculate the refund for an a business trip.

```python
class ExpenseReport:
...
	def get_meals(self, id:str) -> MealExpenses:
		if id not in self.meal_expenses:
			raise MealExpensesNotFound(
				f"Employee {id} not found in Expense report {self.report_id})"
			)
		return self.meal_expenses[id]
...

def get_trip_refund(
	employees_on_trip: List[Employee],
	expense_report:ExpenseReport
) -> float:
	total = 0
	for employee in employees_on_trip:
		try:
			expenses = expense_report.get_meals(employee.get_id())
			total += expenses.get_total()
		except MealExpensesNotFound:
			total += get_meal_per_diem()
	return total
```

Here if the employees meal was expensed they will get the cost of those meal however if they didn't then they get a pre diem for the days they were away. It would be good to get rid of the exception logic that clutters up the function `get_trip_refund`. We could do this by handling the special case as another version of the object `MealExpenses` as follows.

```python
class PerDiemMealExpenses(MealExpenses):
	def get_total(self):
		return get_meal_per_diem()

class ExpenseReport:
...
	def get_meals(self, id:str) -> MealExpenses:
		if id not in self.meal_expenses:
			return PerDiemMealExpenses()
		return self.meal_expenses[id]
...

def get_trip_refund(
	employees_on_trip: List[Employee],
	expense_report:ExpenseReport
) -> float:
	total = 0
	for employee in employees_on_trip:
		expenses = expense_report.get_meals(employee.get_id())
		total += expenses.get_total()
	return total
```

### Benefits

1. **Polymorphism**: Utilizes [[Polymorphism|polymorphism]] to handle different behaviours between a regular object and its special case, keeping the API consistent.
2. **Reduced Conditional Logic**: Helps in minimizing `if` or `switch` statements in your code to check for special cases.
3. **Code Reusability**: Makes it easier to add more special cases in the future without modifying existing code, adhering to the [[Open Closed Principle (OCP)|Open Closed principle]].
4. **Readability**: Improves code readability by eliminating clutter introduced by numerous conditional statements.

### When to Use

1. **Complex Exception Handling**: When you have complex rules for handling special cases that would otherwise clutter your main class with conditional logic.
2. **Multiple Clients**: When multiple parts of your application need to deal with a special case, encapsulating this in a class prevents code duplication.
3. **Future-Proofing**: When you anticipate adding more special cases or exceptions in the future.

### Summary

The Special Case Pattern provides a clean way to handle special or exceptional conditions by encapsulating them in their own classes. This makes the code more maintainable, readable, and adheres to the [[Open Closed Principle (OCP)|Open Closed principle]]. It's a technique that can be particularly useful in larger, more complex applications where special cases are numerous and subject to change.
