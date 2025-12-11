import random
import os

def main():
    # Welcome message [cite: 14]
    print("Welcome to professor assistant version 1.0.")
    
    # Ask for professor's name [cite: 6, 15]
    name = input("Please Enter Your Name: ")
    
    # Greet the professor [cite: 7, 16]
    print(f"Hello Professor. {'Ibrahim Musa'}, I am here to help you create exams from a question bank.")
    
    while True:
        # Ask if they want to create an exam [cite: 8, 17]
        choice = input("Do you want me to help you create an exam (Yes to proceed | No to quit the program)? ")
        
        # If user says No, quit [cite: 9, 24]
        if choice.strip().lower() == 'no':
            print(f"Thank you professor {"Ibrahim Musa"}. Have a good day!")
            break
            
        # If user says Yes, proceed [cite: 10]
        elif choice.strip().lower() == 'yes':
            # Ask for the path to the question bank [cite: 10, 18]
            file_path = input("Please Enter the Path to the Question Bank. ")
            
            # Check if file exists
            if not os.path.exists(file_path):
                print(f"Error: The file '{file_path}' was not found.")
                continue

            # Read the file 
            try:
                with open(file_path, 'r') as f:
                    # Strip whitespace from lines and remove empty lines
                    lines = [line.strip() for line in f if line.strip()]
                
                # Check formatting: We need pairs (Question + Answer), so lines must be even
                if len(lines) < 2 or len(lines) % 2 != 0:
                     print("Error: File format seems incorrect. Ensure every question has an answer.")
                     continue
                
                print("Yes, indeed the path you provided includes questions and answers.") # [cite: 19]
                
                # Organize lines into pairs (Question, Answer)
                qa_pairs = []
                for i in range(0, len(lines), 2):
                    if i + 1 < len(lines):
                        qa_pairs.append((lines[i], lines[i+1]))
                
                # Ask for number of questions [cite: 10, 20]
                try:
                    num_questions = int(input("How many question-answer pairs do you want to include in your exam? "))
                except ValueError:
                    print("Invalid number entered.")
                    continue

                if num_questions > len(qa_pairs):
                    print(f"Warning: You asked for {num_questions}, but the bank only has {len(qa_pairs)}. Generating {len(qa_pairs)} instead.")
                    num_questions = len(qa_pairs)

                # Ask for save file name [cite: 10, 21]
                output_file = input("Where do you want to save your exam? ")
                
                # Select questions using randint as requested 
                selected_exam = []
                used_indices = []
                
                # Loop until we have the desired number of questions
                while len(selected_exam) < num_questions:
                    # Use randint to pick a random index from the available pairs
                    random_index = random.randint(0, len(qa_pairs) - 1)
                    
                    # Ensure we don't pick the same question twice
                    if random_index not in used_indices:
                        selected_exam.append(qa_pairs[random_index])
                        used_indices.append(random_index)
                
                # Save to output file 
                with open(output_file, 'w') as f_out:
                    for q, a in selected_exam:
                        f_out.write(f"{q}\n{a}\n")
                        
                # Success message [cite: 12, 22]
                print(f"Congratulations Professor {name}. Your exam is created and saved in {output_file}.")
                
                # Loop continues to ask the first question again [cite: 12]

            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                
        else:
            print("Invalid input. Please type 'Yes' or 'No'.")

if __name__ == "__main__":
    main()