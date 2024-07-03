import sys
import os
from qa_system import answer_question

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <pdf_file_path> <question>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    question = sys.argv[2]

    if not os.path.exists(pdf_path):
        print(f"Error: The file '{pdf_path}' does not exist.")
        sys.exit(1)

    try:
        answer = answer_question(pdf_path, question)
        print("Answer:", answer)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()