from collections import deque

class EventQueue:
    def __init__(self):
        self.queue = deque()

    def add_event(self, event):
        self.queue.append(event)
        print(f"Event '{event}' added to the queue.")

    def process_event(self):
        if self.queue:
            event = self.queue.popleft()
            print(f"Processing event: '{event}'")
        else:
            print("No events to process.")

    def display_events(self):
        if self.queue:
            print("Pending events in the queue:")
            for event in self.queue:
                print(f"- {event}")
        else:
            print("No pending events in the queue.")

    def cancel_event(self, event):
        if event in self.queue:
            self.queue.remove(event)
            print(f"Event '{event}' canceled successfully.")
        else:
            print(f"Event '{event}' not found in queue.")


# ---------------- Main Program ---------------- #
if __name__ == "__main__":
    system = EventQueue()

    while True:
        print("\n--- Event Processing System ---")
        print("1. Add Event")
        print("2. Process Next Event")
        print("3. Display Pending Events")
        print("4. Cancel Event")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            event = input("Enter event name: ")
            system.add_event(event)

        elif choice == '2':
            system.process_event()

        elif choice == '3':
            system.display_events()

        elif choice == '4':
            event = input("Enter event name to cancel: ")
            system.cancel_event(event)

        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
