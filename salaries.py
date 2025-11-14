# Function for Selection Sort
def selection_sort(salaries):
    n = len(salaries)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if salaries[j] < salaries[min_index]:
                min_index = j
        salaries[i], salaries[min_index] = salaries[min_index], salaries[i]
    return salaries


# Function for Bubble Sort
def bubble_sort(salaries):
    n = len(salaries)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if salaries[j] > salaries[j + 1]:
                salaries[j], salaries[j + 1] = salaries[j + 1], salaries[j]
    return salaries


# Function to display top 5 highest salaries
def display_top_five(sorted_salaries):
    print("\nTop 5 highest salaries:")
    top_five = sorted_salaries[-5:]  # last 5 are highest
    for salary in reversed(top_five):  # show highest first
        print(f"${salary:.2f}")


# Function to get salaries from user input
def get_salaries():
    salaries = []
    num = int(input("Enter the number of employees: "))
    for i in range(num):
        while True:
            try:
                salary = float(input(f"Enter salary for employee #{i + 1}: "))
                if salary < 0:
                    print("Salary cannot be negative. Try again.")
                    continue
                salaries.append(salary)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    return salaries


# Main Program
def main():
    salaries = get_salaries()

    print("\nChoose sorting algorithm:")
    print("1. Selection Sort")
    print("2. Bubble Sort")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("\nSorting using Selection Sort...")
        sorted_salaries = selection_sort(salaries.copy())
    elif choice == '2':
        print("\nSorting using Bubble Sort...")
        sorted_salaries = bubble_sort(salaries.copy())
    else:
        print("Invalid choice. Exiting program.")
        return

    print("\nSorted salaries (ascending order):")
    print([f"${s:.2f}" for s in sorted_salaries])

    display_top_five(sorted_salaries)


# Run the program
if __name__ == "__main__":
    main()
