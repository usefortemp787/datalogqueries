# Define a class to represent assembly in the deductive database
class Assembly:
    def __init__(self, subpart, part, quantity):
        self.part = part
        self.subpart = subpart
        self.quantity = quantity

    def __repr__(self):
        return f"Assembly({self.subpart}, {self.part}, {self.quantity})"

def remove_duplicates(assembly):
    unique_assembly = []
    for fact in assembly:
        is_duplicate = False
        for unique_fact in unique_assembly:
            if fact.part == unique_fact.part and fact.subpart == unique_fact.subpart and fact.quantity == unique_fact.quantity:
                is_duplicate = True
                break
        if not is_duplicate:
            unique_assembly.append(fact)
    return unique_assembly

# Generate all subparts of a given component
def generate_all_subparts(component, assembly):
    print("\n---Parts and Subparts of", component, "---\n")
    print("Part\tSubpart\tQuantity")
    for fact in assembly:
        if fact.part == component:
            print(fact.part, "\t", fact.subpart, "\t", fact.quantity)

def main():
    assembly = [
        Assembly("cpu", "processor", 1),
        Assembly("cooler", "processor", 1),
        Assembly("thermal_paste", "processor", 1),
        Assembly("ram", "memory", 4),
        Assembly("cache", "memory", 1),
        Assembly("controller", "memory", 1),
        Assembly("hdd", "storage", 1),
        Assembly("ssd", "storage", 1),
        Assembly("optical_drive", "storage", 1),
        Assembly("monitor", "peripherals", 1),
        Assembly("keyboard", "peripherals", 1),
        Assembly("mouse", "peripherals", 1),
        Assembly("processor", "computer", 1),
        Assembly("memory", "computer", 2),
        Assembly("storage", "computer", 1),
        Assembly("peripherals", "computer", 1),
    ]

    print("---Applying first rule---\n")
    print("Part\tSubpart\tQuantity")
    for fact in assembly:
        print(fact.part, "\t", fact.subpart, "\t", fact.quantity)

    # Applying the second rule
    assembly = apply_second_rule(assembly)

    print("\n---Applying second rule---\n")
    print("Part\tSubpart\tQuantity")
    for fact in assembly:
        print(fact.part, "\t", fact.subpart, "\t", fact.quantity)

    # Applying the second rule twice
    assembly = apply_second_rule(assembly)
    assembly = remove_duplicates(assembly)

    component = input("\nEnter a component: ")
    generate_all_subparts(component, assembly)

def apply_second_rule(assembly):
    new_facts = []
    for fact1 in assembly:
        for fact2 in assembly:
            if fact1.part == fact2.subpart:
                new_facts.append(Assembly(fact1.subpart, fact2.part, fact1.quantity))
    assembly += new_facts
    return assembly

if __name__ == "__main__":
    main()